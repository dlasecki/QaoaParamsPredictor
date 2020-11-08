import networkx as nx
import qiskit
from qiskit.optimization.applications.ising import max_cut


def generate_caveman_graph(number_of_cliques: int, size_of_cliques: int):
    return nx.caveman_graph(number_of_cliques, size_of_cliques)


def generate_ladder_graph(length_of_ladder: int):
    return nx.ladder_graph(length_of_ladder)


def generate_barbell_graph(number_of_vertices_complete_graph: int):
    return nx.barbell_graph(number_of_vertices_complete_graph, number_of_vertices_complete_graph)


def generate_random_graph(number_of_vertices: int, edge_generation_probability: float):
    return nx.erdos_renyi_graph(number_of_vertices, edge_generation_probability)


def get_weight_matrix(graph):
    return nx.adjacency_matrix(graph)
