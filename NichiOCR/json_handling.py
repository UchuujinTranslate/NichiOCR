import os
import json
from rich.console import Console
from rich.progress import track
from rich.progress import Progress

console = Console()


def load_all_json():
    # Load all JSON files
    #print("Loading scripts...")
    entireScript = {}
    jsonFiles = []

    for filename in os.listdir("scripts"):
        if filename.endswith(".json"):
            jsonFiles.append(filename)

    with Progress() as progress:
        task = progress.add_task("Loading scripts...", total=len(jsonFiles))
        for file in jsonFiles:
            with open(("scripts/" + file), 'r', encoding='utf-8') as f:
                progress.update(task, description=f"Loading script {file}", advance=1)
                data = json.load(f)
                #print(data)
                scriptName = file.replace('.json','')
                entireScript[scriptName] = data
                
                #print(file + " loaded")

    console.log(f"All scripts loaded!")
    return entireScript