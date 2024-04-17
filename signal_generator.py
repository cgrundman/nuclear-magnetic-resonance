from math import *
import numpy as np
import matplotlib.pyplot as plt
import random



# TODO rename vaiables for clarity
# TODO make save signal as data
# TODO create searies of data through 16-20 MHz.
# TODO remove coefficients for peak decay, replace with automatic adjustment back to "normal"
def generate_signal(material, HF_setting):

    # Extract Material Properties
    resonances = material["Resonances"]

    # Create a random signal
    data_points = np.linspace(0, 0.1, 2000) # generate data points
    
    LF_signal = np.sin(2 * pi * 28 * data_points) + 1  # set 28Hz frequency

    # Create Baseline Signal
    HF_signal = np.random.rand(len(data_points)) + 3

    # Chack for and Calculate resonances
    for resonance in resonances:
        for n in range(len(data_points)):
            # Single Peak
            if resonance - .1 < LF_signal[n] + HF_setting < resonance + .1:
                HF_signal[n] = random.random()/10 + 1 + 25*abs((resonance-HF_setting)-LF_signal[n])
            # Double Peak
            # resonance_high = resonance + .25
            # resonance_low = resonance - .25
            # if resonance_high - .1 < LF_signal[n] + HF_setting < resonance_high + .1:
            #     HF_signal[n] = random.random()/10 + 2 + 10*abs((resonance_high-HF_setting)-(LF_signal[n]))
            # elif resonance_low - .1 < LF_signal[n] + HF_setting < resonance_low + .1:
            #     HF_signal[n] = random.random()/10 + 2 + 10*abs((resonance_low-HF_setting)-(LF_signal[n]))
            # Triple Peak
            # resonance_high = resonance + .3
            # resonance_low = resonance - .3
            # if resonance_high - .1 < LF_signal[n] + HF_setting < resonance_high + .1:
            #     HF_signal[n] = random.random()/10 + 2.5 + 5*abs((resonance_high-HF_setting)-(LF_signal[n]))
            # elif resonance_low - .1 < LF_signal[n] + HF_setting < resonance_low + .1:
            #     HF_signal[n] = random.random()/10 + 2.5 + 5*abs((resonance_low-HF_setting)-(LF_signal[n]))
            # elif resonance - .1 < LF_signal[n] + HF_setting < resonance + .1:
            #     HF_signal[n] = random.random()/10 + 1.5 + 7*abs((resonance-HF_setting)-(LF_signal[n]))

    return data_points, HF_signal, LF_signal

# TODO Plot the HF setting in with the same number of digits
def plot(time, NMR_signal, LF_signal, HF_setting, iteration):
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
    ax2.set_xlim((0, 0.1))
    ax2.grid(color='dimgrey')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    plt.savefig(f"figures/material_sample_{iteration}.png")
    plt.close()


# TODO define materials with pek types and resonance points
# TODO add randomness to the HF setting (intended vs measured)
if __name__ == '__main__':

    # Create Material
    material = {
        'Name': "Material 1",
        'Resonances': [16.5, 18, 19]
    }

    # Looped Sweep
    # for i in range(50):

    #     resonance_frq = i/20 - .25

    #     t, b, n = generate_signal(resonance_frq)

    #     HF_setting = 18 + i/40
    #     plot(t, b, n, HF_setting, i)

    # Single Iteration
    resonance_frq = 1
    HF_setting = 18.5
    t, b, n = generate_signal(material, HF_setting)
    
    plot(t, b, n, HF_setting, 1)

    print("Troubleshooting step")
