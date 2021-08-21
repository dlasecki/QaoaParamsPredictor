from data_structures.problem_instances.instances_generators.graph_problems import graphs_builder


def generate_ladder_graph_instances(ladder_graph_ladder_lengths):
    """Generates ladder graph instances from a list of parameters defining each graph and gives them ID."""
    instances = []
    graph_id = 0
    for ladder_length in ladder_graph_ladder_lengths:
        graph = graphs_builder.generate_ladder_graph(ladder_length, graph_id)
        instances.append(graph)
        graph_id += 1
    return instances


def generate_barbell_graph_instances(barbell_graph_num_of_vertices):
    """Generates barbell graph instances from a list of parameters defining each graph and gives them ID."""
    instances = []
    graph_id = 0
    for num_of_vertices in barbell_graph_num_of_vertices:
        graph = graphs_builder.generate_barbell_graph(num_of_vertices, graph_id)
        instances.append(graph)
        graph_id += 1
    return instances


def generate_random_graph_instances(random_graph_num_of_vertices, random_graph_probabilities):
    """Generates random graph instances from a list of parameters defining each graph and gives them ID."""
    instances = []
    graph_id = 0
    for num_of_vertices in random_graph_num_of_vertices:
        for prob in random_graph_probabilities:
            graph = graphs_builder.generate_random_graph(num_of_vertices, prob, graph_id)
            instances.append(graph)
            graph_id += 1
    return instances


def generate_caveman_graph_instances(caveman_graph_cliques):
    """Generates caveman graph instances from a list of parameters defining each graph and gives them ID."""
    instances = []
    graph_id = 0
    for clique_num, clique_size in caveman_graph_cliques:
        graph = graphs_builder.generate_caveman_graph(clique_num, clique_size, graph_id)
        instances.append(graph)
        graph_id += 1
    return instances
