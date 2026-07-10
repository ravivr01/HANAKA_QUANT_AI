"""
==========================================================
HQAI Market Data Agent
Release : R-005-005A
Module  : Market Data Engine

Universe Loader
==========================================================
"""

from __future__ import annotations

import polars as pl

from hqai.core.database import db
from hqai.core.logger import log

# Ensure provider registration
import hqai.marketdata.providers.yahoo  # noqa: F401

from hqai.marketdata.registry import registry
from hqai.marketdata.storage import MarketDataStorage
from hqai.marketdata.validator import MarketDataValidator


class MarketDataAgent:
    """
    HQAI Market Data Agent.

    Coordinates the Market Data Engine.
    """

    ########################################################

    def __init__(
        self,
        provider: str = "yahoo",
    ):

        Provider = registry.get(provider)

        self.provider = Provider()

        self.storage = MarketDataStorage()

        self.validator = MarketDataValidator()

        log.info(f"Provider : {self.provider.name}")

    ########################################################

    def universe(self) -> pl.DataFrame:
        """
        Load the production NSE universe.
        """

        return db.query("""
            SELECT SYMBOL
            FROM universe
            WHERE SERIES='EQ'
            ORDER BY SYMBOL
            """)

    ########################################################

    def universe_symbols(self) -> list[str]:

        universe = self.universe()

        return universe["SYMBOL"].to_list()

    ########################################################

    def summary(self) -> dict:

        symbols = self.universe_symbols()

        return {
            "provider": self.provider.name,
            "universe": len(symbols),
            "storage": self.storage.summary(),
        }

    ########################################################

    def sync(self):

        symbols = self.universe_symbols()

        log.info("=" * 60)

        log.info("HQAI MARKET DATA ENGINE")

        log.info("=" * 60)

        log.info(f"Provider : {self.provider.name}")

        log.info(f"Universe : {len(symbols)} symbols")

        log.info("=" * 60)

        return symbols
