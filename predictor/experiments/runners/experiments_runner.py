import itertools
import multiprocessing
import pathlib
import time
from pathlib import Path

from data_structures.enums.optimizer_name import OptimizerName
from data_structures.enums.problem_name import ProblemName
from data_structures.optimizers import optimizers_factory
from data_structures.problem_instances.graph_problems.graph_problem_instance_factory import \
    create_graph_problem_instance
from data_structures.problem_instances.instances_generators.graph_problems.graphs_instances_generator import \
    generate_random_graph_instances, generate_ladder_graph_instances, generate_caveman_graph_instances, \
    generate_barbell_graph_instances
from experiments.data_handlers import results_serializer
from experiments.runners.base_runner import BaseRunner
from qaoa_solver import qaoa


class ExperimentsRunner(BaseRunner):
    """Class used for generating training data for ML models."""

    def worker(self, problem_name, input_graph, p_param, optimizer, initial_points_num):
        """Worker method for running QAOA algorithm for a given problem instance."""
        optimizer_instance = optimizers_factory.create_optimizer(optimizer)
        problem_instance = create_graph_problem_instance(problem_name, p_param, input_graph, optimizer_instance,
                                                         initial_points_num)
        qaoa_res = qaoa.qaoa_with_optimizer(problem_instance)
        directory = self._build_problem_instance_directory(problem_instance, problem_name)
        results_serializer.save_to_json(directory, qaoa_res)

        return qaoa_res.optimal_params, qaoa_res.optimal_value

    @staticmethod
    def _build_problem_instance_directory(problem_instance, problem_name):
        """Builds a file directory depending on the problem instance and problem name provided where a result of the
        worker method can be stored."""
        path = pathlib.Path(__file__).parent.resolve()
        directory = Path("../output", problem_name.value, problem_instance.input_graph.graph["graph_type"].value)
        full_path = (path).joinpath(directory)
        return full_path


if __name__ == '__main__':
    start = time.perf_counter()
    num_of_starting_points = [1]
    p_params = [1]
    problems = [ProblemName.MAX_CUT]
    NUM_OF_PROCESSES = 6
    optimizers = [OptimizerName.COBYLA]

    random_graph_num_of_vertices_train = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    random_graph_probabilities_train = [0.5, 0.6, 0.7, 0.8]

    ladder_graph_ladder_length_train = [4]

    caveman_graph_cliques_train = [(2, 4)]

    barbell_graph_num_of_vertices_train = [4]

    experiments_runner = ExperimentsRunner()

    inputs_random = experiments_runner._get_cartesian_product_of_inputs(problems, generate_random_graph_instances(
        random_graph_num_of_vertices_train, random_graph_probabilities_train), p_params,
                                                                        optimizers, num_of_starting_points)
    inputs_ladder = experiments_runner._get_cartesian_product_of_inputs(problems, generate_ladder_graph_instances(
        ladder_graph_ladder_length_train), p_params,
                                                                        optimizers, num_of_starting_points)
    inputs_caveman = experiments_runner._get_cartesian_product_of_inputs(problems, generate_caveman_graph_instances(
        caveman_graph_cliques_train), p_params,
                                                                         optimizers, num_of_starting_points)
    inputs_barbell = experiments_runner._get_cartesian_product_of_inputs(problems, generate_barbell_graph_instances(
        barbell_graph_num_of_vertices_train), p_params,
                                                                         optimizers, num_of_starting_points)
    inputs = itertools.chain(inputs_ladder)

    with multiprocessing.Pool(processes=NUM_OF_PROCESSES) as pool:
        results = pool.starmap(experiments_runner.worker, inputs)

    end = time.perf_counter()
    print(str(end - start) + " seconds")
