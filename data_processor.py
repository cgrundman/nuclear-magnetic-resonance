import numpy as np
import os


# TODO Create main funciton
# TODO load all data
# TODO Combine all samples from the same HF setting
# TODO Combine two nmr samples with different HF settings
# TODO Create single nmr resonance data 

if __name__ == '__main__':
    path = 'data/unprocessed_nmr_data/Material_1/'
    directory = os.fsencode(path)

    # Iterate through NMR files
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith("nmr.txt"):
            # print(os.path.join(directory, filename))
            print(filename)
            continue

    # Iterate through LF files
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith("lf.txt"):
            # print(os.path.join(directory, filename))
            print(filename)
            continue

    # nmr = np.loadtxt(path + "159938_nmr.txt")
