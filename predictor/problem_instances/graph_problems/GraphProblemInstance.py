from qiskit.aqua.operators import WeightedPauliOperator
from qiskit.aqua.operators.legacy import op_converter

from experiments.optimizers.Optimizer import Optimizer
from helpers.enums.ProblemName import ProblemName


class ProblemInstance:

    def __init__(self, problem_name: ProblemName, p, input_graph, weight_matrix, optimizer: Optimizer,
                 num_starting_points, optimal_params,
                 min_value, qubit_operator: WeightedPauliOperator, offset, most_likely_binary_solution,
                 most_likely_solution_value, classical_solution_value, good_params):
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
        self.good_params = good_params
