"""
==========================================================
HQAI Base Indicator
==========================================================

Abstract base class for every HQAI indicator.

Release : 0.8
Author  : Hanaka Quant AI
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from time import perf_counter

import pandas as pd

from hqai.core.logger import log
from hqai.indicators.metadata import IndicatorMetadata
from hqai.indicators.exceptions import (
    IndicatorCalculationError,
    IndicatorValidationError,
)


class BaseIndicator(ABC):
    """
    Base class for all HQAI indicators.
    """

    ########################################################

    def __init__(self):

        self.created = datetime.utcnow()

    ########################################################

    @property
    @abstractmethod
    def metadata(self) -> IndicatorMetadata:
        """
        Indicator metadata.
        """

    ########################################################

    @abstractmethod
    def calculate(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Calculate indicator.
        """

    ########################################################

    def required_columns(self) -> list[str]:

        return self.metadata.required_columns

    ########################################################

    def output_columns(self) -> list[str]:

        return self.metadata.output_columns

    ########################################################

    def validate(
        self,
        df: pd.DataFrame,
    ):

        missing = [c for c in self.required_columns() if c not in df.columns]

        if missing:

            raise IndicatorValidationError(f"Missing columns : {missing}")

        if df.empty:

            raise IndicatorValidationError("Input DataFrame is empty.")

    ########################################################

    def run(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        self.validate(df)

        start = perf_counter()

        try:

            result = self.calculate(df)

        except Exception as ex:

            raise IndicatorCalculationError(str(ex)) from ex

        elapsed = perf_counter() - start

        log.info(f"{self.metadata.name} " f"completed in " f"{elapsed:.4f} sec")

        return result

    ########################################################

    def summary(self) -> dict:

        return self.metadata.summary()
