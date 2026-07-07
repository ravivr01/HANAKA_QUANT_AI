"""
==========================================================
HQAI History Downloader
==========================================================

Downloads historical data from Yahoo Finance
and saves immediately to Bronze Storage.

Author  : Ravi Varma
Version : 1.0
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yfinance as yf
from tqdm import tqdm

from hqai.core.database import db
from hqai.core.logger import log


class HistoryDownloader:

    def __init__(self):

        self.period = "5y"

        self.interval = "1d"

        self.output = Path("data/bronze/history")

        self.output.mkdir(
            parents=True,
            exist_ok=True,
        )

    # -----------------------------------------------------

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

    # -----------------------------------------------------

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
            progress=False,
            auto_adjust=False,
            threads=False,
        )

        if df.empty:

            raise Exception(
                f"No data : {ticker}"
            )

        df.reset_index(inplace=True)

        if isinstance(df.columns, pd.MultiIndex):

            df.columns = [
                c[0]
                for c in df.columns
            ]

        df["SYMBOL"] = symbol

        return df

    # -----------------------------------------------------

    def save_symbol(
        self,
        df: pd.DataFrame,
        symbol: str,
    ):

        file = self.output / f"{symbol}.parquet"

        df.to_parquet(
            file,
            index=False,
        )

        log.success(
            f"Saved {file}"
        )

    # -----------------------------------------------------

    def download_many(
        self,
        symbols: list[str],
    ):

        success = 0

        failed = []

        for symbol in tqdm(
            symbols,
            desc="Downloading History",
        ):

            try:

                df = self.download_symbol(
                    symbol
                )

                self.save_symbol(
                    df,
                    symbol,
                )

                success += 1

                del df

            except Exception as ex:

                log.error(
                    f"{symbol} : {ex}"
                )

                failed.append(symbol)

        log.info("=" * 60)

        log.success(
            f"Downloaded : {success}"
        )

        log.warning(
            f"Failed : {len(failed)}"
        )

        return failed

    # -----------------------------------------------------

    def download_all(self):

        universe = self.load_universe()

        symbols = universe["SYMBOL"].to_list()

        return self.download_many(
            symbols
        )