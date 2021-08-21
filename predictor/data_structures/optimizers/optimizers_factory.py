from data_structures.enums.optimizer_name import OptimizerName
from data_structures.optimizers.specializations.cobyla_optimizer import CobylaOptimizer
from data_structures.optimizers.specializations.lbfgs_optimizer import LbfgsOptimizer
from data_structures.optimizers.specializations.nelder_mead_optimizer import NelderMeadOptimizer
from data_structures.optimizers.specializations.spsa_optimizer import SpsaOptimizer


def create_optimizer(optimizer_name: OptimizerName):
    """Factory producing a corresponding optimizer."""
    if optimizer_name == OptimizerName.COBYLA:
        return CobylaOptimizer()
    elif optimizer_name == OptimizerName.SPSA:
        return SpsaOptimizer()
    elif optimizer_name == OptimizerName.NELDER_MEAD:
        return NelderMeadOptimizer()
    elif optimizer_name == OptimizerName.LBFGS:
        return LbfgsOptimizer()
