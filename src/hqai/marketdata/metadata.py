"""
==========================================================
HQAI Market Data Metadata
Release : R-005-001
Author  : Hanaka Quant AI

Metadata object for Market Data.
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
    Metadata describing a downloaded dataset.
    """

    symbol: str
    provider: str
    exchange: str
    interval: str
    period: str

    rows: int
    columns: int

    first_date: str
    last_date: str

    downloaded_at: str

    hqai_version: str = "0.5.0"

    ########################################################

    @classmethod
    def create(
        cls,
        symbol: str,
        provider: str,
        exchange: str,
        interval: str,
        period: str,
        rows: int,
        columns: int,
        first_date,
        last_date,
    ):

        return cls(
            symbol=symbol.upper(),
            provider=provider,
            exchange=exchange,
            interval=interval,
            period=period,
            rows=rows,
            columns=columns,
            first_date=str(first_date),
            last_date=str(last_date),
            downloaded_at=datetime.now().isoformat(),
        )

    ########################################################

    def to_dict(self) -> dict:

        return asdict(self)

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
