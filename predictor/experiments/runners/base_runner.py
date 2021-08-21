import itertools


class BaseRunner:
    """Base class for running experiments on data."""

    def _get_cartesian_product_of_inputs(self, problems, graph_instances_train_operators, p_params, bandwidths,
                                         kernels):
        return itertools.product(problems, graph_instances_train_operators, p_params, bandwidths, kernels)
