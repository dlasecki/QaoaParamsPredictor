from qiskit.aqua.components.optimizers import SPSA

from experiments.optimizers.optimizer import Optimizer
from helpers.enums.optimizer_name import OptimizerName


class SpsaOptimizer(Optimizer):

    def __init__(self):
        super().__init__(SPSA(), OptimizerName.SPSA)
