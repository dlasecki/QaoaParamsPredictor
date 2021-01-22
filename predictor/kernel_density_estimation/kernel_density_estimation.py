import numpy as np
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

from experiments.json_reader import read_from_json


def create_parameters_matrix(jsons_list):
    rows = len(jsons_list)
    cols = len(jsons_list[0])
    good_params_matrix = np.empty(rows, cols)
    for json in jsons_list:
        good_params = json["good_params"]
        np.append(good_params_matrix, good_params)
    return good_params_matrix


json1 = read_from_json("predictor/experiments/output/", "MaxCutRandom0p=1.json")
json2 = read_from_json("predictor/experiments/output/", "MaxCutRandom1p=1.json")

jsons_list = [json1, json2]
good_params_matrix = create_parameters_matrix(jsons_list)

kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(good_params_matrix)
