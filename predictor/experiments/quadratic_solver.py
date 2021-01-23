from qiskit.aqua.algorithms import NumPyMinimumEigensolver
from qiskit.optimization import QuadraticProgram
from qiskit.optimization.algorithms import MinimumEigenOptimizer


def get_exact_classical_binary_solution(qubit_operator, offset):
    qp = QuadraticProgram()
    qp.from_ising(qubit_operator, offset)
    exact = MinimumEigenOptimizer(NumPyMinimumEigensolver())
    result = exact.solve(qp)
    return result.x
