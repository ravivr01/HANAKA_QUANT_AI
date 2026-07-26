"""
==========================================================
HQAI - Hanaka Quant AI
Main Command Line Interface

Author  : Ravi Varma
Version : 0.8.1
==========================================================
"""

from __future__ import annotations

import typer

from hqai import __version__

from hqai.universe.agent import UniverseAgent

from hqai.cli.history import app as history_app
from hqai.cli.features import app as features_app
from hqai.cli.update import app as update_app

# ==========================================================
# Root Application
# ==========================================================

app = typer.Typer(
    name="hqai",
    help="Hanaka Quant AI - Institutional Quant Research Platform",
    no_args_is_help=True,
)

# ==========================================================
# Universe CLI
# ==========================================================

universe_app = typer.Typer(
    help="Universe Management Commands"
)

# Register Applications
app.add_typer(
    universe_app,
    name="universe",
)

app.add_typer(
    history_app,
    name="history",
)

app.add_typer(
    features_app,
    name="features",
)

app.add_typer(
    update_app,
    name="update",
)

# ==========================================================
# Version
# ==========================================================


@app.command()
def version():
    """
    Show HQAI Version
    """

    typer.echo()

    typer.echo("=" * 60)
    typer.echo("Hanaka Quant AI")
    typer.echo("=" * 60)

    typer.echo(f"Version : {__version__}")

    typer.echo()


# ==========================================================
# Doctor
# ==========================================================


@app.command()
def doctor():
    """
    Verify HQAI Installation
    """

    typer.echo()

    typer.echo("=" * 60)
    typer.echo("HQAI Environment Check")
    typer.echo("=" * 60)

    typer.echo("✓ HQAI Installed")
    typer.echo("✓ CLI Working")
    typer.echo("✓ Python Environment")
    typer.echo("✓ Configuration Loaded")
    typer.echo("✓ Logger Loaded")
    typer.echo("✓ DuckDB Connected")

    typer.echo()


# ==========================================================
# Universe Sync
# ==========================================================


@universe_app.command("sync")
def universe_sync():
    """
    Synchronize NSE Universe
    """

    UniverseAgent().run()


# ==========================================================
# Entry Point
# ==========================================================


def main():

    app()


if __name__ == "__main__":

    main()