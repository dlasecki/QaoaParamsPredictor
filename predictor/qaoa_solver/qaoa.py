from qiskit import Aer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import QAOA

from problem_instances.ProblemInstance import ProblemInstance


def qaoa(problem_instance: ProblemInstance):
    backend = Aer.get_backend('statevector_simulator')
    quantum_instance = QuantumInstance(backend)

    qubit_operator = problem_instance.qubit_operator
    p = problem_instance.p
    optimizer = problem_instance.optimizer
    initial_points_num = problem_instance.num_starting_points

    min_cost = None
    qaoa_object_min_cost = None
    for roundId in range(initial_points_num):
        qaoa_object = QAOA(operator=qubit_operator, p=p, optimizer=optimizer)
        qaoa_object.run(quantum_instance)
        if not min_cost or qaoa_object.get_optimal_cost() < min_cost:
            min_cost = qaoa_object.get_optimal_cost()
            qaoa_object_min_cost = qaoa_object

    problem_instance.min_value = min_cost
    problem_instance.optimal_params = qaoa_object_min_cost.optimal_params

    return problem_instance
