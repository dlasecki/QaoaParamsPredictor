def build_kde_parameters_matrix(jsons_list):
    good_params_matrix = []
    for json in jsons_list:
        good_params = json["good_params"]
        good_params_matrix = good_params_matrix + good_params
    return good_params_matrix

