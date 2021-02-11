from qiskit.aqua.components.optimizers import L_BFGS_B

from experiments.optimizers.optimizer import Optimizer
from helpers.enums.optimizer_name import OptimizerName


class LbfgsOptimizer(Optimizer):

    def __init__(self):
        super().__init__(L_BFGS_B(), OptimizerName.LBFGS)
