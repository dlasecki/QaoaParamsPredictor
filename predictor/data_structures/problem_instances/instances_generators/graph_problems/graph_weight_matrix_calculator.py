import networkx as nx


def get_weight_matrix(graph):
    """Returns a weight matrix corresponding to a networkx graph."""
    return nx.to_numpy_matrix(graph).A
