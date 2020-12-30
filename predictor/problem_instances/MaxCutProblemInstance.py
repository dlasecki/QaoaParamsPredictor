from qiskit.optimization.applications.ising import max_cut

from instances_generator import graphs_builder
from problem_instances.ProblemInstance import ProblemInstance


class MaxCutProblemInstance(ProblemInstance):

    def __init__(self, problem_id, p, input_graph, optimizer, num_starting_points, optimal_params=None, min_value=None):
        self.weight_operator = graphs_builder.get_weight_matrix(input_graph)
        self.qubit_operator, self.offset = max_cut.get_operator(self.weight_operator)
        super().__init__(problem_id, "MaxCut", p, input_graph, optimizer, num_starting_points, optimal_params,
                         min_value, self.qubit_operator, self.offset)

