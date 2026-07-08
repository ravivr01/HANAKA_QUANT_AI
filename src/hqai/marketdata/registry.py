"""
==========================================================
HQAI Market Data Provider Registry
Release : 1.0.3
Module  : Market Data Engine

Registers and manages all Market Data Providers.
==========================================================
"""

from __future__ import annotations

from typing import Type

from hqai.marketdata.base import BaseProvider

__all__ = [
    "ProviderRegistry",
    "registry",
]


class ProviderRegistry:
    """
    Registry for all Market Data Providers.

    Example
    -------
    >>> registry.register("yahoo", YahooProvider)
    >>> Provider = registry.get("yahoo")
    >>> provider = Provider()
    """

    ########################################################
    # Constructor
    ########################################################

    def __init__(self) -> None:

        self._providers: dict[str, Type[BaseProvider]] = {}

    ########################################################
    # Register Provider
    ########################################################

    def register(
        self,
        name: str,
        provider: Type[BaseProvider],
    ) -> None:

        key = name.lower()

        if key in self._providers:

            raise ValueError(f"Provider '{name}' already registered.")

        self._providers[key] = provider

    ########################################################
    # Get Provider
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
    # Exists
    ########################################################

    def exists(
        self,
        name: str,
    ) -> bool:

        return name.lower() in self._providers

    ########################################################
    # List Providers
    ########################################################

    def list(self) -> list[str]:

        return sorted(self._providers.keys())

    ########################################################
    # Count Providers
    ########################################################

    def count(self) -> int:

        return len(self._providers)

    ########################################################
    # Clear Registry (Testing)
    ########################################################

    def clear(self) -> None:

        self._providers.clear()

    ########################################################
    # len(registry)
    ########################################################

    def __len__(self) -> int:

        return len(self._providers)


registry = ProviderRegistry()
