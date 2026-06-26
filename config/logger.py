cat > config/logger.py << 'EOF'
from loguru import logger
from pathlib import Path
import sys

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>"
)

logger.add(
    LOG_DIR / "hanaka_quant.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="INFO"
)
EOF