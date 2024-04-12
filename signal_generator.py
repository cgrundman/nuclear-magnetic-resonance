from math import *
import numpy as np
import matplotlib.pyplot as plt


def generate_signal():
    # Create a random signal
    x = np.linspace(0, 1, 2000)
    
    z = np.sin(28 * x) + 1  # set 28Hz frequency

    # Conditionally set the y values
    for n in range(len(x)):
        if 1.5 < (np.sin(28 * n) + 1)/2000 < 1.6:
            y[n] = 1  # TODO set y = 1 at certain points according to z
        else: 
            y = np.random.random((len(x), 1)) + 3

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
