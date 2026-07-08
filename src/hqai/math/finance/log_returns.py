"""
==========================================================
HQAI Log Returns
==========================================================

Formula

Rt = ln(Pt / Pt-1)
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def log_returns(
    close: pd.Series,
) -> pd.Series:
    """
    Calculate logarithmic returns.
    """

    return np.log(close / close.shift(1))
