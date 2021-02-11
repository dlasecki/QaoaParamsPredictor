from experiments.optimizers.specializations.cobyla_optimizer import CobylaOptimizer
from experiments.optimizers.specializations.lbfgs_optimizer import LbfgsOptimizer
from experiments.optimizers.specializations.nelder_mead_optimizer import NelderMeadOptimizer
from experiments.optimizers.specializations.spsa_optimizer import SpsaOptimizer
from helpers.enums.optimizer_name import OptimizerName


def create_optimizer(optimizer_name: OptimizerName):
    if optimizer_name == OptimizerName.COBYLA:
        return CobylaOptimizer()
    elif optimizer_name == OptimizerName.SPSA:
        return SpsaOptimizer()
    elif optimizer_name == OptimizerName.NELDER_MEAD:
        return NelderMeadOptimizer()
    elif optimizer_name == OptimizerName.LBFGS:
        return LbfgsOptimizer()
