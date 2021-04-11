from enum import Enum


class OptimizerName(Enum):
    COBYLA = "cobyla"
    LBFGS = "L-BFGS-B"
    SPSA = "spsa"
    NELDER_MEAD = "nelder_mead"
