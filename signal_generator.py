from math import *
import numpy as np
import matplotlib.pyplot as plt


def generate_signal():
    # Create a random signal
    x = list(range(0, 2000, 1)) # TODO make range to be time related
    y = np.random.random((len(x), 1)) + 3
    z = np.sin(x) + 1 # TODO set 28Hz frequency
    y[400] = 1
    return y, z


def plot(signal, sine_wave):
    # Plot the Signals
    plt.plot(signal)
    plt.plot(sine_wave)
    plt.ylim((0, 5))
    plt.show()


if __name__ == '__main__':
    b, t = generate_signal()
    plot(b, t)
