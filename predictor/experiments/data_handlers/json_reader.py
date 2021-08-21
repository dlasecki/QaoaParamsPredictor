import json


def read_from_json(directory: str, file_name: str):
    """Reads a json file from a given directory."""
    path = directory + "/" + file_name
    with open(path) as json_file:
        json_object = json.load(json_file)
    return json_object
