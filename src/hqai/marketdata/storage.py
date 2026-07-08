"""
==========================================================
HQAI Market Data Storage
Release : 1.0.4
Author  : Hanaka Quant AI

Bronze Layer Storage Manager
==========================================================
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime
import json

import polars as pl

from hqai.core.config import config
from hqai.core.logger import log


class MarketDataStorage:
    """
    Bronze Layer Storage.

    data/
        bronze/
            equity/
                NSE/
                    INFY/
                        history.parquet
                        metadata.json
    """

    def __init__(self):

        self.root = config.project_root / "data" / "bronze" / "equity" / "NSE"

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
        provider: str,
    ):

        folder = self.symbol_path(symbol)

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        parquet = self.parquet_file(symbol)

        df.write_parquet(parquet)

        metadata = {
            "symbol": symbol,
            "provider": provider,
            "rows": df.height,
            "columns": df.width,
            "first_date": str(df["DATE"].min()),
            "last_date": str(df["DATE"].max()),
            "updated_at": datetime.now().isoformat(),
            "version": "1.0.0",
        }

        with open(
            self.metadata_file(symbol),
            "w",
        ) as fp:

            json.dump(
                metadata,
                fp,
                indent=4,
            )

        log.info(f"Saved -> {symbol}")

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
    ):

        parquet = self.parquet_file(symbol)

        metadata = self.metadata_file(symbol)

        if parquet.exists():

            parquet.unlink()

        if metadata.exists():

            metadata.unlink()

    ########################################################

    def metadata(
        self,
        symbol: str,
    ) -> dict:

        with open(
            self.metadata_file(symbol),
            "r",
        ) as fp:

            return json.load(fp)

    ########################################################

    def list_symbols(
        self,
    ) -> list[str]:

        return sorted(p.name for p in self.root.iterdir() if p.is_dir())

    ########################################################

    def summary(self):

        return {
            "symbols": len(self.list_symbols()),
            "location": str(self.root),
        }
