import networkx as nx


def get_weight_matrix(graph):
    return nx.to_numpy_matrix(graph).A
