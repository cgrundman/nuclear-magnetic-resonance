import numpy as np

# TODO Create main funciton
# TODO load all data
# TODO Combine all samples from the same HF setting
# TODO Combine two nmr samples with different HF settings
# TODO Create single nmr resonance data 
path = 'data/unprocessed_nmr_data/Material_1/'

nmr = np.loadtxt(path + "159938_nmr.txt")

print(len(nmr))
