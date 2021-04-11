import dill


def load_kde_model(file_path):
    with open(file_path, 'rb') as file:
        kde_model = dill.load(file)
    return kde_model
