from helpers.enums.OptimizerName import OptimizerName
from kernel_density_estimation.data_handlers import kde_model_serializer
from kernel_density_estimation.data_handlers.data_loader import load_jsons
from kernel_density_estimation.kde_model_trainer import train_kde_model

if __name__ == '__main__':
    PATH = "\\experiments\\output\\max_cut\\random"
    SAVE_PATH = "serialized_models"
    kernel = 'gaussian'
    p = 1
    bandwidth = 0.2
    jsons_list = load_jsons(PATH, OptimizerName.COBYLA, p)
    kde_model = train_kde_model(jsons_list, kernel, bandwidth)
    sample = kde_model.kde_model.sample()
    kde_model_serializer.serialize_kde_model(SAVE_PATH, kde_model)
