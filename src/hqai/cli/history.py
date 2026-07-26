"""
==========================================================
HQAI History CLI
==========================================================

History Management Commands

Author  : Ravi Varma
Version : 0.7.4
"""

import typer

from hqai.history.downloader import HistoryDownloader
from hqai.history.updater import HistoryUpdater
from hqai.history.verify import HistoryVerify
from hqai.history.stats import HistoryStats

app = typer.Typer(
    help="History Management Commands"
)

# ==========================================================
# DOWNLOAD
# ==========================================================

@app.command("download")
def download():
    """
    Download complete historical data.
    """

    HistoryDownloader().download_all()


# ==========================================================
# UPDATE
# ==========================================================

@app.command("update")
def update():
    """
    Update historical data by downloading only
    missing daily candles.
    """

    HistoryUpdater().run()


# ==========================================================
# VERIFY
# ==========================================================

@app.command("verify")
def verify():
    """
    Verify downloaded history repository.
    """

    HistoryVerify().verify()


# ==========================================================
# STATISTICS
# ==========================================================

@app.command("stats")
def stats():
    """
    Display history statistics.
    """

    HistoryStats().run()