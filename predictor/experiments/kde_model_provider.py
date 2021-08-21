import pathlib
from os import listdir
from os.path import join, isfile

from kernel_density_estimation.data_handlers.kde_model_loader import load_kde_model


def get_kde_model(problem_name, graph_type, p, kernel, bandwidth):
    """Finds a file containing a relevant KDE model and loads it."""
    # TODO match by problem name
    fn = pathlib.Path(__file__).parent.parent

    models_directory = 'kernel_density_estimation\serialized_models'
    models_directory = join(str(fn), models_directory)

    all_model_files = [file_name for file_name in listdir(models_directory) if
                       isfile(join(models_directory, file_name))]

    matches = [problem_name.value if problem_name.value != "graph_partition" else "partition", graph_type,
               "p=" + str(p), kernel, "bandwidth=" + str(bandwidth)]
    print(matches)

    for file_name in all_model_files:
        if all(match in file_name for match in matches):
            return load_kde_model(join(models_directory, file_name))
    return None
