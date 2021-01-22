import numpy as np
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

from experiments import json_reader
from experiments.json_reader import read_from_json
from helpers.enums.OptimizerName import OptimizerName
from helpers.enums.ProblemName import ProblemName


def create_parameters_matrix(jsons_list):
    rows = len(jsons_list)
    cols = len(jsons_list[0])
    good_params_matrix = np.empty(rows, cols)
    for json in jsons_list:
        good_params = json["good_params"]
        np.append(good_params_matrix, good_params)
    return good_params_matrix


def load_jsons(file_path: str, problem_name: ProblemName, optimizer_name: OptimizerName, p: int):
    file_name = ""
    jsons_list = []
    if problem_name.value in file_name and optimizer_name.value in file_name and "p=" + str(p) in file_name:
        json = json_reader.read_from_json(file_path, file_name)
        jsons_list.append(json)
    return jsons_list


if __name__ == '__main__':
    PATH = "predictor/experiments/output/"
    p = 1
    jsons_list = load_jsons(PATH, ProblemName.MAX_CUT, OptimizerName.COBYLA, p)
    good_params_matrix = create_parameters_matrix(jsons_list)

    kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(good_params_matrix)
