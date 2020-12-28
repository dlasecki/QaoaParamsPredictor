from qiskit.aqua.components.optimizers import COBYLA

import instances_generator.graphs_builder as gg
from qaoa_solver.qaoa import qaoa


def test_run_qaoa():
    ladder_graph = gg.generate_ladder_graph(3)
    optimizer = COBYLA()
    result = qaoa(ladder_graph_qubit_operator, 3, optimizer)
    print(result.get_optimal_cost())
    print(result.optimal_params)
    print(result.var_form)
    assert isinstance(result.get_optimal_cost(), float), "Optimal value not a float."