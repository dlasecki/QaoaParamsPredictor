from qiskit.optimization.applications.ising import max_cut
from instances_generator import graphs_builder


def get_qaoa_operator(weight_matrix):
    return max_cut.get_operator(weight_matrix)


def generate_instances_operators(instances):
    operators = []
    for instance in instances:
        weight_matrix = graphs_builder.get_weight_matrix(instance)
        qubit_operator, offset = get_qaoa_operator(weight_matrix)
        operators.append(qubit_operator)
    return operators
