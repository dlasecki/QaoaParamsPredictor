from qiskit import Aer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import QAOA


def qaoa(qubit_operator, p, optimizer):
    backend = Aer.get_backend('statevector_simulator')
    quantum_instance = QuantumInstance(backend)
    qaoa_object = QAOA(operator=qubit_operator, p=p, optimizer=optimizer)
    qaoa_object.run(quantum_instance)
    return qaoa_object
