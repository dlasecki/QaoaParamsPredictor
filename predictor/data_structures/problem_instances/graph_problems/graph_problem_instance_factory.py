from data_structures.enums.problem_name import ProblemName
from data_structures.optimizers.optimizer import Optimizer
from data_structures.problem_instances.graph_problems.specializations.graph_partition_problem_instance import \
    GraphPartitionProblemInstance
from data_structures.problem_instances.graph_problems.specializations.maxcut_problem_instance import \
    MaxCutProblemInstance
from data_structures.problem_instances.graph_problems.specializations.stable_set_problem_instance import \
    StableSetProblemInstance
from data_structures.problem_instances.graph_problems.specializations.vertex_cover_problem_instance import \
    VertexCoverProblemInstance


def create_graph_problem_instance(problem_name, p_param, input_graph, optimizer: Optimizer = None,
                                  initial_points_num=None, initial_points=None):
    if problem_name == ProblemName.MAX_CUT:
        return MaxCutProblemInstance(p_param, input_graph, optimizer, initial_points_num)
    elif problem_name == ProblemName.GRAPH_PARTITION:
        return GraphPartitionProblemInstance(p_param, input_graph, optimizer, initial_points_num)
    elif problem_name == ProblemName.STABLE_SET:
        return StableSetProblemInstance(p_param, input_graph, optimizer, initial_points_num)
    elif problem_name == ProblemName.VERTEX_COVER:
        return VertexCoverProblemInstance(p_param, input_graph, optimizer, initial_points_num)
