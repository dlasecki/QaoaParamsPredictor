from math import pi

from numpy import concatenate
from numpy.random.mtrand import uniform
from qiskit import Aer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import QAOA
from qiskit.optimization.applications.ising import max_cut
from qiskit.optimization.applications.ising.common import sample_most_likely

from experiments.problem_instances.graph_problems.GraphProblemInstance import ProblemInstance


def qaoa(problem_instance: ProblemInstance):
    backend = Aer.get_backend('statevector_simulator')
    quantum_instance = QuantumInstance(backend)

    min_cost = None
    result_min_cost = None
    all_results = []
    for _ in range(problem_instance.num_starting_points):
        qaoa_object = QAOA(operator=problem_instance.qubit_operator, p=problem_instance.p,
                           optimizer=problem_instance.optimizer.optimizer,
                           initial_point=__generate_uniformly_random_parameters(problem_instance.p))
        result = qaoa_object.run(quantum_instance)
        qaoa_expectation = result['eigenvalue'].real + problem_instance.offset
        all_results.append(result)
        if __is_solution_better(min_cost, qaoa_expectation):
            min_cost, result_min_cost = qaoa_expectation, result
    high_quality_solutions_params = __get_high_quality_solutions(all_results, result_min_cost, problem_instance.offset)
    problem_instance.good_params = high_quality_solutions_params
    most_likely_binary_solution = sample_most_likely(result_min_cost['eigenstate'])
    most_likely_solution_value = max_cut.max_cut_value(most_likely_binary_solution, problem_instance.weight_matrix)
    problem_instance = __get_instance_with_best_solution(problem_instance, -min_cost,
                                                         result_min_cost['optimal_point'],
                                                         most_likely_binary_solution,
                                                         most_likely_solution_value)

    return problem_instance


def __generate_uniformly_random_parameters(p: int):
    return concatenate([uniform(low=0.0, high=2 * pi, size=p), uniform(low=0.0, high=pi, size=p)])


def __is_solution_better(min_cost, qaoa_expectation):
    return not min_cost or qaoa_expectation < min_cost


def __get_instance_with_best_solution(problem_instance: ProblemInstance, min_cost, optimal_params,
                                      most_likely_binary_solution, most_likely_solution_value):
    problem_instance.min_value = min_cost
    problem_instance.optimal_params = optimal_params
    problem_instance.most_likely_binary_solution = most_likely_binary_solution
    problem_instance.most_likely_solution_value = most_likely_solution_value

    return problem_instance


def __get_high_quality_solutions(all_results, best_result, offset):
    high_quality_solutions_params = []
    best_objective_value = best_result['eigenvalue'].real + offset
    allowed_approximation_error = 0.01  # 1% approximation error
    for solution in all_results:
        solution_objective_value = solution['eigenvalue'].real + offset
        optimality_ratio = solution_objective_value / best_objective_value
        approximation_error = 1 - optimality_ratio
        if allowed_approximation_error >= approximation_error >= 0.0:
            high_quality_solutions_params.append(solution['optimal_point'])

    return high_quality_solutions_params
