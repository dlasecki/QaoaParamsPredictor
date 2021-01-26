import json
from datetime import datetime

from experiments.problem_instances.Result import Result
from experiments.problem_instances.graph_problems.GraphProblemInstance import ProblemInstance
from helpers.converters import complex_ndarray_to_list


def save_to_json(directory: str, problem_instance: ProblemInstance):
    file_name = __create_problem_instance_file_name(problem_instance)
    result = __create_result(problem_instance)
    with open(directory + "\\" + file_name + ".json", 'w') as outfile:
        print(outfile)
        json.dump(result.__dict__, outfile)


def __create_result(problem_instance: ProblemInstance):
    return Result(problem_instance.problem_name.value, problem_instance.optimizer.optimizer_name.value,
                  complex_ndarray_to_list.complex_ndarray_to_matrix(problem_instance.hamiltonian_matrix),
                  problem_instance.weight_matrix.tolist(), problem_instance.optimal_params.tolist(),
                  problem_instance.optimal_value, problem_instance.most_likely_binary_solution.tolist(),
                  problem_instance.most_likely_solution_value, problem_instance.classical_solution_value.tolist(),
                  [np_array.tolist() for np_array in problem_instance.good_params],
                  problem_instance.input_graph.graph["graph_type"].value, problem_instance.p)


def __create_problem_instance_file_name(problem_instance: ProblemInstance):
    timestamp_str = datetime.now().strftime("%d-%b-%Y-%H-%M-%S.%f")
    return problem_instance.problem_name.value + "_" + problem_instance.input_graph.graph[
        "graph_type"].value + "_" + str(problem_instance.input_graph.graph["graph_id"]) + "_" + "p=" + str(
        problem_instance.p) + "_" + problem_instance.optimizer.optimizer_name.value + "_" + timestamp_str
