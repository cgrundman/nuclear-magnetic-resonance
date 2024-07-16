import numpy as np

def nmr_spectrum_compiler(NMR_spectrum, NMR_signal, LF_signal, HF_setting, time):

    time_trimmed, NMR_trimmed, LF_trimmed = trim_signal(time, NMR_signal, LF_signal)

    if HF_setting < 19.9:

        NMR_merged, LF_merged = merge(NMR_signal=NMR_trimmed, LF_signal=LF_trimmed)

        NMR_merged = NMR_merged*(-1) + 4

        NMR_spectrum = spectrum_combine(NMR_spectrum=NMR_spectrum, 
                                        NMR_signal=NMR_merged,
                                        LF_signal=LF_merged,
                                        HF_setting=HF_setting)

    return NMR_spectrum

def merge(NMR_signal, LF_signal):

    # Identify where to slice the signals
    seperator_list = [0]
    for n in range(len(LF_signal)):
        if n != 0:
            if LF_signal[n-1] > LF_signal[n]:
                seperator_list.append(n)
    seperator_list.append(len(NMR_signal)-1)

    # Create parameters of each slice
    n_slices = len(seperator_list)-1 # number of slices
    slice_size = len(NMR_signal) # create the size of each slice
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

    # Merge the slices
    NMR_merged = np.zeros([np.shape(NMR_slices)[1]])
    LF_merged = np.zeros([np.shape(LF_slices)[1]])
    for data_point in range(np.shape(NMR_slices)[1]):
        for slice in range(np.shape(NMR_slices)[0]):
            NMR_merged[data_point] += NMR_slices[slice,data_point]
            LF_merged[data_point] += LF_slices[slice,data_point]
    NMR_merged = NMR_merged/5
    LF_merged = LF_merged/5

    return NMR_merged, LF_merged

def spectrum_combine(NMR_spectrum, NMR_signal, LF_signal, HF_setting):
    # Locate absolute position of iteration
    LF_signal = LF_signal + HF_setting

    # Find first close index pair
    idx_spec, idx_lf = find_closest(LF_signal, NMR_spectrum[0,:])

    # Test two closest spectrum points
    lower = abs(LF_signal[idx_lf] - NMR_spectrum[0,idx_spec])
    if idx_spec+1 < 1200:
        upper = abs(LF_signal[idx_lf] - NMR_spectrum[0,idx_spec+1])
    else:
        upper = 1
    diff = [lower, upper]

    # Set the index to closest of the two
    if diff[1] < diff[0]:
        idx_spec += 1
    # Number of values beyond Spec Range
    idx_end = 0
    if idx_spec > len(NMR_spectrum[0,:])-len(NMR_signal) - 1:
        idx_end = len(NMR_signal) - (len(NMR_spectrum[0,:]) - idx_spec)

    # Set absolute postion of data within spectrum
    LF_signal = NMR_spectrum[0,idx_spec:idx_spec+len(LF_signal)]

    # Insert NMR data into spectrum
    for i in range(len(NMR_signal)-idx_lf-idx_end):
        # Check for current index being within spectrum
        if 16 <= LF_signal[idx_lf+i] <= 20:
            # If value at index is nonzero
            if NMR_spectrum[1,idx_spec+i] != 0:
                NMR_spectrum[1,idx_spec+i] = (NMR_spectrum[1,idx_spec+i]*NMR_spectrum[2,idx_spec+i] + NMR_signal[idx_lf+i])/(NMR_spectrum[2,idx_spec+i]+1)
                NMR_spectrum[2,idx_spec+i] += 1
            # If value at index is zero
            else:
                NMR_spectrum[1,idx_spec+i] = NMR_signal[i]
                NMR_spectrum[2,idx_spec+i] += 1

    return NMR_spectrum

def find_closest(array, baseline):
    
    for value in array:
        for value_baseline in baseline:
            if abs(value - value_baseline) < 0.00336:
                idx_spec = np.where(baseline==value_baseline)[0][0]
                idx_lf = np.where(array==value)[0][0] 

                return idx_spec, idx_lf
            
            
def trim_signal(time, NMR_signal, LF_signal):

    # Adjust the LF Signal
    LF_signal -= 0.5
    LF_signal /= 3

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

    # Trim the data
    LF_trimmed = []
    NMR_trimmed =  []
    for i in range(len(idx_points[0,:])):
        min_idx = int(idx_points[0,i])
        max_idx = int(idx_points[1,i])
        LF_trimmed = np.append(LF_trimmed, LF_signal[min_idx:max_idx])
        NMR_trimmed = np.append(NMR_trimmed, NMR_signal[min_idx:max_idx])
    time_trimmed = time[:int(len(NMR_trimmed))]

    return time_trimmed, NMR_trimmed, LF_trimmed