"""
==========================================================
HQAI Indicator Registry
==========================================================

Central registry for Indicator Engine.

Release : 0.8
Author  : Hanaka Quant AI
"""

from __future__ import annotations

from typing import Type

from hqai.indicators.base import BaseIndicator
from hqai.indicators.exceptions import IndicatorRegistryError


class IndicatorRegistry:
    """
    Central registry of all HQAI indicators.
    """

    ########################################################

    def __init__(self):

        self._registry: dict[str, Type[BaseIndicator]] = {}

    ########################################################

    def register(
        self,
        indicator: Type[BaseIndicator],
    ):

        name = indicator().metadata.name.upper()

        if name in self._registry:

            raise IndicatorRegistryError(f"Indicator '{name}' already registered.")

        self._registry[name] = indicator

    ########################################################

    def unregister(
        self,
        name: str,
    ):

        self._registry.pop(name.upper(), None)

    ########################################################

    def get(
        self,
        name: str,
    ) -> Type[BaseIndicator]:

        key = name.upper()

        if key not in self._registry:

            raise IndicatorRegistryError(f"Unknown indicator : {name}")

        return self._registry[key]

    ########################################################

    def create(
        self,
        name: str,
    ) -> BaseIndicator:

        return self.get(name)()

    ########################################################

    def list(self) -> list[str]:

        return sorted(self._registry.keys())

    ########################################################

    def count(self) -> int:

        return len(self._registry)

    ########################################################

    def clear(self):

        self._registry.clear()


registry = IndicatorRegistry()
