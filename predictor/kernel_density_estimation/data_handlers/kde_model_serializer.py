import dill

from kernel_density_estimation.kde_model import KdeModel


def serialize_kde_model(directory, kde_model: KdeModel):
    """Uses dill to save a binary of a KDE model in the directory provided."""
    file_name = _create_model_file_name(kde_model)
    directory = directory + "\\" + file_name
    with open(directory, 'wb') as f:
        dill.dump(kde_model, f)


def _create_model_file_name(kde_model: KdeModel):
    """Constructs a file name for a given KDE model."""
    problem_name = kde_model.problem_name
    graph_type = kde_model.graph_type
    kernel = kde_model.kernel
    bandwidth = kde_model.bandwidth
    p = kde_model.p
    return 'kde_model_' + problem_name + "_" + graph_type + "_" + kernel + "_bandwidth=" + str(bandwidth) + "_p=" + str(
        p)
