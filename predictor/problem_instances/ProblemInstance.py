class ProblemInstance:

    def __init__(self, problem_id, problem_name, p, input_graph, optimizer, num_starting_points):
        self.problem_id = problem_id
        self.problem_name = problem_name
        self.p = p
        self.input_graph = input_graph
        self.optimizer = optimizer
        self.num_starting_points = num_starting_points

    def get_qaoa_operator(self):
        pass
