class Result:

    def __init__(self, problem_name, optimizer_name, hamiltonian_matrix, weight_matrix, optimal_params, min_value,
                 most_likely_binary_solution, most_likely_solution_value, classical_solution_value, good_params):
        self.problem_name = problem_name
        self.optimizer_name = optimizer_name
        self.hamiltonian_matrix = hamiltonian_matrix
        self.weight_matrix = weight_matrix
        self.optimal_params = optimal_params
        self.min_value = min_value
        self.most_likely_binary_solution = most_likely_binary_solution
        self.most_likely_solution_value = most_likely_solution_value
        self.classical_solution_value = classical_solution_value
        self.good_params = good_params
