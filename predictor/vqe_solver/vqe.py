import numpy as np
from qiskit import Aer
from qiskit.aqua import aqua_globals, QuantumInstance
from qiskit.aqua.algorithms import VQE
from qiskit.aqua.components.optimizers import SPSA
from qiskit.circuit.library import TwoLocal


def run_vqe(qubit_operator, repetitions: int, optimizer_max_iterations: int):
    backend = Aer.get_backend('statevector_simulator')
    quantum_instance = QuantumInstance(backend)
    simultaneous_perturbation_stochastic_approximation = SPSA(maxiter=optimizer_max_iterations)
    ry = TwoLocal(qubit_operator.num_qubits, 'ry', 'cz', reps=repetitions, entanglement='linear')
    vqe = VQE(qubit_operator, ry, simultaneous_perturbation_stochastic_approximation, quantum_instance=quantum_instance)

    return vqe.run(quantum_instance)
