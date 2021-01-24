import pickle


def serialize_kde_model(directory, kde_model):
    file_name = 'entry.pickle'
    directory = directory + "\\" + file_name
    with open(directory, 'wb') as f:
        pickle.dump(kde_model, f)
