from instances_generator import graphs_builder


def generate_ladder_graph_instances(ladder_graph_num_of_vertices):
    instances = []
    for num_of_vertices in ladder_graph_num_of_vertices:
        graph = graphs_builder.generate_ladder_graph(num_of_vertices)
        instances.append(graph)
    return instances


def generate_barbell_graph_instances(barbell_graph_num_of_vertices):
    instances = []
    for num_of_vertices in barbell_graph_num_of_vertices:
        graph = graphs_builder.generate_barbell_graph(num_of_vertices)
        instances.append(graph)
    return instances


def generate_random_graph_instances(random_graph_num_of_vertices, random_graph_probabilities):
    instances = []
    for num_of_vertices in random_graph_num_of_vertices:
        for prob in random_graph_probabilities:
            graph = graphs_builder.generate_random_graph(num_of_vertices, prob)
            instances.append(graph)
    return instances


def generate_caveman_graph_instances(caveman_graph_cliques):
    instances = []
    for clique_num, clique_size in caveman_graph_cliques:
        graph = graphs_builder.generate_caveman_graph(clique_num, clique_size)
        instances.append(graph)
    return instances