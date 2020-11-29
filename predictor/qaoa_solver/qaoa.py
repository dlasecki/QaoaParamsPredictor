from qiskit import Aer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import QAOA


def qaoa(qubit_operator, p, optimizer, initial_points_num):
    backend = Aer.get_backend('statevector_simulator')
    quantum_instance = QuantumInstance(backend)
    min_cost = None
    qaoa_object_min_cost = None
    for roundId in range(initial_points_num):
        qaoa_object = QAOA(operator=qubit_operator, p=p, optimizer=optimizer)
        qaoa_object.run(quantum_instance)
        if not min_cost or qaoa_object.get_optimal_cost() < min_cost:
            min_cost = qaoa_object.get_optimal_cost()
            qaoa_object_min_cost = qaoa_object

    return qaoa_object_min_cost
