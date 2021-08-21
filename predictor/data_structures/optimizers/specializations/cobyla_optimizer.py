from qiskit.aqua.components.optimizers import COBYLA

from data_structures.enums.optimizer_name import OptimizerName
from data_structures.optimizers.optimizer import Optimizer


class CobylaOptimizer(Optimizer):

    def __init__(self):
        super().__init__(COBYLA(), OptimizerName.COBYLA)
