from qiskit.aqua.components.optimizers import COBYLA

from experiments.optimizers.Optimizer import Optimizer
from helpers.enums.OptimizerName import OptimizerName


class CobylaOptimizer(Optimizer):

    def __init__(self):
        super().__init__(COBYLA(), OptimizerName.COBYLA)
