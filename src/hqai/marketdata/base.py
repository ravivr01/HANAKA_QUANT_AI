"""
==========================================================
HQAI Market Data Base Provider
==========================================================

Defines the interface for all market data providers.

Author  : Ravi Varma
Release : 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class BaseProvider(ABC):
    """
    Abstract Market Data Provider.

    Every provider must implement the same interface.
    """

    ########################################################

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Provider name.
        """
        ...

    ########################################################

    @abstractmethod
    def connect(self):
        """
        Connect to provider.
        """
        ...

    ########################################################

    @abstractmethod
    def disconnect(self):
        """
        Close provider connection.
        """
        ...

    ########################################################

    @abstractmethod
    def download_symbol(
        self,
        symbol: str,
        period: str = "5y",
        interval: str = "1d",
    ) -> pd.DataFrame:
        """
        Download one symbol.
        """
        ...

    ########################################################

    @abstractmethod
    def download_many(
        self,
        symbols: list[str],
        period: str = "5y",
        interval: str = "1d",
    ) -> dict[str, pd.DataFrame]:
        """
        Download multiple symbols.
        """
        ...

    ########################################################

    @abstractmethod
    def validate(self) -> bool:
        """
        Validate provider.
        """
        ...

    ########################################################

    @abstractmethod
    def metadata(self) -> dict:
        """
        Provider metadata.
        """
        ...
