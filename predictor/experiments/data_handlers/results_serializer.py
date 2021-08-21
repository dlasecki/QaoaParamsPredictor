import json
import pathlib
from datetime import datetime

from data_structures.problem_instances.graph_problems.graph_problem_instance import ProblemInstance
from data_structures.problem_instances.result import Result


def save_to_json(directory: pathlib.Path, problem_instance: ProblemInstance, kernel=None, bandwidth=None):
    """Saves a given ProblemInstance as a json file to a given directory."""
    file_name = _create_problem_instance_file_name(
        problem_instance)
    if kernel is not None and bandwidth is not None:
        file_name += f"_{kernel}_bandwidth_{bandwidth}"
    result = _create_result(problem_instance)
    print(result)
    print(file_name)
    path = (directory).joinpath(file_name)
    print(path)
    with open(path, 'w') as outfile:
        json.dump(result.__dict__, outfile)


def _create_result(problem_instance: ProblemInstance):
    """Creates a Result object from ProblemInstance. Result object is a lighter version of a ProblemInstance."""
    optimizer_name = problem_instance.optimizer.optimizer_name.value if problem_instance.optimizer else None
    print(optimizer_name)
    most_likely_binary_solution = problem_instance.most_likely_binary_solution.tolist() if \
        problem_instance.most_likely_binary_solution is not None else None
    print(most_likely_binary_solution)
    return Result(problem_instance.problem_name.value, optimizer_name,
                  # complex_ndarray_to_list.complex_ndarray_to_matrix(problem_instance.hamiltonian_matrix),
                  None,
                  problem_instance.weight_matrix.tolist(), problem_instance.optimal_params.tolist(),
                  problem_instance.optimal_value, most_likely_binary_solution,
                  problem_instance.most_likely_solution_value, problem_instance.classical_solution_value.tolist(),
                  [np_array.tolist() for np_array in problem_instance.good_params],
                  problem_instance.input_graph.graph["graph_type"].value, problem_instance.p)


def _create_problem_instance_file_name(problem_instance: ProblemInstance):
    """Uses a ProblemInstance to create a related file name."""
    timestamp_str = datetime.now().strftime("%d-%b-%Y-%H-%M-%S.%f")
    optimizer_name_underscored = (
            problem_instance.optimizer.optimizer_name.value + "_") if problem_instance.optimizer else ""
    return problem_instance.problem_name.value + "_" + problem_instance.input_graph.graph[
        "graph_type"].value + "_" + str(problem_instance.input_graph.graph["graph_id"]) + "_" + "p=" + str(
        problem_instance.p) + "_" + optimizer_name_underscored + timestamp_str
