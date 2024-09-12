import os
import json
from rich import print as rprint

def setconfig():
    pwd=os.getcwd()
    if os.path.isdir(os.path.join(pwd,"config")):
        rprint("[green]Config directory exists. Looking for pre-existing config file.[green]")
        if os.path.isfile(os.path.join(pwd,"config/config.json")):
            rprint("[yellow]An existing config file found. Update? (Y/N): [yellow]",end="")
            choice=input()
            if choice in ["Y","y","Yes","yes"]:
                print("Choosing to update configuration settings.")
                try:
                    with open('config/config.json', 'r') as file:
                        config=json.load(file)
                except:
                    rprint("[red]Empty json file.[red]")
                    config={}
        else:
            rprint("[red]Config file not found. Creating new configuration settings.[red]")
            config={}
    else:
        rprint("[blue]Config directory not found. Creating config directory.[blue]")
        os.makedirs(os.path.join(pwd,"config"))
        config={}

setconfig()