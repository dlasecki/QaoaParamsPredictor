from qiskit.optimization.applications.ising import stable_set

import instances_generator.graph_weight_matrix_calculator
from problem_instances.graph_problems.GraphProblemInstance import ProblemInstance


class StableSetProblemInstance(ProblemInstance):

    def __init__(self, p, input_graph, optimizer, num_starting_points, optimal_params=None, min_value=None,
                 most_likely_binary_solution=None, most_likely_solution_value=None):
        self.weight_operator = instances_generator.graph_weight_matrix_calculator.get_weight_matrix(input_graph)
        self.qubit_operator, self.offset = stable_set.get_operator(self.weight_operator)
        super().__init__("StableSet", p, input_graph, self.weight_operator, optimizer, num_starting_points,
                         optimal_params, min_value, self.qubit_operator, self.offset,
                         most_likely_binary_solution, most_likely_solution_value, self.__get_classical_solution())

    def __get_classical_solution(self):
        x = self.__get_classical_most_likely_binary_solution()
        return stable_set.stable_set_value(x, self.weight_operator)
