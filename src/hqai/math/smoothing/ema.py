"""
==========================================================
HQAI Exponential Moving Average
==========================================================

Mathematical primitive for exponential smoothing.

Formula

EMA_t = α × Price_t + (1-α) × EMA_(t-1)

where

α = 2 / (period + 1)

Release : M2
Author  : Hanaka Quant AI
"""

from __future__ import annotations

import pandas as pd


def ema(
    series: pd.Series,
    period: int,
    adjust: bool = False,
) -> pd.Series:
    """
    Calculate Exponential Moving Average.

    Parameters
    ----------
    series
        Input Series

    period
        EMA Period

    adjust
        Pandas adjust flag

    Returns
    -------
    pd.Series
    """

    if period <= 0:
        raise ValueError("period must be greater than zero.")

    return series.ewm(
        span=period,
        adjust=adjust,
    ).mean()
