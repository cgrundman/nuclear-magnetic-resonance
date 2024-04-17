from math import *
import numpy as np
import matplotlib.pyplot as plt
import random



# TODO rename vaiables for clarity
# TODO make save signal as data
# TODO create searies of data through 16-20 MHz.
# TODO remove coefficients for peak decay, replace with automatic adjustment back to "normal"
def generate_signal(material, HF_actual):

    # Extract Material Properties
    resonances = material["Resonances"]
    peaks = material["Peaks"]

    # Create a random signal
    data_points = np.linspace(0, 0.1, 2000) # generate data points
    
    LF_signal = (np.sin(2 * pi * 28 * data_points) + 1)*.2  # set 28Hz frequency

    # Create Baseline Signal
    HF_signal = np.random.rand(len(data_points)) + 3

    # Chack for and Calculate resonances
    for i in range(len(resonances)):
        resonance = resonances[i]
        peak = peaks[i]
        for n in range(len(data_points)):
            if peak == 1:
                # Single Peak
                if resonance - .05 < LF_signal[n] + HF_actual < resonance + .05:
                    HF_signal[n] = random.random()/10 + 1 + 50*abs((resonance-HF_actual)-LF_signal[n])
            elif peak == 2:
            # Double Peak
                resonance_high = resonance + .05
                resonance_low = resonance - .05
                if resonance_high - .02 < LF_signal[n] + HF_actual < resonance_high + .02:
                    HF_signal[n] = random.random()/10 + 2 + 45*abs((resonance_high-HF_actual)-(LF_signal[n]))
                elif resonance_low - .02 < LF_signal[n] + HF_actual < resonance_low + .02:
                    HF_signal[n] = random.random()/10 + 2 + 45*abs((resonance_low-HF_actual)-(LF_signal[n]))
            # Triple Peak
            elif peak == 3:
                resonance_high = resonance + .05
                resonance_low = resonance - .05
                if resonance_high - .02 < LF_signal[n] + HF_actual < resonance_high + .02:
                    HF_signal[n] = random.random()/10 + 2.5 + 40*abs((resonance_high-HF_actual)-(LF_signal[n]))
                elif resonance_low - .02 < LF_signal[n] + HF_actual < resonance_low + .02:
                    HF_signal[n] = random.random()/10 + 2.5 + 40*abs((resonance_low-HF_actual)-(LF_signal[n]))
                elif resonance - .02 < LF_signal[n] + HF_actual < resonance + .02:
                    HF_signal[n] = random.random()/10 + 1.5 + 50*abs((resonance-HF_actual)-(LF_signal[n]))

    return data_points, HF_signal, LF_signal


def plot(time, NMR_signal, LF_signal, HF_setting, HF_actual, iteration):
    # Plot the Signals
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1)

    fig.suptitle(f"Setting: {HF_setting:.4f} MHz      Actual: {round(HF_actual, 4)} MHz")

    

    ax1.plot(time, NMR_signal, color='lightcoral')
    ax1.set_title("NMR Signal")
    ax1.set_xlim((0, 0.1))
    ax1.grid(color='dimgrey')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.set_ylim((0.5, 4.1))
    ax2.plot(time, LF_signal, color='deepskyblue')
    ax2.set_title("LF Signal")
    ax2.set_xlim((0, 0.1))
    ax2.grid(color='dimgrey')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    plt.savefig(f"full_sweep/material_sample_{iteration}.png")
    plt.close()


# TODO define materials with peak types and resonance points
if __name__ == '__main__':

    # Create Material
    material = {
        'Name': "Material 1",
        'Resonances': [16.5, 18, 19],
        'Peaks': [1, 2, 1]
    }

    # Looped Sweep
    HF_setting = 16
    iteration = 0
    while HF_setting < 20:

        HF_actual = HF_setting + ((random.random()-.5)/50)
        t, b, n = generate_signal(material, HF_actual)

        plot(t, b, n, HF_setting, HF_actual, iteration)

        HF_setting += .0625
        iteration += 1

    # # Single Iteration
    # resonance_frq = 1
    # HF_setting = 18.5
    # t, b, n = generate_signal(material, HF_setting)
    # plot(t, b, n, HF_setting, 1)
