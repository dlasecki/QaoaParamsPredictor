from qiskit.aqua.components.optimizers import L_BFGS_B

from experiments.optimizers.Optimizer import Optimizer
from helpers.enums.OptimizerName import OptimizerName


class LbfgsOptimizer(Optimizer):

    def __init__(self):
        super().__init__(L_BFGS_B(), OptimizerName.LBFGS)
