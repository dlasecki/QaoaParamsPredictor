import itertools
import multiprocessing
import time

from experiments import optimizers_provider, results_serializer
from instances_generator.graphs_instances_generator import generate_ladder_graph_instances, \
    generate_barbell_graph_instances, generate_random_graph_instances, generate_caveman_graph_instances
from problem_instances.graph_problems.specializations.MaxCutProblemInstance import MaxCutProblemInstance
from qaoa_solver import qaoa


def worker(input_graph, p_param, optimizer, initial_points_num):
    problem_instance = MaxCutProblemInstance(p_param, input_graph, optimizer,
                                             initial_points_num) #TODO support other problems
    qaoa_res = qaoa.qaoa(problem_instance)
    results_serializer.save_to_json('output', qaoa_res)

    return qaoa_res.optimal_params, qaoa_res.min_value


def __get_cartesian_product_of_inputs(graph_instances_train_operators, p_params, optimizers, initial_points_num):
    return itertools.product(graph_instances_train_operators, p_params, optimizers, initial_points_num)


def get_random_graphs_train_instances():
    random_graph_num_of_vertices_train = [8]
    random_graph_probabilities_train = [0.5, 0.6, 0.7, 0.8]

    random_graph_instances_train = generate_random_graph_instances(random_graph_num_of_vertices_train,
                                                                   random_graph_probabilities_train)
    return random_graph_instances_train


def get_random_graphs_test_instances():
    random_graph_num_of_vertices_test = [8, 12, 16, 20]
    random_graph_probabilities_test = [0.5, 0.6, 0.7, 0.8]

    random_graph_instances_test = generate_random_graph_instances(random_graph_num_of_vertices_test,
                                                                  random_graph_probabilities_test)
    return random_graph_instances_test


def get_ladder_graphs_train_instances():
    ladder_graph_num_of_vertices_train = [4]
    ladder_graph_instances_train = generate_ladder_graph_instances(ladder_graph_num_of_vertices_train)

    return ladder_graph_instances_train


def get_ladder_graphs_test_instances():
    ladder_graph_num_of_vertices_test = [2, 3, 5, 6, 7, 8, 9, 10, 11]

    ladder_graph_instances_test = generate_ladder_graph_instances(ladder_graph_num_of_vertices_test)
    return ladder_graph_instances_test


def get_caveman_graphs_train_instances():
    caveman_graph_cliques_train = [(2, 4)]

    caveman_graph_instances_train = generate_caveman_graph_instances(caveman_graph_cliques_train)
    return caveman_graph_instances_train


def get_caveman_graphs_test_instances():
    caveman_graph_cliques_test = [(3, 4), (4, 4), (5, 4), (3, 3), (5, 3), (7, 3), (2, 3), (2, 5), (2, 6), (2, 7),
                                  (2, 8), (2, 9), (2, 10)]

    caveman_graph_instances_test = generate_caveman_graph_instances(caveman_graph_cliques_test)
    return caveman_graph_instances_test


def get_barbell_graphs_train_instances():
    barbell_graph_num_of_vertices_train = [4]

    barbell_graph_instances_train = generate_barbell_graph_instances(barbell_graph_num_of_vertices_train)
    return barbell_graph_instances_train


def get_barbell_graphs_test_instances():
    barbell_graph_num_of_vertices_test = [3, 5, 6, 7, 8, 9, 10, 11]

    barbell_graph_instances_test = generate_barbell_graph_instances(barbell_graph_num_of_vertices_test)
    return barbell_graph_instances_test


if __name__ == '__main__':
    start = time.perf_counter()
    num_of_starting_points = [10]
    p_params = [1, 2, 3, 4]
    NUM_OF_PROCESSES = 10
    # p_params = [1]
    optimizers = [optimizers_provider.get_cobyla_optimizer()]
    # optimizers = [optimizers_provider.get_cobyla_optimizer(), optimizers_provider.get_spsa_optimizer(),
    #               optimizers_provider.get_lbfgs_optimizer(), optimizers_provider.get_nelder_mead_optimizer()]

    random_graph_instances_train = get_random_graphs_train_instances()
    ladder_graph_instances_train = get_ladder_graphs_train_instances()
    caveman_graph_instances_cliques_train = get_caveman_graphs_train_instances()
    barbell_graph_instances_train = get_barbell_graphs_train_instances()

    inputs_random = __get_cartesian_product_of_inputs(random_graph_instances_train, p_params, optimizers,
                                                      num_of_starting_points)
    inputs_ladder = __get_cartesian_product_of_inputs(ladder_graph_instances_train, p_params, optimizers,
                                                      num_of_starting_points)
    inputs_caveman = __get_cartesian_product_of_inputs(caveman_graph_instances_cliques_train, p_params, optimizers,
                                                       num_of_starting_points)
    inputs_barbell = __get_cartesian_product_of_inputs(barbell_graph_instances_train, p_params, optimizers,
                                                       num_of_starting_points)
    inputs = itertools.chain(inputs_random, inputs_ladder, inputs_caveman, inputs_barbell)

    with multiprocessing.Pool(processes=NUM_OF_PROCESSES) as pool:
        results = pool.starmap(worker, inputs)

    print(results)

    end = time.perf_counter()

    print(str(end - start) + " seconds")
