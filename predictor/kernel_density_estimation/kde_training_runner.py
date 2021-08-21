from data_structures.enums.kernel import Kernel
from data_structures.enums.optimizer_name import OptimizerName
from kernel_density_estimation.data_handlers import kde_model_serializer
from kernel_density_estimation.data_handlers.data_loader import load_jsons
from kernel_density_estimation.kde_model_trainer import train_kde_model

"""Runs KDE models training for given parameters."""

if __name__ == '__main__':
    SAVE_PATH = "serialized_models"
    kernel = [Kernel.GAUSSIAN, Kernel.EPANECHNIKOV, Kernel.TOPHAT, Kernel.LINEAR, Kernel.COSINE, Kernel.EXPONENTIAL]
    p = [1, 2, 3, 4]
    bandwidth = [0.2, 0.4, 0.6, 0.8]
    problems = ["max_cut", "vertex_cover", "stable_set", "partition"]
    graph_type_names = ["erdos_renyi", "barbell", "caveman", "ladder"]

    for problem in problems:
        for graph_type_name in graph_type_names:
            for p_param in p:
                print(problem + "_" + graph_type_name + "_" + str(p_param))
                for band in bandwidth:
                    PATH = "\\experiments\\workflow_results_converted\\" + problem + "\\" + graph_type_name
                    jsons_list = load_jsons(PATH, OptimizerName.LBFGS, p_param)
                    kde_model = train_kde_model(jsons_list, kernel[0].value, band)
                    sample = kde_model.kde_model.sample()
                    print(sample)
                    kde_model_serializer.serialize_kde_model(SAVE_PATH, kde_model)
