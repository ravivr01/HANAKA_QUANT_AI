"""
==========================================================
HQAI History Downloader
==========================================================

Downloads historical market data from Yahoo Finance
and delegates persistence to HistoryStorage.

Author  : Ravi Varma
Version : 2.0
"""

from __future__ import annotations

import gc

import pandas as pd
import yfinance as yf
from tqdm import tqdm

from hqai.core.database import db
from hqai.core.logger import log
from hqai.history.storage import HistoryStorage


class HistoryDownloader:

    def __init__(self):

        self.period = "5y"

        self.interval = "1d"

        self.storage = HistoryStorage()

    # --------------------------------------------------

    def load_universe(self) -> pd.DataFrame:

        log.info("Loading Universe")

        universe = db.query(
            """
            SELECT *
            FROM universe
            ORDER BY SYMBOL
            """
        )

        log.success(
            f"{len(universe)} symbols loaded."
        )

        return universe

    # --------------------------------------------------

    def download_symbol(
        self,
        symbol: str,
    ) -> pd.DataFrame:

        ticker = f"{symbol}.NS"

        log.info(
            f"Downloading {ticker}"
        )

        df = yf.download(
            ticker,
            period=self.period,
            interval=self.interval,
            auto_adjust=False,
            progress=False,
            threads=False,
        )

        if df.empty:

            raise RuntimeError(
                f"No data returned for {ticker}"
            )

        df.reset_index(inplace=True)

        if isinstance(df.columns, pd.MultiIndex):

            df.columns = [c[0] for c in df.columns]

        df["SYMBOL"] = symbol

        return df

    # --------------------------------------------------

    def download_many(
        self,
        symbols: list[str],
    ) -> list[str]:

        success = 0

        skipped = 0

        failed = []

        for symbol in tqdm(
            symbols,
            desc="History Download",
        ):

            try:

                if self.storage.exists(symbol):

                    skipped += 1

                    continue

                df = self.download_symbol(symbol)

                self.storage.save(
                    df,
                    symbol,
                )

                self.storage.register(
                    symbol,
                )

                success += 1

                del df

                gc.collect()

            except Exception as ex:

                log.error(
                    f"{symbol} -> {ex}"
                )

                failed.append(symbol)

        log.info("=" * 60)

        log.success(
            f"Downloaded : {success}"
        )

        log.info(
            f"Skipped     : {skipped}"
        )

        log.warning(
            f"Failed      : {len(failed)}"
        )

        return failed

    # --------------------------------------------------

    def download_all(self):

        universe = self.load_universe()

        symbols = universe["SYMBOL"].to_list()

        return self.download_many(symbols)