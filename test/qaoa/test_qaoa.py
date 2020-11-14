import instances_generator.graphs_generator as gg
from qaoa_solver.qaoa import qaoa


def test_run_qaoa():
    ladder_graph = gg.generate_ladder_graph(3)
    ladder_graph_weight_matrix = gg.get_weight_matrix(ladder_graph)
    result = qaoa(ladder_graph_weight_matrix, 3)
    print(result.get_optimal_cost())
    print(result.optimal_params)
    print(result.var_form)