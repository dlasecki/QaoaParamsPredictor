from qiskit.optimization.applications.ising import vertex_cover

import instances_generator.graph_weight_matrix_calculator
from problem_instances.graph_problems.GraphProblemInstance import ProblemInstance


class VertexCoverProblemInstance(ProblemInstance):

    def __init__(self, p, input_graph, optimizer, num_starting_points, optimal_params=None, min_value=None,
                 most_likely_binary_solution=None, most_likely_solution_value=None):
        self.weight_operator = instances_generator.graph_weight_matrix_calculator.get_weight_matrix(input_graph)
        self.qubit_operator, self.offset = vertex_cover.get_operator(self.weight_operator)
        super().__init__("VertexCover", p, input_graph, self.weight_operator, optimizer,
                         num_starting_points, optimal_params, min_value, self.qubit_operator, self.offset,
                         most_likely_binary_solution, most_likely_solution_value)
