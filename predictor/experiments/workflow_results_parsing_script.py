import json
import re
from os import listdir
from os.path import isfile, join

import networkx as nx

from experiments.problem_instances.instances_generators.graph_problems import graph_weight_matrix_calculator


def get_hash_table(data):
    hash_table = {}
    for step_id in data.keys():
        step_name = data[step_id]['stepName']
        hash_table[step_name] = step_id
    return hash_table


def get_best_solution(all_cases, case_id):
    optimizer_runs = 1250
    graph_id = 0  # max 0 because only 1 graph
    optimal_value = 0
    optimal_params = None
    # TODO problem with data while parsing random max p=3, key error
    for optimizer_run_id in range(optimizer_runs):
        # Get optimal values
        optimal_value = \
            all_cases[case_id]['optimization-results-aggregated'][str(graph_id)][str(optimizer_run_id)][
                "opt_value"][
                "value"]

        if optimal_value < optimal_value:
            optimal_value = optimal_value
            optimal_params = \
                all_cases[case_id]['optimization-results-aggregated'][str(graph_id)][str(optimizer_run_id)][
                    "opt_params"]["real"]

    return optimal_value, optimal_params


def is_solution_good_enough(best_value, current_value):
    return current_value <= 0.9 * best_value


def generate_json_with_params(data, problem_name, graph_type, p, json_name):
    save_path = "workflow_results_converted/" + problem_name + "/" + graph_type + "/" + "p=" + str(
        int(p)) + "/" + json_name
    with open(save_path, "w") as outfile:
        json.dump(data, outfile)


def generate_output_dictionary(optimal_params, min_value, good_params, optimizer_name, graph_type, p, weight_matrix,
                               problem):
    dic = {}
    dic["problem_name"] = problem
    dic["hamiltonian_matrix"] = []
    dic["weight_matrix"] = weight_matrix
    dic["optimal_params"] = optimal_params
    dic["min_value"] = min_value
    dic["most_likely_binary_solution"] = []
    dic["most_likely_solution_value"] = 1.0
    dic["classical_solution_value"] = 1.0
    dic["good_params"] = good_params
    dic["optimizer_name"] = optimizer_name
    dic["graph_type"] = graph_type
    dic["p"] = p

    return dic


if __name__ == '__main__':
    # we get 8 different graphs for a given probability and for each we initialize in 1250 erdos_renyi points
    problem = "partition"
    graph_type_name = "barbell"
    for p in range(1, 5):
        good_params = []
        directory = 'workflow_results/' + problem + '_' + graph_type_name + '_p=' + str(p) + '_results/'
        files = [file_name for file_name in listdir(directory) if isfile(join(directory, file_name))]

        for file in files:
            prob = re.split('=', re.split('\.', file)[0])[1] if graph_type_name == "random" else "0"
            raw_data = json.load(open(join(directory, file), 'r'))
            hash_table = get_hash_table(raw_data)

            all_cases = [case for _, case in raw_data.items()]

            optimizer_runs = 1250
            graph_id = 0  # max 0 because only 1 graph
            print(file)
            for case_id in range(len(all_cases)):  # max 7 because of 8 paralell runs
                optimal_value, optimal_params = get_best_solution(all_cases, case_id)

                graph_json_0 = all_cases[case_id]['graph-list'][str(graph_id)]['graph']
                optimal_solutions = all_cases[case_id]['graph-list'][str(graph_id)]['optimal_solution']

                graph = nx.readwrite.json_graph.node_link_graph(graph_json_0)
                weight_matrix = graph_weight_matrix_calculator.get_weight_matrix(graph)

                graph_specs = all_cases[case_id]['inputs']['graph_specs']['value']

                graph_type = graph_specs['type_graph']

                # Get optimizer data
                optimizer_specs = all_cases[case_id]['inputs']['optimizer_specs']['value']
                optimizer_name = optimizer_specs['method']

                for optimizer_run_id in range(optimizer_runs):
                    # Get optimal values
                    current_optimal_value = \
                        all_cases[case_id]['optimization-results-aggregated'][str(graph_id)][str(optimizer_run_id)][
                            "opt_value"][
                            "value"]

                    optimal_params = \
                        all_cases[case_id]['optimization-results-aggregated'][str(graph_id)][str(optimizer_run_id)][
                            "opt_params"][
                            "real"]

                    # Bitstrings from QAOA
                    bitstrings = \
                        all_cases[case_id]['bitstring-distributions-aggregated'][str(graph_id)][str(optimizer_run_id)][
                            'bitstring_distribution']

                    if is_solution_good_enough(optimal_value, current_optimal_value):
                        good_params.append(optimal_params)

                dict = generate_output_dictionary(optimal_params, optimal_value, good_params, optimizer_name,
                                                  graph_type, p,
                                                  weight_matrix.tolist(), problem)
                json_name = problem + "_" + graph_type + "_" + str(case_id) + "_" + "p=" + str(int(
                    p)) + "_" + optimizer_name + "_pr=" + prob
                generate_json_with_params(dict, problem, graph_type, p, json_name)
                print(len(good_params))
