"""
==========================================================
HQAI Rolling Mean
==========================================================

Mathematical primitive for rolling mean calculations.

Author  : Ravi Varma
Release : M1
"""

from __future__ import annotations

import pandas as pd


def rolling_mean(
    series: pd.Series,
    window: int,
    min_periods: int | None = None,
) -> pd.Series:
    """
    Compute the rolling mean.

    Parameters
    ----------
    series : pd.Series
        Input series.

    window : int
        Rolling window size.

    min_periods : int | None
        Minimum observations required.

    Returns
    -------
    pd.Series
        Rolling mean.
    """

    if window <= 0:
        raise ValueError("window must be greater than zero")

    if min_periods is None:
        min_periods = window

    return series.rolling(
        window=window,
        min_periods=min_periods,
    ).mean()
