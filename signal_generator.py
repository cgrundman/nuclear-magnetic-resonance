from math import *
import numpy as np
import matplotlib.pyplot as plt


def generate_signal():
    # Create a random signal
    x = np.linspace(0, 1, 2000)  # TODO make range to be time related
    y = np.random.random((len(x), 1)) + 3
    z = np.sin(28 * x) + 1  # TODO set 28Hz frequency
    y[400] = 1  # TODO set y = 1 at certain points according to z
    return x, y, z


def plot(time, signal, sine_wave):
    # Plot the Signals
    plt.plot(time, signal)
    plt.plot(time, sine_wave)
    plt.ylim((0, 5))
    plt.show()


if __name__ == '__main__':
    t, b, n = generate_signal()
    plot(t, b, n)
