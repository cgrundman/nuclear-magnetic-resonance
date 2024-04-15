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
    HF_signal = np.random.rand(len(data_points)) + 3
    for n in range(len(data_points)):
        if .595 < LF_signal[n] < .605:
            HF_signal[n] = 1  # Set resonance
       
    return data_points, HF_signal, LF_signal

# TODO Plot High Frequency setting
def plot(time, signal, sine_wave, HF_setting):
    # Plot the Signals
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1)

    fig.suptitle(f"{HF_setting} MHz")

    ax1.plot(time, signal, color='lightcoral')
    ax1.set_title("NMR Signal")
    ax1.set_xlim((0, 0.1))
    ax1.grid(color='dimgrey')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    # ax1.set_grid(color='r', linestyle='-', linewidth=2)
    ax2.plot(time, sine_wave, color='deepskyblue')
    ax2.set_title("LF Signal")
    # ax2.set_ylim((0, 5))
    ax2.set_xlim((0, 0.1))
    ax2.grid(color='dimgrey')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    plt.savefig("figures/sample_signal.png")


if __name__ == '__main__':
    t, b, n = generate_signal()

    HF_setting = 18.5
    plot(t, b, n, HF_setting)

    print("Troubleshooting step")
