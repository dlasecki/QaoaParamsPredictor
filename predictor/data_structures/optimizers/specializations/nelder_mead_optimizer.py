from qiskit.aqua.components.optimizers import NELDER_MEAD

from data_structures.enums.optimizer_name import OptimizerName
from data_structures.optimizers.optimizer import Optimizer


class NelderMeadOptimizer(Optimizer):

    def __init__(self):
        super().__init__(NELDER_MEAD(), OptimizerName.NELDER_MEAD)
