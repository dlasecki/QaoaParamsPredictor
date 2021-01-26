from math import sqrt

from numpy.core.multiarray import ndarray


def complex_ndarray_to_matrix(array: ndarray):
    elements = len(array)
    dimension = sqrt(elements)
    assert dimension == int(dimension)
    dimension = int(dimension)
    matrix = []
    array = array.reshape((dimension, dimension))
    for row_ind in range(dimension):
        row = []
        for col_ind in range(dimension):
            row.append((array[row_ind][col_ind].real, array[row_ind][col_ind].imag))
        matrix.append(row)
    return matrix
