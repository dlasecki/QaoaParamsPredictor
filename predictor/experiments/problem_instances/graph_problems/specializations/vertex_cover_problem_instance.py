from qiskit.optimization.applications.ising import vertex_cover

from experiments.optimizers.optimizer import Optimizer
from experiments.problem_instances.graph_problems.graph_problem_instance import ProblemInstance
from experiments.problem_instances.instances_generators.graph_problems import graph_weight_matrix_calculator
from experiments.quadratic_solver import get_exact_classical_binary_solution
from helpers.enums.problem_name import ProblemName


class VertexCoverProblemInstance(ProblemInstance):

    def __init__(self, p, input_graph, optimizer: Optimizer, num_starting_points, optimal_params=None,
                 optimal_value=None,
                 most_likely_binary_solution=None, most_likely_solution_value=None, good_params=[]):
        self.weight_operator = graph_weight_matrix_calculator.get_weight_matrix(input_graph)
        self.qubit_operator, self.offset = vertex_cover.get_operator(self.weight_operator)
        super().__init__(ProblemName.VERTEX_COVER, p, input_graph, self.weight_operator, optimizer,
                         num_starting_points, optimal_params, optimal_value, self.qubit_operator, self.offset,
                         most_likely_binary_solution, most_likely_solution_value, self.__get_classical_solution(),
                         good_params)

    def __get_classical_solution(self):
        x = get_exact_classical_binary_solution(self.qubit_operator, self.offset)
        return self.__calc_objective_value(x)

    def __calc_objective_value(self, x):
        # pylint: disable=invalid-name
        # x_mat = np.outer(x, (1 - x))
        # return np.sum(self.weight_operator * x_mat)
        return sum(x)
