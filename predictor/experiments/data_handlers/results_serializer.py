import json
from datetime import datetime

from experiments.problem_instances.graph_problems.graph_problem_instance import ProblemInstance
from experiments.problem_instances.result import Result
from helpers.converters import complex_ndarray_to_list


def save_to_json(directory: str, problem_instance: ProblemInstance):
    file_name = _create_problem_instance_file_name(problem_instance)
    result = _create_result(problem_instance)
    with open(directory + "\\" + file_name + ".json", 'w') as outfile:
        print(outfile)
        json.dump(result.__dict__, outfile)


def _create_result(problem_instance: ProblemInstance):
    optimizer_name = problem_instance.optimizer.optimizer_name.value if problem_instance.optimizer else None
    most_likely_binary_solution = problem_instance.most_likely_binary_solution.tolist() if problem_instance.most_likely_binary_solution else None
    return Result(problem_instance.problem_name.value, optimizer_name,
                  complex_ndarray_to_list.complex_ndarray_to_matrix(problem_instance.hamiltonian_matrix),
                  problem_instance.weight_matrix.tolist(), problem_instance.optimal_params.tolist(),
                  problem_instance.optimal_value, most_likely_binary_solution,
                  problem_instance.most_likely_solution_value, problem_instance.classical_solution_value.tolist(),
                  [np_array.tolist() for np_array in problem_instance.good_params],
                  problem_instance.input_graph.graph["graph_type"].value, problem_instance.p)


def _create_problem_instance_file_name(problem_instance: ProblemInstance):
    timestamp_str = datetime.now().strftime("%d-%b-%Y-%H-%M-%S.%f")
    optimizer_name_underscored = (
            problem_instance.optimizer.optimizer_name.value + "_") if problem_instance.optimizer else ""
    return problem_instance.problem_name.value + "_" + problem_instance.input_graph.graph[
        "graph_type"].value + "_" + str(problem_instance.input_graph.graph["graph_id"]) + "_" + "p=" + str(
        problem_instance.p) + "_" + optimizer_name_underscored + timestamp_str
