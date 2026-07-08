"""
==========================================================
HQAI Market Data Metadata
Release : 1.0.6
Author  : Hanaka Quant AI

Metadata model for Bronze Layer datasets.
==========================================================
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime
import json
from pathlib import Path


@dataclass
class MarketDataMetadata:
    """
    Metadata associated with a Bronze market data dataset.
    """

    symbol: str
    exchange: str
    provider: str

    rows: int

    first_date: str
    last_date: str

    updated_at: str

    version: str = "1.0.0"

    status: str = "SUCCESS"

    ########################################################

    def to_dict(self) -> dict:

        return asdict(self)

    ########################################################

    def save(
        self,
        filename: Path,
    ):

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

    @classmethod
    def create(
        cls,
        symbol: str,
        provider: str,
        rows: int,
        first_date,
        last_date,
        exchange: str = "NSE",
    ):

        return cls(
            symbol=symbol,
            exchange=exchange,
            provider=provider,
            rows=rows,
            first_date=str(first_date),
            last_date=str(last_date),
            updated_at=datetime.now().isoformat(),
        )
