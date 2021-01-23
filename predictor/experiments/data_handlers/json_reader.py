import json


def read_from_json(directory: str, file_name: str):
    path = directory + "/" + file_name
    with open(path) as json_file:
        json_object = json.load(json_file)
    return json_object
