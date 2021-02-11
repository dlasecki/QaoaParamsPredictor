from enum import Enum


class OptimizerName(Enum):
    COBYLA = "cobyla"
    LBFGS = "lbfgs"
    SPSA = "spsa"
    NELDER_MEAD = "nelder_mead"
