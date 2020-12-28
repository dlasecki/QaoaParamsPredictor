from qiskit.optimization.applications.ising import max_cut

from instances_generator import graphs_builder
from problem_instances.ProblemInstance import ProblemInstance


class MaxCutProblemInstance(ProblemInstance):

    def __init__(self, problem_id, p, input_graph, optimizer, num_starting_points):
        super().__init__(problem_id, "MaxCut", p, input_graph, optimizer, num_starting_points)
        self.weight_operator = graphs_builder.get_weight_matrix(input_graph)

    def get_qaoa_operator(self):
        qubit_operator, offset = max_cut.get_operator(self.weight_operator)
        return qubit_operator