"""
HQAI Feature Exceptions
"""


class FeatureError(Exception):
    pass


class FeatureValidationError(FeatureError):
    pass


class FeatureStorageError(FeatureError):
    pass


class FeatureBuilderError(FeatureError):
    pass