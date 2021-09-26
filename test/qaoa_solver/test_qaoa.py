import unittest

from data_structures.enums import optimizer_name
from data_structures.optimizers.test_optimizers_factory import create_optimizer
from data_structures.problem_instances.graph_problems.specializations.test_maxcut_problem_instance import \
    MaxCutProblemInstance
from data_structures.problem_instances.instances_generators.graph_problems.test_graphs_builder import \
    generate_ladder_graph
from qaoa_solver.qaoa import qaoa_with_optimizer


class TestQaoa(unittest.TestCase):
    def test_run_qaoa(self):
        p = 1
        input_graph = generate_ladder_graph(3, 1)
        optimizer = create_optimizer(optimizer_name.OptimizerName.COBYLA)
        num_starting_points = 1

        problem_instance = MaxCutProblemInstance(p, input_graph, optimizer, num_starting_points)
        result = qaoa_with_optimizer(problem_instance)

        assert isinstance(result.optimal_value, float), "Optimal value not a float."
