"""
==========================================================
HQAI Wilder Smoothing
==========================================================

Used by

ATR

ADX

RSI

Release : M2
Author  : Hanaka Quant AI
"""

from __future__ import annotations

import pandas as pd


def wilder(
    series: pd.Series,
    period: int,
) -> pd.Series:
    """
    Wilder's exponential smoothing.

    Parameters
    ----------
    series
        Input Series

    period
        Smoothing Period

    Returns
    -------
    pd.Series
    """

    if period <= 0:
        raise ValueError("period must be greater than zero.")

    return series.ewm(
        alpha=1 / period,
        adjust=False,
    ).mean()
