import itertools
import multiprocessing
import time

from qiskit import Aer
from qiskit.aqua import QuantumInstance

from experiments.kde_model_provider import get_kde_model
from experiments.problem_instances.graph_problems.graph_problem_instance_factory import create_graph_problem_instance
from experiments.problem_instances.instances_generators.graph_problems.graphs_instances_generator import \
    generate_random_graph_instances, generate_ladder_graph_instances, generate_caveman_graph_instances, \
    generate_barbell_graph_instances
from helpers.enums.problem_name import ProblemName
from qaoa_solver import qaoa
from qaoa_solver.qaoa import __is_solution_better, __get_instance_with_best_solution


def worker(problem_name, graph_type, input_graph, p_param, bandwidth, kernel):
    backend = Aer.get_backend('statevector_simulator')
    quantum_instance = QuantumInstance(backend)
    problem_instance = create_graph_problem_instance(problem_name, p_param, input_graph)
    min_cost_expectation = None
    result_min_cost = None
    min_cost_params = None
    kde_model = get_kde_model(problem_name, graph_type, p_param, kernel, bandwidth)
    initial_points = kde_model.kde_model.sample(10)
    print(initial_points)
    for initial_point in initial_points:
        qaoa_res = qaoa.qaoa(quantum_instance, problem_instance, initial_point)
        qaoa_expectation = qaoa_res['eigenvalue'].real + problem_instance.offset
        if __is_solution_better(min_cost_expectation, qaoa_expectation):
            min_cost_expectation, result_min_cost, min_cost_params = qaoa_expectation, qaoa_res, initial_point
    result_min_cost = __get_instance_with_best_solution(problem_instance, min_cost_expectation, min_cost_params, None,
                                                        None)
    # TODO save to model_validation folder
    directory = __build_problem_instance_directory(problem_instance, problem_name)
    # results_serializer.save_to_json(directory, result_min_cost)
    print(result_min_cost.optimal_params, result_min_cost.optimal_value)
    print(result_min_cost.classical_solution_value)
    return result_min_cost.optimal_params, result_min_cost.optimal_value


def __build_problem_instance_directory(problem_instance, problem_name):
    directory = "output\\" + problem_name.value + "\\" + problem_instance.input_graph.graph[
        "graph_type"].value + "_evaluation"
    return directory


def __get_cartesian_product_of_inputs(problems, graph_types, graph_instances_train_operators, p_params, bandwidths,
                                      kernels):
    return itertools.product(problems, graph_types, graph_instances_train_operators, p_params, bandwidths, kernels)


def get_random_graphs_test_instances():
    # random_graph_num_of_vertices_test = [8, 12, 16, 20]
    # random_graph_probabilities_test = [0.5, 0.6, 0.7, 0.8]
    random_graph_num_of_vertices_test = [12]
    random_graph_probabilities_test = [0.5]
    return generate_random_graph_instances(random_graph_num_of_vertices_test, random_graph_probabilities_test)


def get_ladder_graphs_test_instances():
    ladder_graph_num_of_vertices_test = [2, 3, 5, 6, 7, 8, 9, 10, 11]
    return generate_ladder_graph_instances(ladder_graph_num_of_vertices_test)


def get_caveman_graphs_test_instances():
    caveman_graph_cliques_test = [(3, 4), (4, 4), (5, 4), (3, 3), (5, 3), (7, 3), (2, 3), (2, 5), (2, 6), (2, 7),
                                  (2, 8), (2, 9), (2, 10)]

    return generate_caveman_graph_instances(caveman_graph_cliques_test)


def get_barbell_graphs_test_instances():
    barbell_graph_num_of_vertices_test = [3, 5, 6, 7, 8, 9, 10, 11]
    return generate_barbell_graph_instances(barbell_graph_num_of_vertices_test)


if __name__ == '__main__':
    start = time.perf_counter()
    p_params = [2]
    problems = [ProblemName.VERTEX_COVER]
    graph_types = ["erdos_renyi"]
    NUM_OF_PROCESSES = 8
    bandwidths = [0.2]
    kernels = ["gaussian"]

    inputs_random = __get_cartesian_product_of_inputs(problems, graph_types, get_random_graphs_test_instances(),
                                                      p_params, bandwidths, kernels)
    inputs_ladder = __get_cartesian_product_of_inputs(problems, graph_types, get_ladder_graphs_test_instances(),
                                                      p_params, bandwidths, kernels)
    inputs_caveman = __get_cartesian_product_of_inputs(problems, graph_types, get_caveman_graphs_test_instances(),
                                                       p_params, bandwidths, kernels)
    inputs_barbell = __get_cartesian_product_of_inputs(problems, graph_types, get_barbell_graphs_test_instances(),
                                                       p_params, bandwidths, kernels)
    inputs = itertools.chain(inputs_random)

    with multiprocessing.Pool(processes=NUM_OF_PROCESSES) as pool:
        results = pool.starmap(worker, inputs)

    end = time.perf_counter()
    print(str(end - start) + " seconds")
