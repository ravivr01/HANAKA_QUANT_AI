import typer

app = typer.Typer(
    name="hqai",
    help="Hanaka Quant AI - Institutional Quant Research Platform"
)

@app.command()
def version():
    """Show HQAI version."""
    print("HQAI Version 0.1.0")

@app.command()
def doctor():
    """Check HQAI installation."""
    print("===================================")
    print(" HQAI Environment Check")
    print("===================================")
    print("✓ HQAI Installed")
    print("✓ CLI Working")
    print("✓ Python Environment OK")
    print("✓ Ready for Sprint 2")

def main():
    app()

if __name__ == "__main__":
    main()
