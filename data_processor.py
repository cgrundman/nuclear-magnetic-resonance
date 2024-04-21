import numpy as np
import os


# TODO load all data
# TODO Combine all samples from the same HF setting
# TODO Combine two nmr samples with different HF settings
# TODO Create single nmr resonance data 
def process_data(path):

    # Single data load
    nmr = np.loadtxt(path + "159938_nmr.txt")
    lf = np.loadtxt(path + "159938_lf.txt")

    # Merge data from single iteration
    merge_iteration(nmr, lf)

    # print(len(lf))

    pass


# TODO make each slice of data the same size
# TODO plot this operation
# TODO average all the data into the same list
def merge_iteration(NMR_signal, LF_signal):

    # Identify where to slice the signals
    seperator_list = [0]
    for n in range(len(NMR_signal)):
        if n != 0:
            if LF_signal[n-1] > LF_signal[n]:
                seperator_list.append(n)
    seperator_list.append(len(NMR_signal)-1)

    # Create parameters of each slice
    n_slices = len(seperator_list)-1 # number of slices
    slice_size = len(NMR_signal) # Commonize the 
    for i in range(n_slices):
        size = seperator_list[i+1]-seperator_list[i]
        if size<slice_size:
            slice_size = size

    # Slice the data
    NMR_slices = np.zeros([n_slices, slice_size])
    LF_slices = np.zeros([n_slices, slice_size])
    for i in range(n_slices):
        NMR_slices[i,:] = NMR_signal[seperator_list[i]:seperator_list[i]+slice_size]
        LF_slices[i,:] = LF_signal[seperator_list[i]:seperator_list[i]+slice_size]
        
    # Merge Slices
    NMR_merged = np.zeros([np.shape(NMR_slices)[1]])
    LF_merged = np.zeros([np.shape(LF_slices)[1]])
    for data_point in range(np.shape(NMR_slices)[1]):
        for slice in range(np.shape(NMR_slices)[0]):
            NMR_merged[data_point] += NMR_slices[slice,data_point]
            LF_merged[data_point] += LF_slices[slice,data_point]
    NMR_merged = NMR_merged/5
    LF_merged = LF_merged/5

    # Plot Slices
    print(np.shape(NMR_merged))
    print(np.shape(LF_merged))


if __name__ == '__main__':
    path = 'data/unprocessed_nmr_data/Material_1/'
    directory = os.fsencode(path)

    process_data(path)

    # # Iterate through NMR files
    # for file in os.listdir(directory):
    #     filename = os.fsdecode(file)
    #     if filename.endswith("nmr.txt"):
    #         # print(os.path.join(directory, filename))
    #         print(filename)
    #         continue

    # # Iterate through LF files
    # for file in os.listdir(directory):
    #     filename = os.fsdecode(file)
    #     if filename.endswith("lf.txt"):
    #         # print(os.path.join(directory, filename))
    #         print(filename)
    #         continue

    # nmr = np.loadtxt(path + "159938_nmr.txt")
