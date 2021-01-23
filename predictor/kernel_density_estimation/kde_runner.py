from sklearn.neighbors import KernelDensity

from helpers.enums.OptimizerName import OptimizerName
from kde_matrix_builder import build_kde_parameters_matrix
from kernel_density_estimation.data_handlers.data_loader import load_jsons

if __name__ == '__main__':
    PATH = "/experiments/output/max_cut/random"
    p = 1
    jsons_list = load_jsons(PATH, OptimizerName.COBYLA, p)
    good_params_matrix = build_kde_parameters_matrix(jsons_list)
    kde = KernelDensity(kernel='gaussian', bandwidth=0.2)
    kde.fit(good_params_matrix)
    sample = kde.sample()
    print(sample)

