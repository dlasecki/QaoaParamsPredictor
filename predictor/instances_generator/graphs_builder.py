import networkx as nx


def generate_caveman_graph(number_of_cliques: int, size_of_cliques: int, graph_id: int):
    graph = nx.caveman_graph(number_of_cliques, size_of_cliques)
    graph.graph["graph_id"] = graph_id
    graph.graph["graph_type"] = "Caveman"
    return graph


def generate_ladder_graph(length_of_ladder: int, graph_id: int):
    graph = nx.ladder_graph(length_of_ladder)
    graph.graph["graph_id"] = graph_id
    graph.graph["graph_type"] = "Ladder"
    return graph


def generate_barbell_graph(number_of_vertices_complete_graph: int, graph_id: int):
    graph = nx.barbell_graph(number_of_vertices_complete_graph, number_of_vertices_complete_graph)
    graph.graph["graph_id"] = graph_id
    graph.graph["graph_type"] = "Barbell"
    return graph


def generate_random_graph(number_of_vertices: int, edge_generation_probability: float, graph_id: int):
    graph = nx.erdos_renyi_graph(number_of_vertices, edge_generation_probability)
    graph.graph["graph_id"] = graph_id
    graph.graph["graph_type"] = "Random"
    return graph
