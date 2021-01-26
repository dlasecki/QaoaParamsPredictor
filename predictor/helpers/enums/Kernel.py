from enum import Enum


class Kernel(Enum):
    GAUSSIAN = "gaussian"
    TOPHAT = "tophat"
    EPANECHNIKOV = "epanechnikov"
    EXPONENTIAL = "exponential"
    LINEAR = "linear"
    COSINE = "cosine"
