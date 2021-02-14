import os
import json

def load_all_json():
    # Load all JSON files
    print("Loading scripts...")
    entireScript = {}

    for filename in os.listdir("scripts"):
        if filename.endswith(".json"):
            with open(("scripts/" + filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                #print(data)
                scriptName = filename.replace('.json','')
                entireScript[scriptName] = data
                print(filename + " loaded")
    print("Finished dict")

    return entireScript