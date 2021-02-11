from qiskit.aqua.components.optimizers import COBYLA

from experiments.optimizers.optimizer import Optimizer
from helpers.enums.optimizer_name import OptimizerName


class CobylaOptimizer(Optimizer):

    def __init__(self):
        super().__init__(COBYLA(), OptimizerName.COBYLA)
