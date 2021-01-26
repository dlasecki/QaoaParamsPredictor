import networkx as nx

from helpers.enums.GraphType import GraphType


def generate_caveman_graph(number_of_cliques: int, size_of_cliques: int, graph_id: int):
    graph = nx.caveman_graph(number_of_cliques, size_of_cliques)
    graph = __get_graph_with_attributes(graph, graph_id, GraphType.CAVEMAN)
    return graph


def generate_ladder_graph(length_of_ladder: int, graph_id: int):
    graph = nx.ladder_graph(length_of_ladder)
    graph = __get_graph_with_attributes(graph, graph_id, GraphType.LADDER)
    return graph


def generate_barbell_graph(number_of_vertices_complete_graph: int, graph_id: int):
    graph = nx.barbell_graph(number_of_vertices_complete_graph, number_of_vertices_complete_graph)
    graph = __get_graph_with_attributes(graph, graph_id, GraphType.BARBELL)
    return graph


def generate_random_graph(number_of_vertices: int, edge_generation_probability: float, graph_id: int):
    graph = nx.erdos_renyi_graph(number_of_vertices, edge_generation_probability)
    graph = __get_graph_with_attributes(graph, graph_id, GraphType.RANDOM)
    return graph


def __get_graph_with_attributes(graph, graph_id: int, graph_type: GraphType):
    graph.graph["graph_id"] = graph_id
    graph.graph["graph_type"] = graph_type
    return graph
