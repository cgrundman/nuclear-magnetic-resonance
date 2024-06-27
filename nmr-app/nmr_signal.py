import numpy as np
from math import *
import random


# Generate the nmr signal
def nmr_signal_generator(material, HF_actual):

    # Extract Material Properties
    resonances = material["Resonances"]
    peaks = material["Peaks"]

    # Set number of data points
    data_points = np.linspace(0, 5/28, 2000)

    # Create the lf signal
    lf_signal = (np.sin(2 * pi * 28 * data_points - pi/2) + 1)*.2

    # Create the nmr signal
    nmr_signal = np.random.rand(len(data_points)) + 3

    # Chack for and Calculate resonances
    for i in range(len(resonances)):
        resonance = resonances[i]
        peak = peaks[i]
        for n in range(len(data_points)):
            if peak == 1:
                # Single Peak
                if resonance - .05 < lf_signal[n] + HF_actual < resonance + .05:
                    nmr_signal[n] = random.random()/10 + 1 + 50*abs((resonance-HF_actual)-lf_signal[n])
            elif peak == 2:
            # Double Peak
                resonance_high = resonance + .05
                resonance_low = resonance - .05
                if resonance_high - .02 < lf_signal[n] + HF_actual < resonance_high + .02:
                    nmr_signal[n] = random.random()/10 + 2 + 45*abs((resonance_high-nmr_signal)-(lf_signal[n]))
                elif resonance_low - .02 < lf_signal[n] + HF_actual < resonance_low + .02:
                    nmr_signal[n] = random.random()/10 + 2 + 45*abs((resonance_low-nmr_signal)-(lf_signal[n]))
            # Triple Peak
            elif peak == 3:
                resonance_high = resonance + .05
                resonance_low = resonance - .05
                if resonance_high - .02 < lf_signal[n] + HF_actual < resonance_high + .02:
                    nmr_signal[n] = random.random()/10 + 2.5 + 40*abs((resonance_high-HF_actual)-(lf_signal[n]))
                elif resonance_low - .02 < lf_signal[n] + HF_actual < resonance_low + .02:
                    nmr_signal[n] = random.random()/10 + 2.5 + 40*abs((resonance_low-HF_actual)-(lf_signal[n]))
                elif resonance - .02 < lf_signal[n] + HF_actual < resonance + .02:
                    nmr_signal[n] = random.random()/10 + 1.5 + 50*abs((resonance-HF_actual)-(lf_signal[n]))


    return data_points, lf_signal, nmr_signal
