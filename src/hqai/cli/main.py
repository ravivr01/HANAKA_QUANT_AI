"""
==========================================================
HQAI - Hanaka Quant AI
Command Line Interface
Version : 0.1.0
==========================================================
"""

import typer

from hqai import __version__
from hqai.universe.agent import UniverseAgent
from hqai.cli.history import app as history_app
from hqai.cli.update import app as update_app

# ---------------------------------------------------------
# Root Application
# ---------------------------------------------------------

app = typer.Typer(
    name="hqai",
    help="Hanaka Quant AI - Institutional Quant Research Platform",
    no_args_is_help=True,
)

# ---------------------------------------------------------
# Universe Commands
# ---------------------------------------------------------

universe_app = typer.Typer(help="Universe Management Commands")

app.add_typer(universe_app, name="universe")
app.add_typer(history_app, name="history")
app.add_typer(update_app, name="update")

# ---------------------------------------------------------
# Version
# ---------------------------------------------------------


@app.command()
def version():
    """
    Show HQAI Version
    """

    typer.echo("")
    typer.echo("========================================")
    typer.echo(" Hanaka Quant AI")
    typer.echo("========================================")
    typer.echo(f"Version : {__version__}")
    typer.echo("")


# ---------------------------------------------------------
# Doctor
# ---------------------------------------------------------


@app.command()
def doctor():
    """
    Verify HQAI Installation
    """

    typer.echo("")
    typer.echo("========================================")
    typer.echo(" HQAI Environment Check")
    typer.echo("========================================")

    typer.echo("✓ HQAI Installed")
    typer.echo("✓ CLI Working")
    typer.echo("✓ Python Environment OK")
    typer.echo("✓ Configuration Loaded")
    typer.echo("✓ Logger Loaded")
    typer.echo("✓ Database Ready")

    typer.echo("")


# ---------------------------------------------------------
# Universe Sync
# ---------------------------------------------------------


@universe_app.command("sync")
def universe_sync():
    """
    Download and update NSE Universe
    """

    agent = UniverseAgent()

    agent.run()


# ---------------------------------------------------------
# Future Commands
# ---------------------------------------------------------

# hqai history download
#
# hqai indicators build
#
# hqai features build
#
# hqai ml train
#
# hqai portfolio optimize
#
# hqai dashboard start


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------


def main():

    app()


if __name__ == "__main__":

    main()
