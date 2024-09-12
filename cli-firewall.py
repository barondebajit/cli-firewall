import typer
from rich import print as rprint
import commands
import commands.setconfig

app=typer.Typer()

@app.command("help",help="View usage")
def help():
    rprint("[blue]Commands:[blue]")

@app.command("setconfig",help="Set configuration settings")
def help():
    commands.setconfig()