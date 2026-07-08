"""
==========================================================
HQAI Rolling Sum
==========================================================
"""

from __future__ import annotations

import pandas as pd


def rolling_sum(
    series: pd.Series,
    window: int,
    min_periods: int | None = None,
) -> pd.Series:
    """
    Compute the rolling sum.
    """

    if window <= 0:
        raise ValueError("window must be greater than zero")

    if min_periods is None:
        min_periods = window

    return series.rolling(
        window=window,
        min_periods=min_periods,
    ).sum()
