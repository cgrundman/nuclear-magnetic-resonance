from math import *
import numpy as np
import matplotlib.pyplot as plt
import random

# TODO input peak point from outside of function
# TODO make double and triple peaks
# TODO make more realistic peak
def generate_signal():
    # Create a random signal
    data_points = np.linspace(0, 0.1, 2000) # generate data points
    
    LF_signal = np.sin(2 * pi * 28 * data_points) + 1  # set 28Hz frequency

    # Conditionally set the y values
    HF_signal = np.zeros(len(data_points))
    for n in range(len(data_points)):
        if .495 < LF_signal[n] < .505:
            HF_signal[n] = 1  # Set resonance
        else: 
            HF_signal[n] = random.random() + 3 # set random values

    return data_points, HF_signal, LF_signal

def plot(time, signal, sine_wave):
    # Plot the Signals
    plt.plot(time, signal)
    plt.plot(time, sine_wave)
    plt.ylim((0, 5))
    plt.xlim((0, 0.1))
    plt.show()


if __name__ == '__main__':
    t, b, n = generate_signal()
    plot(t, b, n)

    print("Troubleshooting step")
