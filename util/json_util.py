import json
import re

def serialize(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
def deserliaze(data):
    return json.dumps(data)

def strip_by_keys(data, keys):
    if isinstance(data, dict):
        return {k: strip_by_keys(v, keys) for k, v in data.items() if k in keys or isinstance(v, (dict, list)) and strip_by_keys(v, keys)}
    elif isinstance(data, list):
        return [strip_by_keys(item, keys) for item in data]
    else:
        return data





