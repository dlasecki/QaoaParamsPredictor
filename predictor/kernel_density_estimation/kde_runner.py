from helpers.enums.kernel import Kernel
from helpers.enums.optimizer_name import OptimizerName
from kernel_density_estimation.data_handlers import kde_model_serializer
from kernel_density_estimation.data_handlers.data_loader import load_jsons
from kernel_density_estimation.kde_model_trainer import train_kde_model

if __name__ == '__main__':
    # PATH = "\\experiments\\output\\max_cut\\erdos_renyi"
    problem = "partition"
    graph_type_name = "ladder"
    PATH = "\\experiments\\workflow_results_converted\\" + problem + "\\" + graph_type_name + "\\"
    SAVE_PATH = "serialized_models"
    kernel = [Kernel.GAUSSIAN, Kernel.EPANECHNIKOV, Kernel.TOPHAT, Kernel.LINEAR, Kernel.COSINE, Kernel.EXPONENTIAL]
    p = [1, 2, 3, 4]
    bandwidth = [0.2, 0.4, 0.6, 0.8]
    for p_param in p:
        for band in bandwidth:
            jsons_list = load_jsons(PATH, OptimizerName.LBFGS, p_param)
            kde_model = train_kde_model(jsons_list, kernel[0].value, band)
            sample = kde_model.kde_model.sample()
            print(sample)
            kde_model_serializer.serialize_kde_model(SAVE_PATH, kde_model)
