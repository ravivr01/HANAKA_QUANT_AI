"""
==========================================================
HQAI Market Data Validator
Release : 1.0.5
Module  : Market Data Engine
Author  : Hanaka Quant AI

Validates OHLCV datasets before storing in Bronze Layer.
==========================================================
"""

from __future__ import annotations

import polars as pl

from hqai.core.logger import log


class MarketDataValidator:
    """
    Validates market data before storage.
    """

    REQUIRED_COLUMNS = [
        "SYMBOL",
        "DATE",
        "OPEN",
        "HIGH",
        "LOW",
        "CLOSE",
        "VOLUME",
    ]

    ########################################################
    # Validate Row Count
    ########################################################

    def validate_rows(
        self,
        df: pl.DataFrame,
    ) -> bool:

        if df.height == 0:
            raise ValueError("Dataset is empty.")

        return True

    ########################################################
    # Validate Required Columns
    ########################################################

    def validate_columns(
        self,
        df: pl.DataFrame,
    ) -> bool:

        missing = [
            column for column in self.REQUIRED_COLUMNS if column not in df.columns
        ]

        if missing:
            raise ValueError(f"Missing columns: {missing}")

        return True

    ########################################################
    # Validate Duplicate Dates
    ########################################################

    def validate_duplicates(
        self,
        df: pl.DataFrame,
    ) -> bool:

        duplicates = df["DATE"].is_duplicated().sum()

        if duplicates > 0:
            raise ValueError(f"{duplicates} duplicate DATE values found.")

        return True

    ########################################################
    # Validate Prices
    ########################################################

    def validate_prices(
        self,
        df: pl.DataFrame,
    ) -> bool:

        for column in [
            "OPEN",
            "HIGH",
            "LOW",
            "CLOSE",
        ]:

            if (df[column] <= 0).any():

                raise ValueError(f"{column} contains invalid values.")

        return True

    ########################################################
    # Validate Volume
    ########################################################

    def validate_volume(
        self,
        df: pl.DataFrame,
    ) -> bool:

        if (df["VOLUME"] < 0).any():

            raise ValueError("Negative volume detected.")

        return True

    ########################################################
    # Validate Date Order
    ########################################################

    def validate_dates(
        self,
        df: pl.DataFrame,
    ) -> bool:

        if not df["DATE"].is_sorted():

            raise ValueError("DATE column is not sorted.")

        return True

    ########################################################
    # Validate NULL Values
    ########################################################

    def validate_nulls(
        self,
        df: pl.DataFrame,
    ) -> bool:

        total_nulls = df.null_count().to_numpy().sum()

        if total_nulls > 0:

            raise ValueError(f"{total_nulls} NULL values detected.")

        return True

    ########################################################
    # Validate Entire Dataset
    ########################################################

    def validate(
        self,
        df: pl.DataFrame,
    ) -> bool:

        self.validate_rows(df)

        self.validate_columns(df)

        self.validate_duplicates(df)

        self.validate_prices(df)

        self.validate_volume(df)

        self.validate_dates(df)

        self.validate_nulls(df)

        log.info("Market data validation passed.")

        return True
