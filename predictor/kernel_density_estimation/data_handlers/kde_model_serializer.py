import pickle

from kernel_density_estimation.KdeModel import KdeModel


def serialize_kde_model(directory, kde_model: KdeModel):
    file_name = __create_model_file_name(kde_model)
    directory = directory + "\\" + file_name
    with open(directory, 'wb') as f:
        pickle.dump(kde_model, f)


def __create_model_file_name(kde_model: KdeModel):
    problem_name = kde_model.problem_name
    graph_type = kde_model.graph_type
    kernel = kde_model.kernel
    bandwidth = kde_model.bandwidth
    return 'kde_model_' + problem_name + "_" + graph_type + "_" + kernel + "_bandwidth=" + str(bandwidth)
