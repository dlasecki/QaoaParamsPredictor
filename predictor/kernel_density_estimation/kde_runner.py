from sklearn.neighbors import KernelDensity

from helpers.enums.OptimizerName import OptimizerName
from kde_matrix_builder import build_kde_parameters_matrix
from kernel_density_estimation.data_handlers import kde_model_serializer
from kernel_density_estimation.data_handlers.data_loader import load_jsons


def train_kde_model(jsons_list, bandwidth: float):
    good_params_matrix = build_kde_parameters_matrix(jsons_list)
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth)
    kde.fit(good_params_matrix)
    return kde


if __name__ == '__main__':
    PATH = "\\experiments\\output\\max_cut\\random"
    SAVE_PATH = "serialized_models"
    p = 1
    bandwidth = 0.2
    jsons_list = load_jsons(PATH, OptimizerName.COBYLA, p)
    kde_model = train_kde_model(jsons_list, bandwidth)
    sample = kde_model.sample()
    print(sample)
    kde_model_serializer.serialize_kde_model(SAVE_PATH, kde_model)
