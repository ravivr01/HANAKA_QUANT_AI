"""
==========================================================
HQAI Market Data Base Provider
Release : 1.0.2
Module  : Market Data Engine

Defines the interface for all market data providers.
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

__all__ = [
    "BaseProvider",
]


class BaseProvider(ABC):
    """
    Abstract base class for all market data providers.

    Every provider (Yahoo, NSE, Polygon, AlphaVantage, etc.)
    must implement this interface.
    """

    ########################################################
    # Provider Name
    ########################################################

    @property
    @abstractmethod
    def name(self) -> str:
        """Provider name."""
        ...

    ########################################################
    # Connection
    ########################################################

    @abstractmethod
    def connect(self) -> None:
        """Open provider connection."""
        ...

    ########################################################

    @abstractmethod
    def disconnect(self) -> None:
        """Close provider connection."""
        ...

    ########################################################
    # Download One Symbol
    ########################################################

    @abstractmethod
    def download_symbol(
        self,
        symbol: str,
        period: str = "5y",
        interval: str = "1d",
    ) -> pd.DataFrame:
        """
        Download historical market data for one symbol.
        """
        ...

    ########################################################
    # Download Multiple Symbols
    ########################################################

    @abstractmethod
    def download_many(
        self,
        symbols: list[str],
        period: str = "5y",
        interval: str = "1d",
    ) -> dict[str, pd.DataFrame]:
        """
        Download historical data for multiple symbols.
        """
        ...

    ########################################################
    # Validation
    ########################################################

    @abstractmethod
    def validate(self) -> bool:
        """
        Validate provider connectivity.
        """
        ...

    ########################################################
    # Metadata
    ########################################################

    @abstractmethod
    def metadata(self) -> dict:
        """
        Return provider metadata.
        """
        ...
