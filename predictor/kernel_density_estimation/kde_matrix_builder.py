import numpy as np


def build_kde_parameters_matrix(jsons_list):
    good_params_matrix = []
    for json in jsons_list:
        good_params = json["good_params"]
        good_params_matrix = good_params_matrix + good_params
    print(good_params_matrix)
    return good_params_matrix

