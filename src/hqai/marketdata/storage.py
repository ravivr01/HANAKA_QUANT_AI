"""
==========================================================
HQAI Market Data Storage
Release : R-005-001
Author  : Hanaka Quant AI

Bronze Layer Storage Manager

Directory Structure

data/
    bronze/
        NSE/
            yahoo/
                INFY/
                    history.parquet
                    metadata.json
==========================================================
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import polars as pl

from hqai.core.config import config
from hqai.core.logger import log


class MarketDataStorage:
    """
    Bronze Layer Storage Manager.
    """

    ########################################################

    def __init__(
        self,
        exchange: str = "NSE",
        provider: str = "yahoo",
    ):

        self.exchange = exchange.upper()
        self.provider = provider.lower()

        self.root = config.bronze_dir / self.exchange / self.provider

        self.root.mkdir(
            parents=True,
            exist_ok=True,
        )

    ########################################################

    def symbol_path(
        self,
        symbol: str,
    ) -> Path:

        return self.root / symbol.upper()

    ########################################################

    def parquet_file(
        self,
        symbol: str,
    ) -> Path:

        return self.symbol_path(symbol) / "history.parquet"

    ########################################################

    def metadata_file(
        self,
        symbol: str,
    ) -> Path:

        return self.symbol_path(symbol) / "metadata.json"

    ########################################################

    def exists(
        self,
        symbol: str,
    ) -> bool:

        return self.parquet_file(symbol).exists()

    ########################################################

    def save(
        self,
        symbol: str,
        df: pl.DataFrame,
    ) -> None:

        folder = self.symbol_path(symbol)

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.write_parquet(self.parquet_file(symbol))

        metadata = {
            "symbol": symbol.upper(),
            "provider": self.provider,
            "exchange": self.exchange,
            "rows": df.height,
            "columns": df.width,
            "first_date": str(df["DATE"].min()),
            "last_date": str(df["DATE"].max()),
            "downloaded_at": datetime.now().isoformat(),
            "hqai_version": "0.5.0",
        }

        with open(
            self.metadata_file(symbol),
            "w",
            encoding="utf-8",
        ) as fp:

            json.dump(
                metadata,
                fp,
                indent=4,
            )

        log.info(f"Saved {symbol}")

    ########################################################

    def load(
        self,
        symbol: str,
    ) -> pl.DataFrame:

        return pl.read_parquet(self.parquet_file(symbol))

    ########################################################

    def delete(
        self,
        symbol: str,
    ) -> None:

        parquet = self.parquet_file(symbol)

        metadata = self.metadata_file(symbol)

        if parquet.exists():
            parquet.unlink()

        if metadata.exists():
            metadata.unlink()

    ########################################################

    def read_metadata(
        self,
        symbol: str,
    ) -> dict:

        with open(
            self.metadata_file(symbol),
            "r",
            encoding="utf-8",
        ) as fp:

            return json.load(fp)

    ########################################################

    def list_symbols(
        self,
    ) -> list[str]:

        if not self.root.exists():
            return []

        return sorted(path.name for path in self.root.iterdir() if path.is_dir())

    ########################################################

    def summary(
        self,
    ) -> dict:

        return {
            "exchange": self.exchange,
            "provider": self.provider,
            "location": str(self.root),
            "symbols": len(self.list_symbols()),
        }
