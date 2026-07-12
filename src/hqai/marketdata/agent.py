"""
==========================================================
HQAI Market Data Agent
==========================================================

Coordinates Market Data download pipeline.

Release : 1.1.0
Author  : Hanaka Quant AI
"""

from __future__ import annotations

import polars as pl

from hqai.core.logger import log

# Force provider registration
import hqai.marketdata.providers  # noqa: F401

from hqai.marketdata.registry import registry
from hqai.marketdata.storage import MarketDataStorage
from hqai.marketdata.validator import MarketDataValidator
from hqai.marketdata.metadata import MarketDataMetadata


class MarketDataAgent:
    """
    HQAI Market Data Agent

    Responsibilities
    ----------------
    - Download market data
    - Validate data
    - Store Bronze data
    - Create metadata
    - Synchronize entire universe
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

    ########################################################

    def build(
        self,
        symbol: str,
    ):

        log.info(f"Downloading {symbol}")

        df = self.provider.download_symbol(symbol)

        if isinstance(df, pl.DataFrame):

            pdf = df.to_pandas()

        else:

            pdf = df

        pdf.columns = [
            column.upper().replace(" ", "_")
            for column in pdf.columns
        ]

        dataframe = pl.from_pandas(pdf)

        self.validator.validate(dataframe)

        self.storage.save(
            symbol=symbol,
            df=dataframe,
            provider=self.provider.name,
        )

        metadata = MarketDataMetadata.create(
            symbol=symbol,
            provider=self.provider.name,
            rows=dataframe.height,
            first_date=dataframe["DATE"].min(),
            last_date=dataframe["DATE"].max(),
        )

        metadata.save(
            self.storage.metadata_file(symbol)
        )

        log.info(f"{symbol} completed.")

    ########################################################

    def sync_universe(self):

        """
        Download historical data for every symbol
        in the Universe table.
        """

        from hqai.core.database import db

        symbols = db.query(
            """
            SELECT SYMBOL
            FROM universe
            ORDER BY SYMBOL
            """
        )

        total = symbols.height

        success = 0

        failed = 0

        log.info("=" * 70)
        log.info("Starting Universe Synchronization")
        log.info(f"Total Symbols : {total}")
        log.info("=" * 70)

        for index, row in enumerate(
            symbols.iter_rows(named=True),
            start=1,
        ):

            symbol = row["SYMBOL"]

            log.info(
                f"[{index}/{total}] {symbol}"
            )

            try:

                self.build(symbol)

                success += 1

            except Exception as ex:

                failed += 1

                log.error(
                    f"{symbol} -> {ex}"
                )

        log.info("=" * 70)
        log.info("Universe Synchronization Complete")
        log.info(f"Total   : {total}")
        log.info(f"Success : {success}")
        log.info(f"Failed  : {failed}")
        log.info("=" * 70)

    ########################################################

    def validate(self):

        return self.provider.validate()

    ########################################################

    def summary(self):

        return self.storage.summary()

    ########################################################

    def clean(self):

        for symbol in self.storage.list_symbols():

            self.storage.delete(symbol)

        log.info("Bronze storage cleaned.")