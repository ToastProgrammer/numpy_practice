import numpy as np
import matplotlib.pyplot as ppl
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from typing import Union, Tuple, Iterable, List


BASIC_1D_ARR = (8, 6, 7, 5, 3, 0, 9)
BASIC_2D_ARR = ((3, 1, 4), (1, 5, 9))
BASIC_5D_ARR = (
    ((1,), (2,)),
    ((3,), (4,))
)
BASIC_NON_HOMOGENOUS_ARR = (
    1, (21, 22),
    (31, (321, 322)),
    (41, (421,))
)
BASIC_HOMOGENOUS_ARR = (
    ((111, 112), (121, 122)),
    ((211, 212), (221, 222)),
    ((311, 312), (321, 322)),
    ((411, 412), (421, 422))
)


def make_array_base(size: Union[int, Tuple[int, int]]):
    return np.array(size)


def print_ndarray_stats(arr: np.ndarray) -> None:
    # If the array is a scalar, arr.shape returns an empty tuple
    if not arr.shape:
        print(f"Array is a scalar value")
    else:
        # print(f"Array has dimensions of size {', '.join(str(i) for i in arr.shape)}")
        print(f"Array has dimensions of size {', '.join(map(str, arr.shape))}")
    print(arr)
    print(f"{'':*>48}")


def create_simple_plot(arrs: Iterable[np.array]) -> Tuple[ppl.figure, Union[Axes, List[Axes]]]:

    fig, axe = ppl.subplots()
    for arr in arrs:
        axe.plot(arr)
    return fig, axe
