from enum import Enum


class GraphType(Enum):
    """Enum containing possible graph types."""
    BARBELL = "barbell"
    RANDOM = "erdos_renyi"
    LADDER = "ladder"
    CAVEMAN = "caveman"
