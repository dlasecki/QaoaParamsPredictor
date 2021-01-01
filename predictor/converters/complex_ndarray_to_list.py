from numpy.core.multiarray import ndarray


def complex_ndarray_to_list(array: ndarray):
    flat_list = []
    for i in range(len(array)):
        flat_list.append(array[i].real)
        flat_list.append(array[i].imag)
    return flat_list
