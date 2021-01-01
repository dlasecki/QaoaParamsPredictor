from qiskit import Aer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import QAOA
from qiskit.optimization.applications.ising import max_cut
from qiskit.optimization.applications.ising.common import sample_most_likely

from problem_instances.graph_problems.GraphProblemInstance import ProblemInstance


def qaoa(problem_instance: ProblemInstance):
    backend = Aer.get_backend('statevector_simulator')
    quantum_instance = QuantumInstance(backend)

    min_cost = None
    qaoa_object_min_cost = None

    for _ in range(problem_instance.num_starting_points):
        qaoa_object = QAOA(operator=problem_instance.qubit_operator, p=problem_instance.p,
                           optimizer=problem_instance.optimizer)
        qaoa_object.run(quantum_instance)

        if __is_solution_better(min_cost, qaoa_object):
            min_cost, qaoa_object_min_cost = __get_updated_solution(qaoa_object)

    most_likely_binary_solution = sample_most_likely(qaoa_object_min_cost.compute_minimum_eigenvalue().eigenstate)
    most_likely_solution_value = max_cut.max_cut_value(most_likely_binary_solution, problem_instance.weight_matrix)
    problem_instance = __get_instance_with_best_solution(problem_instance, min_cost,
                                                         qaoa_object_min_cost.optimal_params, most_likely_binary_solution,
                                                         most_likely_solution_value)

    return problem_instance


def __is_solution_better(min_cost, qaoa_object):
    return not min_cost or qaoa_object.get_optimal_cost() < min_cost


def __get_updated_solution(qaoa_object):
    return qaoa_object.get_optimal_cost(), qaoa_object


def __get_instance_with_best_solution(problem_instance: ProblemInstance, min_cost, optimal_params,
                                      most_likely_binary_solution, most_likely_solution_value):
    problem_instance.min_value = min_cost
    problem_instance.optimal_params = optimal_params
    problem_instance.most_likely_binary_solution = most_likely_binary_solution
    problem_instance.most_likely_solution_value = most_likely_solution_value

    return problem_instance
