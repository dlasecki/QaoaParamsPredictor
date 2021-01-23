import json
from datetime import datetime

from helpers.converters import complex_ndarray_to_list
from problem_instances.Result import Result
from problem_instances.graph_problems.GraphProblemInstance import ProblemInstance


def save_to_json(directory: str, data: ProblemInstance):
    date_time_obj = datetime.now()
    timestamp_str = date_time_obj.strftime("%d-%b-%Y-%H-%M-%S.%f")
    file_name = data.problem_name.value + "_" + data.input_graph.graph["graph_type"].value + "_" + str(
        data.input_graph.graph["graph_id"]) + "_" + "p=" + str(data.p) + "_" + timestamp_str
    result = __create_result(data)
    with open(directory + "\\" + file_name + ".json", 'w') as outfile:
        print(outfile)
        json.dump(result.__dict__, outfile)


def __create_result(problem_instance: ProblemInstance):
    return Result(problem_instance.problem_name.value,
                  complex_ndarray_to_list.complex_ndarray_to_list(problem_instance.hamiltonian_matrix),
                  problem_instance.weight_matrix.tolist(), problem_instance.optimal_params.tolist(),
                  problem_instance.min_value, problem_instance.most_likely_binary_solution.tolist(),
                  problem_instance.most_likely_solution_value, problem_instance.classical_solution_value.tolist(),
                  [np_array.tolist() for np_array in problem_instance.good_params])
