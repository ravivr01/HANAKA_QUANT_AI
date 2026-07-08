"""
==========================================================
HQAI Simple Returns
==========================================================

Formula

Rt = (Pt / Pt-1) - 1
"""

from __future__ import annotations

import pandas as pd


def simple_returns(
    close: pd.Series,
) -> pd.Series:
    """
    Calculate simple percentage returns.

    Parameters
    ----------
    close
        Closing price series.

    Returns
    -------
    pd.Series
    """

    return close.pct_change()
