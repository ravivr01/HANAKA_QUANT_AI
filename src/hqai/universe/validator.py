"""
============================================================
HQAI Universe Validator
============================================================
Validates and standardizes the NSE Universe.
============================================================
"""

from __future__ import annotations

import pandas as pd

from hqai.core.logger import log


class UniverseValidator:
    """
    Cleans and validates the NSE Universe DataFrame.
    """

    REQUIRED_COLUMNS = [
        "SYMBOL",
        "NAME OF COMPANY",
        "SERIES",
        "DATE OF LISTING",
        "PAID UP VALUE",
        "MARKET LOT",
        "ISIN NUMBER",
        "FACE VALUE",
    ]

    def validate(self, dataframe: pd.DataFrame) -> pd.DataFrame:

        log.info("Validating universe...")

        dataframe = dataframe.copy()

        dataframe.columns = dataframe.columns.str.strip()

        self._check_columns(dataframe)

        dataframe = self._remove_duplicates(dataframe)

        dataframe = self._remove_empty_symbols(dataframe)

        dataframe = self._trim_strings(dataframe)

        dataframe = dataframe.sort_values(by="SYMBOL").reset_index(drop=True)

        log.info(f"Validation Complete : {len(dataframe)} records")

        return dataframe

    ########################################################

    def _check_columns(self, dataframe):

        missing = []

        for column in self.REQUIRED_COLUMNS:

            if column not in dataframe.columns:
                missing.append(column)

        if missing:
            raise ValueError(f"Missing Columns : {missing}")

    ########################################################

    def _remove_duplicates(self, dataframe):

        before = len(dataframe)

        dataframe = dataframe.drop_duplicates(subset=["SYMBOL"])

        after = len(dataframe)

        log.info(f"Removed {before-after} duplicate symbols")

        return dataframe

    ########################################################

    def _remove_empty_symbols(self, dataframe):

        dataframe = dataframe.dropna(subset=["SYMBOL"])

        dataframe = dataframe[dataframe["SYMBOL"].astype(str).str.strip() != ""]

        return dataframe

    ########################################################

    def _trim_strings(self, dataframe):

        object_columns = dataframe.select_dtypes(include="object").columns

        for column in object_columns:

            dataframe[column] = dataframe[column].astype(str).str.strip()

        return dataframe
