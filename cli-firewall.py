import typer
import os
from rich import print as rprint
from dotenv import load_dotenv
import commands.setconfig
import commands.run

load_dotenv()
app=typer.Typer()

appName=os.getenv("appName")
author=os.getenv("author")
version=os.getenv("version")

@app.command("help")
def cmd_help():
    rprint("{}: {} developed by {}".format(appName,version,author))
    rprint("[blue]Available Commands:[/blue]")
    rprint("  help          - Show help message")
    rprint("  version       - Print current version")
    rprint("  setconfig     - Configure the firewall")
    rprint("  run           - Run the firewall")

@app.command("version")
def cmd_version():
    rprint("Version: {}".format(version))

@app.command("setconfig")
def cmd_setconfig():
    commands.setconfig.setconfig()

@app.command("run")
def cmd_run():
    commands.run.run()

if __name__=="__main__":
    app()