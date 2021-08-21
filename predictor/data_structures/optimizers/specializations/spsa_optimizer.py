from qiskit.aqua.components.optimizers import SPSA

from data_structures.enums.optimizer_name import OptimizerName
from data_structures.optimizers.optimizer import Optimizer


class SpsaOptimizer(Optimizer):

    def __init__(self):
        super().__init__(SPSA(), OptimizerName.SPSA)
