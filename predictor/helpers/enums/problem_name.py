from enum import Enum


class ProblemName(Enum):
    """Enum containing possible graph problems."""
    GRAPH_PARTITION = "graph_partition"
    MAX_CUT = "max_cut"
    STABLE_SET = "stable_set"
    VERTEX_COVER = "vertex_cover"
