import networkx as nx

from data_structures.enums.graph_type import GraphType


def generate_caveman_graph(number_of_cliques: int, size_of_cliques: int, graph_id: int):
    """Generates a caveman graph based on its parameters."""
    graph = nx.caveman_graph(number_of_cliques, size_of_cliques)
    graph = _get_graph_with_attributes(graph, graph_id, GraphType.CAVEMAN)
    return graph


def generate_ladder_graph(length_of_ladder: int, graph_id: int):
    """Generates a ladder graph based on its parameters."""
    graph = nx.ladder_graph(length_of_ladder)
    graph = _get_graph_with_attributes(graph, graph_id, GraphType.LADDER)
    return graph


def generate_barbell_graph(number_of_vertices_complete_graph: int, graph_id: int):
    """Generates a barbell graph based on its parameters."""
    graph = nx.barbell_graph(number_of_vertices_complete_graph, number_of_vertices_complete_graph)
    graph = _get_graph_with_attributes(graph, graph_id, GraphType.BARBELL)
    return graph


def generate_random_graph(number_of_vertices: int, edge_generation_probability: float, graph_id: int):
    """Generates a random graph based on its parameters."""
    graph = nx.erdos_renyi_graph(number_of_vertices, edge_generation_probability)
    graph = _get_graph_with_attributes(graph, graph_id, GraphType.RANDOM)
    return graph


def _get_graph_with_attributes(graph, graph_id: int, graph_type: GraphType):
    """Adds additional attributed to a networkx graph - ID and type of a graph."""
    graph.graph["graph_id"] = graph_id
    graph.graph["graph_type"] = graph_type
    return graph
