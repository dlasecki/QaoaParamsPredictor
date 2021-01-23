from helpers.enums.OptimizerName import OptimizerName


class Optimizer:

    def __init__(self, optimizer, optimizer_name: OptimizerName):
        self.optimizer = optimizer
        self.optimizer_name = optimizer_name
