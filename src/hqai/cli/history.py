"""
==========================================================
HQAI History CLI
==========================================================

History Management Commands

Author  : Ravi Varma
Version : 0.7.1
"""

import typer

from hqai.history.downloader import HistoryDownloader
from hqai.history.stats import HistoryStats

app = typer.Typer(
    help="History Management Commands"
)


# ---------------------------------------------------------
# Download
# ---------------------------------------------------------

@app.command("download")
def download():
    """
    Download complete history.
    """

    HistoryDownloader().download_all()


# ---------------------------------------------------------
# Update
# ---------------------------------------------------------

@app.command("update")
def update():
    """
    Update existing history.
    """

    typer.echo("=" * 60)
    typer.echo("HQAI HISTORY UPDATE")
    typer.echo("=" * 60)
    typer.echo()
    typer.echo("History Update - Coming Soon")


# ---------------------------------------------------------
# Verify
# ---------------------------------------------------------

@app.command("verify")
def verify():
    """
    Verify downloaded history.
    """

    typer.echo("=" * 60)
    typer.echo("HQAI HISTORY VERIFY")
    typer.echo("=" * 60)
    typer.echo()
    typer.echo("History Verification - Coming Soon")


# ---------------------------------------------------------
# Statistics
# ---------------------------------------------------------

@app.command("stats")
def stats():
    """
    Display history statistics.
    """

    HistoryStats().run()