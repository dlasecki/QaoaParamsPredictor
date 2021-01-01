class Result:

    def __init__(self, problem_id, problem_name, hamiltonian_matrix, optimal_params, min_value):
        self.problem_id = problem_id
        self.problem_name = problem_name
        self.hamiltonian_matrix = hamiltonian_matrix
        self.optimal_params = optimal_params
        self.min_value = min_value
