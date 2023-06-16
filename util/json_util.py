import json

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

def get_nodes(data, keyValuePairs):
    def match_key_value(node, key, value):
        if isinstance(node, dict):
            if key in node and node[key] == value:
                return True
        return False

    def traverse(node):
        matches = []
        if isinstance(node, dict):
            if any(match_key_value(node, k, v) for k, v in keyValuePairs):
                matches.append(node)
            for value in node.values():
                if isinstance(value, (dict, list)):
                    matches.extend(traverse(value))
        elif isinstance(node, list):
            for item in node:
                if isinstance(item, (dict, list)):
                    matches.extend(traverse(item))
        return matches

    result = traverse(data)
    return result