import json
import os

def read_json():
    if not os.path.isfile('data/data.json'):
        with open('data/data.json', 'w') as f:
            json.dump([],f)
    with open('data/data.json', 'r') as f:
        data = json.load(f)
    return data

def write_json(data):
    with open('data/data.json','w') as f:
        json.dump(data, f)

def create_folder(path):
    try:
        os.mkdir(path)
        return True
    except FileExistsError:
        return False

def move_file(oldPath,newPath):
    try:
        file = os.path.basename(oldPath)
        newPath = newPath + '/' + file
        os.replace(oldPath,newPath)
        return newPath
    except:
        return False

def exec_file(name):
    data = read_json()
    script = next((x for x in data if x['name'] == name), None)
    if script is None:
        return 'Script does not exist'
    else:
        return os.system(f"pwsh {script['path']}")
