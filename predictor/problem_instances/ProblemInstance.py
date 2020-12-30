from qiskit.aqua.operators import WeightedPauliOperator


class ProblemInstance:

    def __init__(self, problem_id, problem_name, p, input_graph, optimizer, num_starting_points, optimal_params,
                 min_value, qubit_operator : WeightedPauliOperator, offset):
        self.problem_id = problem_id
        self.problem_name = problem_name
        self.p = p
        self.input_graph = input_graph
        self.optimizer = optimizer
        self.num_starting_points = num_starting_points
        self.optimal_params = optimal_params
        self.min_value = min_value
        self.qubit_operator = qubit_operator
        self.offset = offset
