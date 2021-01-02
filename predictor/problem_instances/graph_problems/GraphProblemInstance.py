from qiskit.aqua.algorithms import NumPyMinimumEigensolver
from qiskit.aqua.operators import WeightedPauliOperator
from qiskit.aqua.operators.legacy import op_converter
from qiskit.optimization.applications.ising.common import sample_most_likely


class ProblemInstance:

    def __init__(self, problem_name, p, input_graph, weight_matrix, optimizer, num_starting_points, optimal_params,
                 min_value, qubit_operator: WeightedPauliOperator, offset, most_likely_binary_solution,
                 most_likely_solution_value, classical_solution_value):
        self.problem_name = problem_name
        self.p = p
        self.input_graph = input_graph
        self.weight_matrix = weight_matrix
        self.optimizer = optimizer
        self.num_starting_points = num_starting_points
        self.optimal_params = optimal_params
        self.min_value = min_value
        self.qubit_operator = qubit_operator
        self.offset = offset
        self.hamiltonian_matrix = op_converter.to_matrix_operator(qubit_operator).matrix
        self.most_likely_binary_solution = most_likely_binary_solution
        self.most_likely_solution_value = most_likely_solution_value
        self.classical_solution_value = classical_solution_value

    def get_classical_most_likely_binary_solution(self):
        numpy_minimum_eigensolver = NumPyMinimumEigensolver(self.qubit_operator)
        result = numpy_minimum_eigensolver.compute_minimum_eigenvalue()

        return sample_most_likely(result.eigenstate)