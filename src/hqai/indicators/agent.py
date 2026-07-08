"""
==========================================================
HQAI Indicator Agent
==========================================================

Builds indicator datasets from Bronze History.

Author  : Ravi Varma
Release : 0.9.5
"""

from __future__ import annotations

import pandas as pd

from hqai.core.base_agent import BaseAgent
from hqai.core.logger import log
from hqai.history.storage import HistoryStorage
from hqai.indicators.index import IndicatorIndex
from hqai.indicators.registry import registry
from hqai.indicators.storage import IndicatorStorage


class IndicatorAgent(BaseAgent):
    """
    Builds indicator datasets.
    """

    def __init__(self):

        self.history = HistoryStorage()

        self.storage = IndicatorStorage()

        self.index = IndicatorIndex()

    ########################################################

    def build(
        self,
        symbol: str,
    ) -> pd.DataFrame:

        log.info(f"Building indicators -> {symbol}")

        history = self.history.load(symbol)

        df = history.to_pandas()

        for name in registry.list():

            log.info(f"Running {name}")

            indicator = registry.get(name)()

            df = indicator.run(df)

        self.storage.save(
            df,
            symbol,
        )

        self.storage.register(
            symbol,
        )

        indicator_columns = len(df.columns) - 6

        self.index.update(
            symbol=symbol,
            df=history,
            indicators=indicator_columns,
        )

        log.success(f"Finished -> {symbol}")

        return df

    ########################################################

    def sync(self):

        raise NotImplementedError

    ########################################################

    def validate(self):

        raise NotImplementedError

    ########################################################

    def summary(self):

        return self.index.summary()

    ########################################################

    def clean(self):

        raise NotImplementedError