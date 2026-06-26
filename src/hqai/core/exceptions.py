"""
HQAI Custom Exceptions
"""


class HQAIError(Exception):
    """Base exception for HQAI."""

    pass


class ConfigurationError(HQAIError):
    """Configuration related errors."""

    pass


class DatabaseError(HQAIError):
    """Database related errors."""

    pass


class DownloaderError(HQAIError):
    """Download related errors."""

    pass


class ValidationError(HQAIError):
    """Validation related errors."""

    pass


class DataNotFoundError(HQAIError):
    """Raised when requested data is unavailable."""

    pass


class ModelError(HQAIError):
    """Machine Learning related errors."""

    pass


class PortfolioError(HQAIError):
    """Portfolio related errors."""

    pass
