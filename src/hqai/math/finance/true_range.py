"""
==========================================================
HQAI True Range
==========================================================

TR = max(

High-Low,

abs(High-PreviousClose),

abs(Low-PreviousClose)

)

Used by

ATR

ADX

SuperTrend
"""

from __future__ import annotations

import pandas as pd


def true_range(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """
    Calculate True Range.
    """

    previous_close = close.shift(1)

    ranges = pd.concat(
        [
            high - low,
            (high - previous_close).abs(),
            (low - previous_close).abs(),
        ],
        axis=1,
    )

    return ranges.max(axis=1)
