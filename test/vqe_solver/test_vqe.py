import instances_generator.graphs_generator as gg
import vqe_solver.vqe as qm
from instances_generator import maxcut


def test_run_vqe():
    ladder_graph = gg.generate_ladder_graph(2)
    ladder_graph_weight_matrix = gg.get_weight_matrix(ladder_graph)
    ladder_graph_qubit_operator, offset = maxcut.get_qaoa_operator(ladder_graph_weight_matrix)
    repetitions = 5
    max_iterations = 30
    result = qm.run_vqe(ladder_graph_qubit_operator, repetitions, max_iterations)
    assert isinstance(result.get("optimal_value"), float), "Optimal value not a float."
