"""
==========================================================
HQAI Market Data Provider Registry
==========================================================

Registers all Market Data Providers.

Author  : Ravi Varma
Release : 1.0.2
"""

from __future__ import annotations

from typing import Type

from hqai.marketdata.base import BaseProvider


class ProviderRegistry:
    """
    Registry of Market Data Providers.
    """

    def __init__(self):

        self._providers: dict[str, Type[BaseProvider]] = {}

    ########################################################

    def register(
        self,
        name: str,
        provider: Type[BaseProvider],
    ):

        key = name.lower()

        if key in self._providers:

            raise ValueError(f"Provider '{name}' already registered.")

        self._providers[key] = provider

    ########################################################

    def get(
        self,
        name: str,
    ) -> Type[BaseProvider]:

        key = name.lower()

        if key not in self._providers:

            raise ValueError(f"Unknown provider '{name}'.")

        return self._providers[key]

    ########################################################

    def exists(
        self,
        name: str,
    ) -> bool:

        return name.lower() in self._providers

    ########################################################

    def list(self) -> list[str]:

        return sorted(self._providers.keys())

    ########################################################

    def count(self) -> int:

        return len(self._providers)


registry = ProviderRegistry()
