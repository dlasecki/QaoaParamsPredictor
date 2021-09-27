import unittest

from data_structures.enums.optimizer_name import OptimizerName
from data_structures.optimizers.optimizers_factory import create_optimizer
from data_structures.optimizers.specializations.cobyla_optimizer import CobylaOptimizer
from data_structures.optimizers.specializations.lbfgs_optimizer import LbfgsOptimizer
from data_structures.optimizers.specializations.nelder_mead_optimizer import NelderMeadOptimizer
from data_structures.optimizers.specializations.spsa_optimizer import SpsaOptimizer


class TestOptimizersFactory(unittest.TestCase):

    def test_create_optimizer_cobyla(self):
        optimizer = create_optimizer(OptimizerName.COBYLA)
        assert isinstance(optimizer, CobylaOptimizer)

    def test_create_optimizer_spsa(self):
        optimizer = create_optimizer(OptimizerName.SPSA)
        assert isinstance(optimizer, SpsaOptimizer)

    def test_create_optimizer_nelder_mead(self):
        optimizer = create_optimizer(OptimizerName.NELDER_MEAD)
        assert isinstance(optimizer, NelderMeadOptimizer)

    def test_create_optimizer_lbfgs(self):
        optimizer = create_optimizer(OptimizerName.LBFGS)
        assert isinstance(optimizer, LbfgsOptimizer)
