"""
==========================================================
HQAI Indicator Validator
==========================================================

Validates historical OHLCV data before indicator calculation.

Release : 0.8
Author  : Hanaka Quant AI
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from hqai.indicators.exceptions import IndicatorValidationError


class IndicatorValidator:
    """
    Validates historical market data.
    """

    REQUIRED_COLUMNS = [
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    ]

    ########################################################

    def validate(
        self,
        df: pd.DataFrame,
    ) -> None:

        self._validate_empty(df)
        self._validate_columns(df)
        self._validate_duplicates(df)
        self._validate_missing(df)
        self._validate_infinite(df)
        self._validate_dates(df)
        self._validate_prices(df)
        self._validate_volume(df)

    ########################################################

    def _validate_empty(
        self,
        df: pd.DataFrame,
    ):

        if df.empty:

            raise IndicatorValidationError("Input DataFrame is empty.")

    ########################################################

    def _validate_columns(
        self,
        df: pd.DataFrame,
    ):

        missing = [c for c in self.REQUIRED_COLUMNS if c not in df.columns]

        if missing:

            raise IndicatorValidationError(f"Missing columns: {missing}")

    ########################################################

    def _validate_duplicates(
        self,
        df: pd.DataFrame,
    ):

        if df["Date"].duplicated().any():

            raise IndicatorValidationError("Duplicate dates detected.")

    ########################################################

    def _validate_missing(
        self,
        df: pd.DataFrame,
    ):

        if df[self.REQUIRED_COLUMNS].isna().any().any():

            raise IndicatorValidationError("Missing values detected.")

    ########################################################

    def _validate_infinite(
        self,
        df: pd.DataFrame,
    ):

        numeric = df.select_dtypes(include=[np.number])

        if np.isinf(numeric.to_numpy()).any():

            raise IndicatorValidationError("Infinite values detected.")

    ########################################################

    def _validate_dates(
        self,
        df: pd.DataFrame,
    ):

        if not df["Date"].is_monotonic_increasing:

            raise IndicatorValidationError("Dates are not sorted.")

    ########################################################

    def _validate_prices(
        self,
        df: pd.DataFrame,
    ):

        if (df["High"] < df["Low"]).any():

            raise IndicatorValidationError("High is less than Low.")

        if (
            (df["Open"] < 0) | (df["High"] < 0) | (df["Low"] < 0) | (df["Close"] < 0)
        ).any():

            raise IndicatorValidationError("Negative prices detected.")

    ########################################################

    def _validate_volume(
        self,
        df: pd.DataFrame,
    ):

        if (df["Volume"] < 0).any():

            raise IndicatorValidationError("Negative volume detected.")
