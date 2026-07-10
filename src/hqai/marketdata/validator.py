"""
==========================================================
HQAI Market Data Validator
Release : R-005-001
Author  : Hanaka Quant AI

Validates downloaded market data.
Compatible with Polars 1.42+
==========================================================
"""

from __future__ import annotations

import polars as pl

from hqai.core.logger import log


class MarketDataValidator:

    REQUIRED_COLUMNS = [
        "DATE",
        "OPEN",
        "HIGH",
        "LOW",
        "CLOSE",
        "VOLUME",
        "SYMBOL",
    ]

    ########################################################

    def validate_columns(
        self,
        df: pl.DataFrame,
    ) -> None:

        missing = [
            column for column in self.REQUIRED_COLUMNS if column not in df.columns
        ]

        if missing:

            raise ValueError(f"Missing columns: {missing}")

    ########################################################

    def validate_empty(
        self,
        df: pl.DataFrame,
    ) -> None:

        if df.is_empty():

            raise ValueError("Empty DataFrame received.")

    ########################################################

    def validate_duplicates(
        self,
        df: pl.DataFrame,
    ) -> None:

        duplicates = df.select(pl.col("DATE").is_duplicated().sum()).item()

        if duplicates > 0:

            raise ValueError(f"{duplicates} duplicate DATE values found.")

    ########################################################

    def validate_prices(
        self,
        df: pl.DataFrame,
    ) -> None:

        for column in [
            "OPEN",
            "HIGH",
            "LOW",
            "CLOSE",
        ]:

            minimum = df[column].min()

            if minimum is None:

                continue

            if minimum <= 0:

                raise ValueError(f"{column} contains non-positive prices.")

    ########################################################

    def validate_volume(
        self,
        df: pl.DataFrame,
    ) -> None:

        minimum = df["VOLUME"].min()

        if minimum is None:

            return

        if minimum < 0:

            raise ValueError("Negative volume detected.")

    ########################################################

    def validate(
        self,
        df: pl.DataFrame,
    ) -> bool:

        self.validate_empty(df)

        self.validate_columns(df)

        self.validate_duplicates(df)

        self.validate_prices(df)

        self.validate_volume(df)

        log.info("Market data validation successful.")

        return True
