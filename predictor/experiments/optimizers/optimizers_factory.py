from experiments.optimizers.specializations.CobylaOptimizer import CobylaOptimizer
from experiments.optimizers.specializations.LbfgsOptimizer import LbfgsOptimizer
from experiments.optimizers.specializations.NelderMeadOptimizer import NelderMeadOptimizer
from experiments.optimizers.specializations.SpsaOptimizer import SpsaOptimizer
from helpers.enums.OptimizerName import OptimizerName


def create_optimizer(optimizer_name: OptimizerName):
    if optimizer_name == OptimizerName.COBYLA:
        return CobylaOptimizer()
    elif optimizer_name == OptimizerName.SPSA:
        return SpsaOptimizer()
    elif optimizer_name == OptimizerName.NELDER_MEAD:
        return NelderMeadOptimizer()
    elif optimizer_name == OptimizerName.LBFGS:
        return LbfgsOptimizer()
