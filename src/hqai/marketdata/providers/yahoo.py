"""
==========================================================
HQAI Yahoo Market Data Provider
Release : 1.0.5
Module  : Market Data Engine

Yahoo Finance implementation of BaseProvider.
==========================================================
"""

from __future__ import annotations

import pandas as pd
import yfinance as yf

from hqai.core.logger import log
from hqai.marketdata.base import BaseProvider
from hqai.marketdata.registry import registry

__all__ = ["YahooProvider"]


class YahooProvider(BaseProvider):
    """
    Yahoo Finance Provider for NSE equities.
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

        ticker = f"{symbol.upper()}.NS"

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

        df.columns = [column.upper().replace(" ", "_") for column in df.columns]

        df["SYMBOL"] = symbol.upper()

        df = (
            df.sort_values("DATE").drop_duplicates(subset="DATE").reset_index(drop=True)
        )

        return df

    ########################################################

    def download_many(
        self,
        symbols: list[str],
        period: str = "5y",
        interval: str = "1d",
    ) -> dict[str, pd.DataFrame]:

        datasets: dict[str, pd.DataFrame] = {}

        for symbol in symbols:

            try:

                datasets[symbol] = self.download_symbol(
                    symbol=symbol,
                    period=period,
                    interval=interval,
                )

            except Exception as ex:

                log.error(f"{symbol} -> {ex}")

        return datasets

    ########################################################

    def validate(self) -> bool:

        try:

            self.download_symbol(
                "INFY",
                period="5d",
            )

            return True

        except Exception as ex:

            log.error(ex)

            return False

    ########################################################

    def metadata(self) -> dict:

        return {
            "name": "Yahoo Finance",
            "exchange": "NSE",
            "supports_intraday": True,
            "supports_history": True,
            "supports_incremental": True,
        }


if not registry.exists("yahoo"):
    registry.register(
        "yahoo",
        YahooProvider,
    )
