from enum import Enum


class OptimizerName(Enum):
    """Enum containing possible optimizer names."""
    COBYLA = "cobyla"
    LBFGS = "L-BFGS-B"
    SPSA = "spsa"
    NELDER_MEAD = "nelder_mead"
