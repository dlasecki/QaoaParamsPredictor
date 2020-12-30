from qiskit.optimization.applications.ising import stable_set

import instances_generator.graph_weight_matrix_calculator
from problem_instances.graph_problems.ProblemInstance import ProblemInstance


class StableSetProblemInstance(ProblemInstance):

    def __init__(self, problem_id, p, input_graph, optimizer, num_starting_points, optimal_params=None, min_value=None):
        self.weight_operator = instances_generator.graph_weight_matrix_calculator.get_weight_matrix(input_graph)
        self.qubit_operator, self.offset = stable_set.get_operator(self.weight_operator)
        super().__init__(problem_id, "StableSet", p, input_graph, optimizer, num_starting_points, optimal_params,
                         min_value, self.qubit_operator, self.offset)
