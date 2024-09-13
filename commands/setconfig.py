import os
import sys
import json
from rich import print as rprint

def setconfig():
    '''Old configuration management'''
    pwd=os.getcwd()
    if os.path.isdir(os.path.join(pwd,"config")):
        rprint("[green]Config directory exists. Looking for pre-existing config file.[green]")
        if os.path.isfile(os.path.join(pwd,"config/config.json")):
            rprint("[yellow]An existing config file found. Update? (Y/N): [yellow]",end="")
            choice=input()
            if choice in ["Y","y","Yes","yes"]:
                print("[blue]Choosing to update configuration settings.[blue]")
                try:
                    with open('config/config.json', 'r') as file:
                        config=json.load(file)
                except:
                    rprint("[red]Empty or invalid json file.[red]")
                    config={}
            else:
                rprint("[blue]Exiting.[blue]")
                sys.exit(0)
        else:
            rprint("[red]Config file not found. Creating new configuration settings.[red]")
            config={}
    else:
        rprint("[blue]Config directory not found. Creating config directory.[blue]")
        os.makedirs(os.path.join(pwd,"config"))
        config={}

    '''New configuration menu'''
    rprint("[blue]Setting new configuration.[blue]")

    if "BannedIP" in config.keys():
        oldresult=list(config["BannedIP"])
    else:
        oldresult=[]
    rprint("Enter the IPs you want to filter out.")
    rprint("[blue]Current list (will be overwritten): {}[blue]".format(oldresult))
    rprint("Enter E to stop")
    newresult=[]
    while True:
        ip=input("")
        if ip=="E":
            break
        newresult.append(ip)
    rprint("[yellow]Update value? (Y/N): [yellow]",end="")
    choice=input()
    if choice in ["Y","y","Yes","yes"]:
        config["BannedIP"]=newresult

    if "BannedPorts" in config.keys():
        oldresult=list(config["BannedPorts"])
    else:
        oldresult=[]
    rprint("Enter the ports you want to filter out.")
    rprint("[blue]Current list (will be overwritten): {}[blue]".format(oldresult))
    rprint("Enter E to stop")
    newresult=[]
    while True:
        port=input("")
        if port=="E":
            break
        newresult.append(ip)
    rprint("[yellow]Update value? (Y/N): [yellow]",end="")
    choice=input()
    if choice in ["Y","y","Yes","yes"]:
        config["BannedPorts"]=newresult

    '''Writing final configuration'''
    jsondict=json.dumps(config, indent=4)
    try:
        with open("config/config.json","w") as file:
            file.write(jsondict)
    except:
        rprint("[red]Error writing file.[red]")