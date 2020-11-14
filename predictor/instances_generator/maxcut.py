from qiskit.optimization.applications.ising import max_cut


def get_qaoa_operator(weight_matrix):
    return max_cut.get_operator(weight_matrix)