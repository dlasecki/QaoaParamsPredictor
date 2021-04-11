from enum import Enum


class GraphType(Enum):
    BARBELL = "barbell"
    RANDOM = "erdos_renyi"
    LADDER = "ladder"
    CAVEMAN = "caveman"
