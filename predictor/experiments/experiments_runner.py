import itertools
import multiprocessing
import time

from problem_instances.instances_generator.graphs_instances_generator import generate_ladder_graph_instances, \
    generate_barbell_graph_instances, generate_random_graph_instances, generate_caveman_graph_instances

from experiments import optimizers_factory
from experiments.data_handlers import results_serializer
from helpers.enums.ProblemName import ProblemName
from problem_instances.graph_problems.graph_problem_instance_factory import create_graph_problem_instance
from qaoa_solver import qaoa


def worker(problem_name, input_graph, p_param, optimizer, initial_points_num):
    problem_instance = create_graph_problem_instance(problem_name, p_param, input_graph, optimizer, initial_points_num)
    qaoa_res = qaoa.qaoa(problem_instance)
    directory = "output\\" + problem_name.value + "\\" + problem_instance.input_graph.graph["graph_type"].value
    results_serializer.save_to_json(directory, qaoa_res)

    return qaoa_res.optimal_params, qaoa_res.min_value


def __get_cartesian_product_of_inputs(problems, graph_instances_train_operators, p_params, optimizers,
                                      initial_points_num):
    return itertools.product(problems, graph_instances_train_operators, p_params, optimizers, initial_points_num)


def get_random_graphs_train_instances():
    random_graph_num_of_vertices_train = [8]
    random_graph_probabilities_train = [0.5, 0.6, 0.7, 0.8]
    return generate_random_graph_instances(random_graph_num_of_vertices_train, random_graph_probabilities_train)


def get_random_graphs_test_instances():
    random_graph_num_of_vertices_test = [8, 12, 16, 20]
    random_graph_probabilities_test = [0.5, 0.6, 0.7, 0.8]
    return generate_random_graph_instances(random_graph_num_of_vertices_test, random_graph_probabilities_test)


def get_ladder_graphs_train_instances():
    ladder_graph_num_of_vertices_train = [4]
    return generate_ladder_graph_instances(ladder_graph_num_of_vertices_train)


def get_ladder_graphs_test_instances():
    ladder_graph_num_of_vertices_test = [2, 3, 5, 6, 7, 8, 9, 10, 11]
    return generate_ladder_graph_instances(ladder_graph_num_of_vertices_test)


def get_caveman_graphs_train_instances():
    caveman_graph_cliques_train = [(2, 4)]
    return generate_caveman_graph_instances(caveman_graph_cliques_train)


def get_caveman_graphs_test_instances():
    caveman_graph_cliques_test = [(3, 4), (4, 4), (5, 4), (3, 3), (5, 3), (7, 3), (2, 3), (2, 5), (2, 6), (2, 7),
                                  (2, 8), (2, 9), (2, 10)]

    return generate_caveman_graph_instances(caveman_graph_cliques_test)


def get_barbell_graphs_train_instances():
    barbell_graph_num_of_vertices_train = [4]
    return generate_barbell_graph_instances(barbell_graph_num_of_vertices_train)


def get_barbell_graphs_test_instances():
    barbell_graph_num_of_vertices_test = [3, 5, 6, 7, 8, 9, 10, 11]
    return generate_barbell_graph_instances(barbell_graph_num_of_vertices_test)


if __name__ == '__main__':
    start = time.perf_counter()
    num_of_starting_points = [10]
    p_params = [1, 2, 3, 4]
    problems = [ProblemName.MAX_CUT]
    NUM_OF_PROCESSES = 8
    optimizers = [optimizers_factory.get_cobyla_optimizer()]

    inputs_random = __get_cartesian_product_of_inputs(problems, get_random_graphs_train_instances(), p_params,
                                                      optimizers, num_of_starting_points)
    inputs_ladder = __get_cartesian_product_of_inputs(problems, get_ladder_graphs_train_instances(), p_params,
                                                      optimizers, num_of_starting_points)
    inputs_caveman = __get_cartesian_product_of_inputs(problems, get_caveman_graphs_train_instances(), p_params,
                                                       optimizers, num_of_starting_points)
    inputs_barbell = __get_cartesian_product_of_inputs(problems, get_barbell_graphs_train_instances(), p_params,
                                                       optimizers, num_of_starting_points)
    inputs = itertools.chain(inputs_random)

    with multiprocessing.Pool(processes=NUM_OF_PROCESSES) as pool:
        results = pool.starmap(worker, inputs)

    print(results)
    end = time.perf_counter()
    print(str(end - start) + " seconds")
