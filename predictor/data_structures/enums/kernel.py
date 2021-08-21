from enum import Enum


class Kernel(Enum):
    """Enum containing possible kernels for Kernel Density Estimation."""
    GAUSSIAN = "gaussian"
    TOPHAT = "tophat"
    EPANECHNIKOV = "epanechnikov"
    EXPONENTIAL = "exponential"
    LINEAR = "linear"
    COSINE = "cosine"
