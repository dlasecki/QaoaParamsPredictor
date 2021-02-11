from qiskit.aqua.components.optimizers import NELDER_MEAD

from experiments.optimizers.optimizer import Optimizer
from helpers.enums.optimizer_name import OptimizerName


class NelderMeadOptimizer(Optimizer):

    def __init__(self):
        super().__init__(NELDER_MEAD(), OptimizerName.NELDER_MEAD)
