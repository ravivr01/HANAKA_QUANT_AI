"""
==========================================================
HQAI Simple Moving Average
==========================================================

Trend Indicator

Formula

SMA = Sum(Close) / Period

Uses

hqai.math.rolling.rolling_mean()

Author  : Ravi Varma
Release : F1
"""

from __future__ import annotations

import pandas as pd

from hqai.indicators.base import BaseIndicator
from hqai.indicators.metadata import IndicatorMetadata
from hqai.math.rolling import rolling_mean


class SMA(BaseIndicator):
    """
    Simple Moving Average Indicator.
    """

    def __init__(
        self,
        period: int = 20,
    ):

        super().__init__()

        self.period = period

    ######################################################

    @property
    def metadata(self) -> IndicatorMetadata:

        return IndicatorMetadata(
            name=f"SMA{self.period}",
            category="Trend",
            version="1.0",
            description="Simple Moving Average",
            formula="Rolling Mean",
            reference="John Murphy",
            author="HQAI",
            required_columns=["Close"],
            output_columns=[
                f"SMA{self.period}"
            ],
            parameters={
                "period": self.period
            },
            warmup_period=self.period,
            complexity="O(n)",
            supports_incremental=True,
        )

    ######################################################

    def calculate(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        result = df.copy()

        result[f"SMA{self.period}"] = rolling_mean(
            result["Close"],
            window=self.period,
        )

        return result