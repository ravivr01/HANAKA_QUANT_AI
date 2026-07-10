"""
==========================================================
HQAI Yahoo Finance Provider
Release : R-005-001
Author  : Hanaka Quant AI

Yahoo Finance Market Data Provider
Compatible with:
    Python 3.12
    yfinance 1.4.x
==========================================================
"""

from __future__ import annotations

import pandas as pd
import yfinance as yf

from hqai.core.logger import log
from hqai.marketdata.base import BaseProvider
from hqai.marketdata.registry import registry


class YahooProvider(BaseProvider):
    """
    Yahoo Finance Provider
    """

    @property
    def name(self) -> str:
        return "yahoo"

    ########################################################

    def connect(self) -> None:

        log.info("Yahoo Provider Ready")

    ########################################################

    def disconnect(self) -> None:

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
            tickers=ticker,
            period=period,
            interval=interval,
            auto_adjust=False,
            progress=False,
            threads=False,
        )

        if df.empty:
            raise RuntimeError(f"No data returned for {ticker}")

        df.reset_index(inplace=True)

        # Flatten MultiIndex columns if present
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [c[0] for c in df.columns]

        # Standardize column names
        df.columns = [str(col).upper().replace(" ", "_") for col in df.columns]

        df["SYMBOL"] = symbol.upper()

        required = [
            "DATE",
            "OPEN",
            "HIGH",
            "LOW",
            "CLOSE",
            "VOLUME",
            "SYMBOL",
        ]

        missing = [c for c in required if c not in df.columns]

        if missing:
            raise RuntimeError(f"Missing columns: {missing}")

        return df

    ########################################################

    def validate(self) -> bool:

        try:

            df = self.download_symbol(
                "INFY",
                period="5d",
            )

            return not df.empty

        except Exception as ex:

            log.error(ex)

            return False

    ########################################################

    def metadata(self) -> dict:

        return {
            "provider": "Yahoo Finance",
            "exchange": "NSE",
            "supports_history": True,
            "supports_intraday": True,
            "default_period": "5y",
            "default_interval": "1d",
        }


registry.register(
    "yahoo",
    YahooProvider,
)
