from experiments.optimizers.optimizers_factory import create_optimizer
from experiments.problem_instances.graph_problems.specializations.maxcut_problem_instance import MaxCutProblemInstance
from experiments.problem_instances.instances_generators.graph_problems.graphs_builder import generate_ladder_graph
from helpers.enums import optimizer_name
from qaoa_solver.qaoa import qaoa_with_optimizer


def test_run_qaoa():
    p = 1
    input_graph = generate_ladder_graph(3, 1)
    optimizer = create_optimizer(optimizer_name.OptimizerName.COBYLA)
    num_starting_points = 1

    problem_instance = MaxCutProblemInstance(p, input_graph, optimizer, num_starting_points)
    result = qaoa_with_optimizer(problem_instance)

    assert isinstance(result.optimal_value, float), "Optimal value not a float."
