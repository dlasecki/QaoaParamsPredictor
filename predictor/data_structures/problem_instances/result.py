class Result:
    """Class storing all information that are considered important results of an optimization."""

    def __init__(self, problem_name, optimizer_name, hamiltonian_matrix, weight_matrix, optimal_params, optimal_value,
                 most_likely_binary_solution, most_likely_solution_value, classical_solution_value, good_params,
                 graph_type, p):
        self.problem_name = problem_name

        self.optimizer_name = optimizer_name

        self.hamiltonian_matrix = hamiltonian_matrix

        self.weight_matrix = weight_matrix

        self.optimal_params = optimal_params

        self.optimal_value = optimal_value

        self.most_likely_binary_solution = most_likely_binary_solution

        self.most_likely_solution_value = most_likely_solution_value

        self.classical_solution_value = classical_solution_value

        self.good_params = good_params

        self.graph_type = graph_type

        self.p = p
