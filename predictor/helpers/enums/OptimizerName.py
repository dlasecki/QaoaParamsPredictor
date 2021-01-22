from enum import Enum


class OptimizerName(Enum):
    COBYLA = "Cobyla"
    LBFGS = "Lbfgs"
    SPSA = "Spsa"
    NELDER_MEAD = "NelderMead"
