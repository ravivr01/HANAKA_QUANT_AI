"""
==========================================================
HQAI Market Data Metadata
Release : 1.0.6
Module  : Market Data Engine
Author  : Hanaka Quant AI

Metadata Manager for Bronze Layer datasets.
==========================================================
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class MarketDataMetadata:
    """
    Metadata associated with a Bronze Layer dataset.
    """

    symbol: str

    exchange: str

    provider: str

    rows: int

    columns: int

    first_date: str

    last_date: str

    updated_at: str

    version: str = "1.0.0"

    status: str = "SUCCESS"

    ########################################################
    # Convert to Dictionary
    ########################################################

    def to_dict(self) -> dict:

        return asdict(self)

    ########################################################
    # Save Metadata
    ########################################################

    def save(
        self,
        filename: Path,
    ) -> None:

        filename.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as fp:

            json.dump(
                self.to_dict(),
                fp,
                indent=4,
            )

    ########################################################
    # Load Metadata
    ########################################################

    @classmethod
    def load(
        cls,
        filename: Path,
    ):

        with open(
            filename,
            "r",
            encoding="utf-8",
        ) as fp:

            data = json.load(fp)

        return cls(**data)

    ########################################################
    # Factory Method
    ########################################################

    @classmethod
    def create(
        cls,
        symbol: str,
        provider: str,
        rows: int,
        columns: int,
        first_date,
        last_date,
        exchange: str = "NSE",
    ):

        return cls(
            symbol=symbol.upper(),
            exchange=exchange,
            provider=provider,
            rows=rows,
            columns=columns,
            first_date=str(first_date),
            last_date=str(last_date),
            updated_at=datetime.now().isoformat(),
            version="1.0.0",
            status="SUCCESS",
        )

    ########################################################
    # Pretty Representation
    ########################################################

    def __str__(self):

        return (
            f"{self.symbol} | "
            f"{self.rows} rows | "
            f"{self.first_date} -> {self.last_date}"
        )
