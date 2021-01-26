import problem_instances.instances_generator.graphs_builder as gg

from experiments.optimizers import optimizers_factory
from experiments.problem_instances.graph_problems.specializations.MaxCutProblemInstance import MaxCutProblemInstance
from qaoa_solver.qaoa import qaoa


def test_run_qaoa():
    problem_id = "1"
    p = 1
    input_graph = gg.generate_ladder_graph(3)
    optimizer = optimizers_factory.get_cobyla_optimizer()
    num_starting_points = 1

    problem_instance = MaxCutProblemInstance(problem_id, p, input_graph, optimizer, num_starting_points)
    result = qaoa(problem_instance)

    assert isinstance(result.min_value, float), "Optimal value not a float."
