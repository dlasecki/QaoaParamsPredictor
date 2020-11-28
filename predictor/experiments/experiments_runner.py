import itertools
import multiprocessing
import time

from experiments import starting_points_generator, optimizers_provider
from instances_generator.maxcut import generate_instances_operators
from instances_generator.graphs_instances_generator import generate_ladder_graph_instances, \
    generate_barbell_graph_instances, generate_random_graph_instances, generate_caveman_graph_instances
from qaoa_solver import qaoa


def worker(qaoa_operator, p_param, optimizer, initial_point):
    qaoa_res = qaoa.qaoa(qaoa_operator, p_param, optimizer, initial_point)
    print(qaoa_res.optimal_params)
    # print(multiprocessing.current_process())
    # results_list.append(qaoa_res)


def get_cartesian_product_of_inputs(graph_instances_train_operators, p_params, optimizers, initial_points):
    return itertools.product([graph_instances_train_operators, p_params, optimizers, initial_points])


if __name__ == '__main__':
    # manager = multiprocessing.Manager()
    # results = manager.list()

    start = time.perf_counter()
    p_params = [1, 2, 3, 4]
    # p_params = [1, 2]
    optimizers = [optimizers_provider.get_cobyla_optimizer()]
    num_of_starting_points = [1000]

    random_graph_num_of_vertices_train = [8]
    random_graph_probabilities_train = [0.5, 0.6, 0.7, 0.8]

    random_graph_num_of_vertices_test = [8, 12, 16, 20]
    random_graph_probabilities_test = [0.5, 0.6, 0.7, 0.8]

    ladder_graph_num_of_vertices_train = [4]
    ladder_graph_num_of_vertices_test = [2, 3, 5, 6, 7, 8, 9, 10, 11]

    caveman_graph_cliques_train = [(2, 4)]
    caveman_graph_cliques_test = [(3, 4), (4, 4), (5, 4), (3, 3), (5, 3), (7, 3), (2, 3), (2, 5), (2, 6), (2, 7),
                                  (2, 8),
                                  (2, 9), (2, 10)]

    barbell_graph_num_of_vertices_train = [4]
    barbell_graph_num_of_vertices_test = [3, 5, 6, 7, 8, 9, 10, 11]

    random_graph_instances_train = generate_random_graph_instances(random_graph_num_of_vertices_train,
                                                                   random_graph_probabilities_train)
    ladder_graph_instances_train = generate_ladder_graph_instances(ladder_graph_num_of_vertices_train)
    caveman_graph_instances_cliques_train = generate_caveman_graph_instances(caveman_graph_cliques_train)
    barbell_graph_instances_train = generate_barbell_graph_instances(barbell_graph_num_of_vertices_train)

    random_graph_instances_train_operators = generate_instances_operators(random_graph_instances_train)
    ladder_graph_instances_train_operators = generate_instances_operators(ladder_graph_instances_train)
    caveman_graph_instances_cliques_train_operators = generate_instances_operators(
        caveman_graph_instances_cliques_train)
    barbell_graph_instances_train_operators = generate_instances_operators(barbell_graph_instances_train)

    initial_points = starting_points_generator.generate_starting_points(p_params, num_of_starting_points)

    # for p in p_params:
    #     for operator in random_graph_instances_train_operators:
    #         res = multiprocessing.Process(target=worker, args=(operator, p, optimizers[0]))
    #         res.start()

    NUM_OF_PROCESSES = 8
    inputs = get_cartesian_product_of_inputs(random_graph_instances_train_operators, p_params, optimizers,
                                             initial_points)
    with multiprocessing.Pool(NUM_OF_PROCESSES) as pool:
        results = pool.map(worker, inputs)

    end = time.perf_counter()

    print(results)

    print(str(end - start) + " seconds")
