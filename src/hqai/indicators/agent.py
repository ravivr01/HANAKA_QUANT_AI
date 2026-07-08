"""
==========================================================
HQAI Indicator Agent
==========================================================

Builds technical indicators for all symbols.

Author  : Ravi Varma
Release : 0.9.6
"""

from __future__ import annotations

import pandas as pd
from tqdm import tqdm

from hqai.core.base_agent import BaseAgent
from hqai.core.database import db
from hqai.core.logger import log

from hqai.history.storage import HistoryStorage

from hqai.indicators.index import IndicatorIndex
from hqai.indicators.registry import registry
from hqai.indicators.storage import IndicatorStorage


class IndicatorAgent(BaseAgent):
    """
    HQAI Indicator Engine
    """

    ########################################################

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

            indicator_class = registry.get(name)

            indicator = indicator_class()

            log.info(f"Running {name}")

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

        universe = db.query("""
            SELECT SYMBOL
            FROM universe
            ORDER BY SYMBOL
            """)

        symbols = universe["SYMBOL"].to_list()

        total = len(symbols)

        success = 0

        failed = []

        log.info("=" * 60)
        log.info(f"Building Indicators for {total} symbols")
        log.info("=" * 60)

        for symbol in tqdm(
            symbols,
            desc="Indicators",
        ):

            try:

                self.build(symbol)

                success += 1

            except Exception as ex:

                log.error(f"{symbol} -> {ex}")

                failed.append(symbol)

        log.info("=" * 60)
        log.success(f"Success : {success}")
        log.warning(f"Failed  : {len(failed)}")

        return failed

    ########################################################

    def validate(self):

        raise NotImplementedError("validate() not implemented.")

    ########################################################

    def summary(self):

        return self.index.summary()

    ########################################################

    def clean(self):

        raise NotImplementedError("clean() not implemented.")
