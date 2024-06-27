import numpy as np
from math import *


# Generate the nmr signal
def nmr_signal_generator():
    # Set number of data points
    data_points = np.linspace(0, 5/28, 2000)

    # Create the lf signal
    lf_signal = (np.sin(2 * pi * 28 * data_points - pi/2) + 1)*.2

    # Create the nmr signal
    nmr_signal = np.random.rand(len(data_points))

    return data_points, lf_signal, nmr_signal
