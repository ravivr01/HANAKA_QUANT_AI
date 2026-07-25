from datetime import datetime
import time

from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)

console = Console()


def simulate_download():

    total_symbols = 2496

    progress = Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TextColumn("[green]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
    )

    task = progress.add_task(
        "Downloading NSE History",
        total=total_symbols,
    )

    with Live(progress, refresh_per_second=10):

        for i in range(total_symbols):

            progress.update(task, advance=1)

            time.sleep(0.01)

    console.print()

    console.print(
        Panel.fit(
            f"""
HQAI DAILY UPDATE COMPLETED

Date      : {datetime.now()}

Universe  : {total_symbols}

Downloaded: {total_symbols}

Failed    : 0

Status    : SUCCESS
""",
            title="HQAI",
            border_style="green",
        )
    )


if __name__ == "__main__":

    console.print()

    console.rule("[bold green]HQAI DAILY HISTORY UPDATE")

    simulate_download()