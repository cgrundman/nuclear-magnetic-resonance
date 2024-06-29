import numpy as np

def nmr_spectrum_compiler():
    x=np.linspace(16, 20, 1200)
    nmr_spectrum = np.random.rand(len(x))
    return x, nmr_spectrum