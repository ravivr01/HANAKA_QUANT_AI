"""
==========================================================
HQAI Yahoo Market Data Provider
==========================================================

Yahoo Finance implementation of BaseProvider.

Author  : Ravi Varma
Release : 1.0.3
"""

from __future__ import annotations

import pandas as pd
import yfinance as yf

from hqai.core.logger import log
from hqai.marketdata.base import BaseProvider
from hqai.marketdata.registry import registry


class YahooProvider(BaseProvider):
    """
    Yahoo Finance Provider.
    """

    @property
    def name(self) -> str:
        return "yahoo"

    ########################################################

    def connect(self):

        log.info("Yahoo Provider Ready")

    ########################################################

    def disconnect(self):

        log.info("Yahoo Provider Closed")

    ########################################################

    def download_symbol(
        self,
        symbol: str,
        period: str = "5y",
        interval: str = "1d",
    ) -> pd.DataFrame:

        ticker = f"{symbol}.NS"

        log.info(f"Downloading {ticker}")

        df = yf.download(
            ticker,
            period=period,
            interval=interval,
            auto_adjust=False,
            progress=False,
            threads=False,
        )

        if df.empty:

            raise RuntimeError(f"No data returned for {ticker}")

        df.reset_index(inplace=True)

        if isinstance(df.columns, pd.MultiIndex):

            df.columns = [column[0] for column in df.columns]

        df["SYMBOL"] = symbol

        return df

    ########################################################

    def download_many(
        self,
        symbols: list[str],
        period: str = "5y",
        interval: str = "1d",
    ) -> dict[str, pd.DataFrame]:

        result = {}

        for symbol in symbols:

            try:

                result[symbol] = self.download_symbol(
                    symbol,
                    period,
                    interval,
                )

            except Exception as ex:

                log.error(f"{symbol} -> {ex}")

        return result

    ########################################################

    def validate(self) -> bool:

        try:

            self.download_symbol("INFY", period="5d")

            return True

        except Exception:

            return False

    ########################################################

    def metadata(self) -> dict:

        return {
            "name": "Yahoo Finance",
            "exchange": "NSE",
            "supports_intraday": True,
            "supports_history": True,
        }


registry.register(
    "yahoo",
    YahooProvider,
)
