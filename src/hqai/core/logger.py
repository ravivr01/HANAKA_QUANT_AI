"""
HQAI Logger
"""

from loguru import logger

from hqai.core.config import config

# Create log directory if it doesn't exist
config.log_dir.mkdir(parents=True, exist_ok=True)

LOG_FILE = config.log_dir / "hqai.log"

# Remove default logger
logger.remove()

# Console logger
logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    colorize=True,
)

# File logger
logger.add(
    LOG_FILE,
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="DEBUG",
)

log = logger
