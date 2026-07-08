"""
==========================================================
HQAI Base Agent
==========================================================

Defines the common interface for all HQAI Agents.

Author  : Ravi Varma
Release : 0.9
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Base class for all HQAI Agents.
    """

    @abstractmethod
    def build(self, *args, **kwargs):
        """
        Build one object.
        """
        raise NotImplementedError

    ########################################################

    @abstractmethod
    def sync(self):
        """
        Synchronize all objects.
        """
        raise NotImplementedError

    ########################################################

    @abstractmethod
    def validate(self):
        """
        Validate outputs.
        """
        raise NotImplementedError

    ########################################################

    @abstractmethod
    def summary(self):
        """
        Return summary information.
        """
        raise NotImplementedError

    ########################################################

    @abstractmethod
    def clean(self):
        """
        Remove generated files.
        """
        raise NotImplementedError
