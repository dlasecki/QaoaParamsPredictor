import json

from problem_instances.ProblemInstance import ProblemInstance
from problem_instances.Result import Result


def save_to_json(directory: str, data: ProblemInstance):
    file_name = data.problem_name + str(data.problem_id)
    result = __create_result(data)
    with open(directory + "\\" + file_name + ".json", 'w') as outfile:
        print(outfile)
        json.dump(result.__dict__, outfile)


def read_from_json(directory: str, file_name: str):
    path = directory + "\\" + file_name
    with open(path) as json_file:
        json_object = json.load(json_file)
    return json_object


def __create_result(problem_instance: ProblemInstance):
    return Result(problem_instance.problem_id, problem_instance.problem_name, problem_instance.optimal_params.tolist(),
                  problem_instance.min_value)
