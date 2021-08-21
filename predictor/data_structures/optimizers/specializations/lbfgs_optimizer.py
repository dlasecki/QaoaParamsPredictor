from qiskit.aqua.components.optimizers import L_BFGS_B

from data_structures.enums.optimizer_name import OptimizerName
from data_structures.optimizers.optimizer import Optimizer


class LbfgsOptimizer(Optimizer):

    def __init__(self):
        super().__init__(L_BFGS_B(), OptimizerName.LBFGS)
