"""
HQAI Progress Manager
"""

from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)

console = Console()


class ProgressManager:

    def __init__(self):

        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[cyan]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
        )

    def __enter__(self):

        self.progress.start()

        return self.progress

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.progress.stop()
