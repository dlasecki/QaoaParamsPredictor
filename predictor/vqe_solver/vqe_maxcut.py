from qiskit import Aer
from qiskit.aqua import aqua_globals, QuantumInstance
from qiskit.aqua.algorithms import VQE
from qiskit.aqua.components.optimizers import SPSA
from qiskit.circuit.library import TwoLocal
from qiskit.optimization.applications.ising import max_cut
import numpy as np


def get_qaoa_operator(weight_matrix):
    return max_cut.get_operator(weight_matrix)


def run_vqe(weight_matrix, repetitions: int, optimizer_max_iterations: int):
    aqua_globals.random_seed = np.random.default_rng(123)
    seed = 10598
    backend = Aer.get_backend('statevector_simulator')
    quantum_instance = QuantumInstance(backend, seed_simulator=seed, seed_transpiler=seed)
    simultaneous_perturbation_stochastic_approximation = SPSA(maxiter=optimizer_max_iterations)
    qubit_operator, offset = get_qaoa_operator(weight_matrix)
    ry = TwoLocal(qubit_operator.num_qubits, 'ry', 'cz', reps=repetitions, entanglement='linear')
    vqe = VQE(qubit_operator, ry, simultaneous_perturbation_stochastic_approximation, quantum_instance=quantum_instance)

    return vqe.run(quantum_instance)
