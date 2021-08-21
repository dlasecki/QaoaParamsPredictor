from sklearn.neighbors import KernelDensity

from kernel_density_estimation.data_handlers.jsons_validator import validate_json_list_not_empty, validate_jsons, \
    _get_model_metadata
from kernel_density_estimation.kde_matrix_builder import build_kde_parameters_matrix
from kernel_density_estimation.kde_model import KdeModel


def train_kde_model(jsons_list, kernel: str, bandwidth: float):
    """Trains a KDE model from data provided as json files."""
    validate_json_list_not_empty(jsons_list)
    if not validate_jsons(jsons_list):
        raise Exception("Provided json files reference different optimization problem and/or graph type.")
    good_params_matrix = build_kde_parameters_matrix(jsons_list)

    kde = KernelDensity(kernel=kernel, bandwidth=bandwidth)
    kde.fit(good_params_matrix)
    return _create_kde_model(jsons_list, kde, kernel, bandwidth)


def _create_kde_model(jsons_list, kde_model, kernel, bandwidth):
    """Constructs a KdeModel object from a KDE model trained and related metadata."""
    problem_name, graph_type, number_of_instances_trained, p = _get_model_metadata(jsons_list)
    return KdeModel(kde_model, kernel, bandwidth, problem_name, graph_type, number_of_instances_trained, p)
