from qiskit.aqua.algorithms import NumPyMinimumEigensolver
from qiskit.optimization import QuadraticProgram
from qiskit.optimization.algorithms import MinimumEigenOptimizer


def get_classical_solver_result(qubit_operator, offset):
    qp = QuadraticProgram()
    qp.from_ising(qubit_operator, offset)
    exact = MinimumEigenOptimizer(NumPyMinimumEigensolver())
    return exact.solve(qp)


def get_exact_classical_binary_solution(qubit_operator, offset):
    result = get_classical_solver_result(qubit_operator, offset)
    return result.x


def get_exact_classical_fval_solution(qubit_operator, offset):
    result = get_classical_solver_result(qubit_operator, offset)
    return result.fval
