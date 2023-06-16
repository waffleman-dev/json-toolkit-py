import json

def get_load(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)