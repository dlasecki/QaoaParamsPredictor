import networkx as nx


class GraphsGenerator:

    @staticmethod
    def generate_caveman_graph(number_of_cliques: int, size_of_cliques: int):
        return nx.caveman_graph(number_of_cliques, size_of_cliques)

    @staticmethod
    def generate_ladder_graph(length_of_ladder: int):
        return nx.ladder_graph(length_of_ladder)

    @staticmethod
    def generate_barbell_graph(number_of_vertices_complete_graph: int):
        return nx.barbell_graph(number_of_vertices_complete_graph, number_of_vertices_complete_graph)

    @staticmethod
    def generate_random_graph(number_of_vertices: int, edge_generation_probability: float):
        return nx.erdos_renyi_graph(number_of_vertices, edge_generation_probability)
