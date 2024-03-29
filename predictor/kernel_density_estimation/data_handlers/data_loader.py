import pathlib
from os import listdir
from os.path import isfile, join

from data_structures.enums.optimizer_name import OptimizerName
from experiments.data_handlers import json_reader


def load_jsons(directory: str, optimizer_name: OptimizerName, p: int):
    fn = pathlib.Path(__file__).parent.parent.parent
    directory = str(fn) + directory + "\\p=" + str(int(p)) + "\\"
    all_file_names = _get_all_file_names(directory)
    relevant_file_names = _get_relevant_file_names(all_file_names, optimizer_name, p)
    jsons_list = []
    for file_name in relevant_file_names:
        json = json_reader.read_from_json(directory, file_name)
        jsons_list.append(json)
    return jsons_list


def _get_all_file_names(directory: str):
    return [file_name for file_name in listdir(directory) if isfile(join(directory, file_name))]


def _get_relevant_file_names(all_file_names_list, optimizer_name: OptimizerName, p: int):
    return [file_name for file_name in all_file_names_list if _is_file_relevant(file_name, optimizer_name, p)]


def _is_file_relevant(file_name, optimizer_name: OptimizerName, p: int):
    return optimizer_name.value in file_name and "p=" + str(p) in file_name
