import typer
from rich import print as rprint
import commands.setconfig

app = typer.Typer()

@app.command("help")
def show_help():
    rprint("[blue]Available Commands:[/blue]")
    rprint("  help          - Show help message")
    rprint("  setconfig     - Run the setconfig command")

@app.command("setconfig")
def run_setconfig():
    commands.setconfig.setconfig()

if __name__ == "__main__":
    app()