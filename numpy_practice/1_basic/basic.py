"""
Practicing basic numpy array & datatype use.

Numpy type guide
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
"""
import numpy as np
from numpy_practice.common import print_ndarray_stats
from numpy_practice.common import BASIC_1D_ARR
from numpy_practice.common import BASIC_2D_ARR
from numpy_practice.common import BASIC_5D_ARR
from numpy_practice.common import BASIC_NON_HOMOGENOUS_ARR
from numpy_practice.common import BASIC_HOMOGENOUS_ARR


def create_basic_arrays():
    """Attempt to create some basic numpy arrays. Invalid arguments will also be tried, and should raise an
    exception when used to initialize a numpy array. Reasons for these arguments being invalid include
    using inconsistent dimensions or mismatching types.
    """
    print("Showing four arrays: a 0D array (scalar), as well as a 1D, 2D, and 5D-array")
    arr_0d = np.array(42)
    print_ndarray_stats(arr_0d)

    arr_1d = np.array(BASIC_1D_ARR)
    print_ndarray_stats(arr_1d)

    arr_2d = np.array(BASIC_2D_ARR)
    print_ndarray_stats(arr_2d)

    arr_5d = np.array(BASIC_5D_ARR)
    print_ndarray_stats(arr_5d)

    print("Attempting to create arrays of homogenous and non-homogenous dimensions.")
    print("Homogenous Array:")
    arr_hom = np.array(BASIC_HOMOGENOUS_ARR)
    print_ndarray_stats(arr_hom)

    print("Non-homogenous Array:")
    try:
        arr_nhom = np.array(BASIC_NON_HOMOGENOUS_ARR)
        print_ndarray_stats(arr_nhom)
    except ValueError as exc:
        print("Value raised an exception when being used trying to create numpy array, as expected. Error was:")
        print(exc)


if __name__ == "__main__":
    create_basic_arrays()
