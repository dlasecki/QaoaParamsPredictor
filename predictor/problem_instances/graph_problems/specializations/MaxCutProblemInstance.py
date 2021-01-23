from qiskit.optimization.applications.ising import max_cut

import problem_instances.instances_generator.graph_weight_matrix_calculator
from helpers.enums.ProblemName import ProblemName
from problem_instances.graph_problems.GraphProblemInstance import ProblemInstance


class MaxCutProblemInstance(ProblemInstance):

    def __init__(self, p, input_graph, optimizer, num_starting_points, optimal_params=None, min_value=None,
                 most_likely_binary_solution=None, most_likely_solution_value=None, good_params=[]):
        self.weight_operator = problem_instances.instances_generator.graph_weight_matrix_calculator.get_weight_matrix(
            input_graph)
        self.qubit_operator, self.offset = max_cut.get_operator(self.weight_operator)
        super().__init__(ProblemName.MAX_CUT, p, input_graph, self.weight_operator, optimizer, num_starting_points,
                         optimal_params, min_value, self.qubit_operator, self.offset, most_likely_binary_solution,
                         most_likely_solution_value, self.__get_classical_solution(), good_params)

    def __get_classical_solution(self):
        x = self.get_classical_exact_binary_solution()
        return max_cut.max_cut_value(x, self.weight_operator)
