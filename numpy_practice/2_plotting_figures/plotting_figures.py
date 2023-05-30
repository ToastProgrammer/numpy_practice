"""
Using matplotlib to graph different sets and types of data
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from numpy_practice.common import create_simple_plot
from numpy_practice.common import BASIC_1D_ARR


def main():
    arr: np.array
    arr2: np.array
    fig: Figure
    axe: Axes
    arr: np.array = np.array(BASIC_1D_ARR)
    arr2: np.array = np.array((5,5,5,6))
    fig, axe = create_simple_plot([arr, arr2], )
    plt.show()


if __name__ == "__main__":
    main()
