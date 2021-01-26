from qiskit.optimization.applications.ising import graph_partition

from experiments.optimizers.Optimizer import Optimizer
from experiments.problem_instances.graph_problems.GraphProblemInstance import ProblemInstance
from experiments.problem_instances.instances_generators.graph_problems import graph_weight_matrix_calculator
from experiments.quadratic_solver import get_exact_classical_binary_solution
from helpers.enums.ProblemName import ProblemName


class GraphPartitionProblemInstance(ProblemInstance):

    def __init__(self, p, input_graph, optimizer: Optimizer, num_starting_points, optimal_params=None, min_value=None,
                 most_likely_binary_solution=None, most_likely_solution_value=None, good_params=[]):
        self.weight_operator = graph_weight_matrix_calculator.get_weight_matrix(
            input_graph)
        self.qubit_operator, self.offset = graph_partition.get_operator(self.weight_operator)
        super().__init__(ProblemName.GRAPH_PARTITION, p, input_graph, self.weight_operator, optimizer,
                         num_starting_points, optimal_params, min_value, self.qubit_operator, self.offset,
                         most_likely_binary_solution, most_likely_solution_value, self.__get_classical_solution(),
                         good_params)

    def __get_classical_solution(self):
        x = get_exact_classical_binary_solution(self.qubit_operator, self.offset)
        return graph_partition.objective_value(x, self.weight_operator)
