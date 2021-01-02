from qiskit.aqua.components.optimizers import COBYLA, L_BFGS_B, NELDER_MEAD, SPSA


def get_cobyla_optimizer():
    return COBYLA()


def get_lbfgs_optimizer():
    return L_BFGS_B()


def get_nelder_mead_optimizer():
    return NELDER_MEAD()

def get_spsa_optimizer():
    return SPSA()