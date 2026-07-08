"""
==========================================================
HQAI Indicator Exceptions
==========================================================

Custom exception hierarchy for the Indicator Engine.

Release : 0.8
Author  : Hanaka Quant AI

Every Indicator Engine module must raise these exceptions
instead of generic Python exceptions.

Hierarchy
---------
IndicatorError
│
├── IndicatorValidationError
├── IndicatorCalculationError
├── IndicatorStorageError
├── IndicatorRegistryError
├── IndicatorMetadataError
└── IndicatorConfigurationError
"""

from __future__ import annotations


class IndicatorError(Exception):
    """
    Base exception for all Indicator Engine errors.
    """

    pass


############################################################


class IndicatorValidationError(IndicatorError):
    """
    Raised when the input data fails validation.

    Examples
    --------
    - Missing required columns
    - Duplicate dates
    - NaN values
    - Negative volume
    """

    pass


############################################################


class IndicatorCalculationError(IndicatorError):
    """
    Raised when an indicator calculation fails.

    Examples
    --------
    - Division by zero
    - Invalid rolling window
    - Mathematical overflow
    """

    pass


############################################################


class IndicatorStorageError(IndicatorError):
    """
    Raised when indicator storage fails.

    Examples
    --------
    - Unable to save parquet
    - DuckDB registration failed
    """

    pass


############################################################


class IndicatorRegistryError(IndicatorError):
    """
    Raised when indicator registration fails.

    Examples
    --------
    - Duplicate indicator name
    - Unknown indicator
    """

    pass


############################################################


class IndicatorMetadataError(IndicatorError):
    """
    Raised when indicator metadata is invalid.

    Examples
    --------
    - Missing version
    - Missing parameters
    - Invalid metadata schema
    """

    pass


############################################################


class IndicatorConfigurationError(IndicatorError):
    """
    Raised when configuration is invalid.

    Examples
    --------
    - Invalid worker count
    - Unsupported storage mode
    """

    pass