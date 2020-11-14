from qiskit import Aer
from qiskit import Aer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import QAOA
from qiskit.aqua.components.optimizers import COBYLA

from vqe_solver.vqe_maxcut import get_qaoa_operator


def qaoa(weight_matrix, p):
    backend = Aer.get_backend('statevector_simulator')
    quantum_instance = QuantumInstance(backend)
    qubit_operator, offset = get_qaoa_operator(weight_matrix)
    cobyla = COBYLA()
    qaoa_object = QAOA(operator=qubit_operator, p=p, optimizer=cobyla)
    qaoa_object.run(quantum_instance)
    return qaoa_object
