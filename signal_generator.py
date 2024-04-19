from math import *
import numpy as np
import matplotlib.pyplot as plt
import random
import json


# TODO remove coefficients for peak decay, replace with automatic adjustment back to "normal"
def generate_signal(material, HF_actual):

    # Extract Material Properties
    resonances = material["Resonances"]
    peaks = material["Peaks"]

    # Create a random signal
    data_points = np.linspace(0, 5/28, 2000) # generate data points
    
    LF_signal = (np.sin(2 * pi * 28 * data_points - pi/2) + 1)*.2  # set 28Hz frequency

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


def trim_signal(time, NMR_signal, LF_signal):

    # Create trim ranges
    idx_points = np.zeros([2,5])
    i, j = 0, 0
    for n in range(len(LF_signal)):
        if LF_signal[n-1]<=.1 and LF_signal[n]>=.1:
            idx_points[0,i] = np.where(time==time[n])[0]
            i += 1
        if LF_signal[n-1]<=.3 and LF_signal[n]>=.3:
            idx_points[1,j] = np.where(time==time[n])[0]
            j += 1

    LF_trimmed = []
    NMR_trimmed =  []
    for i in range(len(idx_points[0,:])):
        min_idx = int(idx_points[0,i])
        max_idx = int(idx_points[1,i])
        LF_trimmed = np.append(LF_trimmed, LF_signal[min_idx:max_idx])
        NMR_trimmed = np.append(NMR_trimmed, NMR_signal[min_idx:max_idx])
    time_trimmed = time[:int(len(NMR_trimmed))]

    return time_trimmed, NMR_trimmed, LF_trimmed


def save_signal(NMR, LF, set_point):

    # Save signals to JSON
    set_point = int(set_point*10000) 
    np.savetxt(f"data/{set_point}_nmr.txt", NMR)
    np.savetxt(f"data/{set_point}_lf.txt", LF)


def sweep(material):
    # Looped Sweep
    HF_setting = 16
    iteration = 0
    while HF_setting <= 20:

        # Create actual HF signal setting
        HF_actual = HF_setting + ((random.random()-.5)/50)

        # Generate the signal for current settings
        time, NMR_signal, LF_signal = generate_signal(material, HF_actual)

        # Plot
        # plot(time, NMR_signal, LF_signal, HF_setting, HF_actual)
        # plot_regions(time, NMR_signal, LF_signal, HF_setting, HF_actual)
        # plot_trimmed(time, NMR_signal, LF_signal, HF_setting, HF_actual)

        # Trim the signal for usable parts
        time_trimmed, NMR_trimmed, LF_trimmed = trim_signal(time, NMR_signal, LF_signal)

        save_signal(NMR_trimmed, LF_trimmed, HF_actual)

        print(len(time_trimmed))
        print(len(NMR_trimmed))
        print(len(LF_trimmed))

        HF_setting += .03125
        iteration += 1

    return "Sweep Complete"


def plot_trimmed(time, NMR_signal, LF_signal, HF_setting, HF_actual):

    # Create trim ranges
    idx_points = np.zeros([2,5])
    i, j = 0, 0
    for n in range(len(LF_signal)):
        if LF_signal[n-1]<=.1 and LF_signal[n]>=.1:
            idx_points[0,i] = np.where(time==time[n])[0]
            i += 1
        if LF_signal[n-1]<=.3 and LF_signal[n]>=.3:
            idx_points[1,j] = np.where(time==time[n])[0]
            j += 1

    LF_trimmed = []
    NMR_trimmed =  []
    for i in range(len(idx_points[0,:])):
        min_idx = int(idx_points[0,i])
        max_idx = int(idx_points[1,i])
        LF_trimmed = np.append(LF_trimmed, LF_signal[min_idx:max_idx])
        NMR_trimmed = np.append(NMR_trimmed, NMR_signal[min_idx:max_idx])
    time_trimmed = time[:int(len(NMR_trimmed))]

    # Plot the Signals
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle(f"Setting: {HF_setting:.4f} MHz      Actual: {round(HF_actual, 4)} MHz")

    # Subplot 1
    ax1.plot(time_trimmed, NMR_trimmed, color='lightcoral')
    ax1.set_title("NMR Signal")
    ax1.grid(color='dimgrey')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.set_xlim((0, time_trimmed[-1]))
    ax1.set_ylim((0.5, 4.1))

    # Subplot 2
    ax2.plot(time_trimmed, LF_trimmed, color='deepskyblue')
    ax2.set_title("LF Signal")
    ax2.grid(color='dimgrey')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.set_xlim((0, time_trimmed[-1]))
    
    # Save and close plot
    plt.savefig(f"figures/trimmed_data.png")
    plt.close()


def plot_regions(time, NMR_signal, LF_signal, HF_setting, HF_actual):
    
    # Plot the Signals
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle(f"Setting: {HF_setting:.4f} MHz      Actual: {round(HF_actual, 4)} MHz")

    # Subplot 1
    ax1.plot(time, NMR_signal, color='lightcoral')
    ax1.set_title("NMR Signal")
    ax1.grid(color='dimgrey')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    
    ax1.set_xlim((0, 5/28))
    ax1.set_ylim((0.5, 4.1))

    # Subplot 2
    ax2.plot(time, LF_signal, color='deepskyblue')
    ax2.set_title("LF Signal")
    ax2.grid(color='dimgrey')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.set_xlim((0, 5/28))

    # Create highlighted ranges
    range_points = np.zeros([2,5])
    i, j = 0, 0
    for n in range(len(LF_signal)):
        if LF_signal[n-1]<=.1 and LF_signal[n]>=.1:
            range_points[0,i] = time[n]
            i += 1
        if LF_signal[n-1]<=.3 and LF_signal[n]>=.3:
            range_points[1,j] = time[n]
            j += 1
    for i in range(len(range_points[0,:])):
        ax1.axvspan(range_points[0,i], range_points[1,i], color='yellow', alpha=0.5)
        ax2.axvspan(range_points[0,i], range_points[1,i], color='yellow', alpha=0.5)

    # Save and close plot
    plt.savefig(f"figures/highlighted_data.png")
    plt.close()


def plot(time, NMR_signal, LF_signal, HF_setting, HF_actual):
    
    # Plot the Signals
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle(f"Setting: {HF_setting:.4f} MHz      Actual: {round(HF_actual, 4)} MHz")

    # Subplot 1
    ax1.plot(time, NMR_signal, color='lightcoral')
    ax1.set_title("NMR Signal")
    ax1.grid(color='dimgrey')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    
    ax1.set_xlim((0, 5/28))
    ax1.set_ylim((0.5, 4.1))

    # Subplot 2
    ax2.plot(time, LF_signal, color='deepskyblue')
    ax2.set_title("LF Signal")
    ax2.grid(color='dimgrey')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.set_xlim((0, 5/28))

    # Save and close plot
    plt.savefig(f"figures/full_data_iteration.png")
    plt.close()


# TODO define materials with peak types and resonance points
if __name__ == '__main__':

    # Create Material
    material = {
        'Name': "Material 1",
        'Resonances': [16.5, 18, 19.1],
        'Peaks': [1, 2, 1]
    }
    material = {
        'Name': "Material 2",
        'Resonances': [17],
        'Peaks': [1]
    }
    material = {
        'Name': "Material 3",
        'Resonances': [18.4],
        'Peaks': [3]
    }
    material = {
        'Name': "Material 4",
        'Resonances': [16.8, 18.9],
        'Peaks': [1, 3]
    }
    material = {
        'Name': "Material 5",
        'Resonances': [16.2, 17.5],
        'Peaks': [1, 1]
    }

    sweep(material)

    print("Sweep")
    print("Stop")
    print("End")
