"""
==========================================================
HQAI Market Data Provider Interface
Release : R-005-001
Author  : Hanaka Quant AI

Abstract interface for all Market Data Providers.
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class BaseProvider(ABC):
    """
    Abstract Market Data Provider.

    Every provider (Yahoo, NSE, Polygon, AlphaVantage, etc.)
    must implement this interface.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Provider name."""
        raise NotImplementedError

    @abstractmethod
    def connect(self) -> None:
        """Initialize provider."""
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> None:
        """Close provider."""
        raise NotImplementedError

    @abstractmethod
    def validate(self) -> bool:
        """Return True if provider is healthy."""
        raise NotImplementedError

    @abstractmethod
    def metadata(self) -> dict:
        """Provider metadata."""
        raise NotImplementedError

    @abstractmethod
    def download_symbol(
        self,
        symbol: str,
        period: str = "5y",
        interval: str = "1d",
    ) -> pd.DataFrame:
        """
        Download one symbol.

        Parameters
        ----------
        symbol
            NSE symbol without '.NS'

        period
            Default 5 years

        interval
            Default daily
        """
        raise NotImplementedError

    def download_many(
        self,
        symbols: list[str],
        period: str = "5y",
        interval: str = "1d",
    ) -> dict[str, pd.DataFrame]:
        """
        Default sequential implementation.

        Providers may override this with a faster
        implementation if supported.
        """

        result: dict[str, pd.DataFrame] = {}

        for symbol in symbols:
            result[symbol] = self.download_symbol(
                symbol=symbol,
                period=period,
                interval=interval,
            )

        return result
