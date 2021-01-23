from qiskit.aqua.components.optimizers import SPSA

from experiments.optimizers.Optimizer import Optimizer
from helpers.enums.OptimizerName import OptimizerName


class SpsaOptimizer(Optimizer):

    def __init__(self):
        super().__init__(SPSA(), OptimizerName.SPSA)
