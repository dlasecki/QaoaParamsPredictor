def validate_json_list_not_empty(jsons_list):
    """Validates that list of json files provided for ML model training is not empty."""
    number_of_instances_trained = len(jsons_list)
    if number_of_instances_trained == 0:
        raise Exception("Empty list of json files provided for KDE training.")


def validate_jsons(jsons_list):
    """Validates that list of json files provided for ML model training all refer to the same problem instance."""
    reference_problem_name, reference_graph_type, reference_p = _get_reference_metadata(jsons_list)
    for json in jsons_list:
        if _is_compliant_with_reference_json(reference_problem_name, reference_graph_type, reference_p, json):
            return False
    return True


def _get_reference_metadata(jsons_list):
    """Gets metadata for a problem instance that the first json in the list refers to."""
    reference_json = jsons_list[0]
    problem_name = reference_json["problem_name"]
    graph_type = reference_json["graph_type"]
    p = reference_json["p"]

    return problem_name, graph_type, p


def _is_compliant_with_reference_json(reference_problem_name: str, reference_graph_type: str, reference_p: int, json):
    """Validates if a json file contains the same metadata as provided in arguments."""
    return reference_problem_name != json["problem_name"] or reference_graph_type != json[
        "graph_type"] or reference_p != json["p"]


def _get_model_metadata(jsons_list):
    """Gets metadata regarding a problem instance from the list of json files that should have been checked to be
    referring to the same problem instance."""
    number_of_instances_trained = len(jsons_list)
    problem_name, graph_type, p = _get_reference_metadata(jsons_list)
    return problem_name, graph_type, number_of_instances_trained, p
