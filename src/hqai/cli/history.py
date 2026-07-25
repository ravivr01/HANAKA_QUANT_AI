"""
HQAI History CLI
"""

import typer

from hqai.history.downloader import HistoryDownloader

app = typer.Typer(help="History Management Commands")


@app.command("download")
def download():
    """
    Download complete history.
    """

    HistoryDownloader().download_all()


@app.command("update")
def update():
    """
    Update missing history.
    """

    typer.echo("History Update - Coming Soon")


@app.command("verify")
def verify():
    """
    Verify downloaded history.
    """

    typer.echo("History Verification - Coming Soon")


@app.command("stats")
def stats():
    """
    History statistics.
    """

    typer.echo("History Statistics - Coming Soon")