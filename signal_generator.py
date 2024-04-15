from math import *
import numpy as np
import matplotlib.pyplot as plt
import random


# TODO connect resonance_frq to plot
# TODO rename vaiables for clarity
# TODO make save signal as data
# TODO create searies of data through 16-20 MHz.
def generate_signal(resonance_frq):
    # Create a random signal
    data_points = np.linspace(0, 0.1, 2000) # generate data points
    
    LF_signal = np.sin(2 * pi * 28 * data_points) + 1  # set 28Hz frequency

    # Conditionally set the y values
    HF_signal = np.random.rand(len(data_points)) + 3
    for n in range(len(data_points)):
        # Single Peak
        # if resonance_frq - .1 < LF_signal[n] < resonance_frq + .1:
        #     HF_signal[n] = random.random()/10 + 1 + 25*abs(resonance_frq-LF_signal[n])
        # Double Peak
        # resonance_high = resonance_frq + .25
        # resonance_low = resonance_frq - .25
        # if resonance_high - .1 < LF_signal[n] < resonance_high + .1:
        #     HF_signal[n] = random.random()/10 + 2 + 5*abs((resonance_high)-(LF_signal[n]))
        # elif resonance_low - .1 < LF_signal[n] < resonance_low + .1:
        #     HF_signal[n] = random.random()/10 + 2 + 5*abs((resonance_low)-(LF_signal[n]))
        # Triple Peak
        resonance_high = resonance_frq + .3
        resonance_low = resonance_frq - .3
        if resonance_high - .1 < LF_signal[n] < resonance_high + .1:
            HF_signal[n] = random.random()/10 + 2.5 + 5*abs((resonance_high)-(LF_signal[n]))
        elif resonance_low - .1 < LF_signal[n] < resonance_low + .1:
            HF_signal[n] = random.random()/10 + 2.5 + 5*abs((resonance_low)-(LF_signal[n]))
        elif resonance_frq - .1 < LF_signal[n] < resonance_frq + .1:
            HF_signal[n] = random.random()/10 + 1.5 + 7*abs((resonance_frq)-(LF_signal[n]))

    return data_points, HF_signal, LF_signal


def plot(time, NMR_signal, LF_signal, HF_setting):
    # Plot the Signals
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1)

    fig.suptitle(f"{HF_setting} MHz")

    ax1.plot(time, NMR_signal, color='lightcoral')
    ax1.set_title("NMR Signal")
    ax1.set_xlim((0, 0.1))
    ax1.grid(color='dimgrey')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.set_ylim((0.5, 4.1))
    ax2.plot(time, LF_signal, color='deepskyblue')
    ax2.set_title("LF Signal")
    # ax2.set_ylim((0, 5))
    ax2.set_xlim((0, 0.1))
    ax2.grid(color='dimgrey')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    plt.savefig("figures/sample_signal.png")


if __name__ == '__main__':
    resonance_frq = .6

    t, b, n = generate_signal(resonance_frq)

    HF_setting = 18.5
    plot(t, b, n, HF_setting)

    print("Troubleshooting step")
