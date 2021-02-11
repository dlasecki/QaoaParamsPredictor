def validate_json_list_not_empty(jsons_list):
    number_of_instances_trained = len(jsons_list)
    if number_of_instances_trained == 0:
        raise Exception("Empty list of json files provided for KDE training.")


def validate_jsons(jsons_list):
    reference_problem_name, reference_graph_type, reference_p = __get_reference_metadata(jsons_list)
    for json in jsons_list:
        if __is_compliant_with_reference_json(reference_problem_name, reference_graph_type, reference_p, json):
            return False
    return True


def __get_reference_metadata(jsons_list):
    reference_json = jsons_list[0]
    problem_name = reference_json["problem_name"]
    graph_type = reference_json["graph_type"]
    p = reference_json["p"]

    return problem_name, graph_type, p


def __is_compliant_with_reference_json(reference_problem_name: str, reference_graph_type: str, reference_p: int, json):
    return reference_problem_name != json["problem_name"] or reference_graph_type != json[
        "graph_type"] or reference_p != json["p"]


def __get_model_metadata(jsons_list):
    number_of_instances_trained = len(jsons_list)
    problem_name, graph_type, p = __get_reference_metadata(jsons_list)
    return problem_name, graph_type, number_of_instances_trained, p
