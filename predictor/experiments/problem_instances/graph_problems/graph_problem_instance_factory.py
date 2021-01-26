from experiments.optimizers.Optimizer import Optimizer
from experiments.problem_instances.graph_problems.specializations.GraphPartitionProblemInstance import \
    GraphPartitionProblemInstance
from experiments.problem_instances.graph_problems.specializations.MaxCutProblemInstance import MaxCutProblemInstance
from experiments.problem_instances.graph_problems.specializations.StableSetProblemInstance import \
    StableSetProblemInstance
from experiments.problem_instances.graph_problems.specializations.VertexCoverProblemInstance import \
    VertexCoverProblemInstance
from helpers.enums.ProblemName import ProblemName


def create_graph_problem_instance(problem_name, p_param, input_graph, optimizer: Optimizer, initial_points_num):
    if problem_name == ProblemName.MAX_CUT:
        return MaxCutProblemInstance(p_param, input_graph, optimizer, initial_points_num)
    elif problem_name == ProblemName.GRAPH_PARTITION:
        return GraphPartitionProblemInstance(p_param, input_graph, optimizer, initial_points_num)
    elif problem_name == ProblemName.STABLE_SET:
        return StableSetProblemInstance(p_param, input_graph, optimizer, initial_points_num)
    elif problem_name == ProblemName.VERTEX_COVER:
        return VertexCoverProblemInstance(p_param, input_graph, optimizer, initial_points_num)
