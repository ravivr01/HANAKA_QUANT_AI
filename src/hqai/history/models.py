"""
============================================================
HQAI Historical Data Models
============================================================

Defines the core data structures used by the Historical
Data Engine.

Release : 0.4.0
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class HistoryRecord:
    """
    Represents one OHLCV candle.

    All downstream modules (Indicators, Features,
    Backtesting, ML, Portfolio) will use this model.
    """

    symbol: str

    trading_date: date

    open: float

    high: float

    low: float

    close: float

    volume: int

    adjusted_close: float

    delivery_quantity: int | None = None

    delivery_percentage: float | None = None


@dataclass(slots=True)
class DownloadStatistics:
    """
    Download summary.
    """

    symbol: str

    records: int

    started_at: str

    completed_at: str

    successful: bool

    message: str = ""
