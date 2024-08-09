import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os


def process_data(path):

    # Initialize empty NMR Spectrum
    nmr_spectrum = np.zeros([3, 1200])
    nmr_spectrum[0,:] = np.linspace(16, 20, num=1200)

    # Create list of files within path
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break

    # counter = 1
    # Iterate trough files
    for file in files:

        # Load data
        data_load = np.loadtxt(path + "/" + file)
        lf = data_load[0,:]
        nmr = data_load[1,:]

        # Extract hf_setting
        hf_setting = extract_decimal(file)

        if hf_setting < 19.9:

            # Merge data from single iteration
            nmr_iteration, lf_iteration = merge_iteration(nmr, lf)

            nmr_iteration = nmr_iteration*(-1) + 4

            nmr_spectrum = iteration_combine(nmr_spectrum, nmr_iteration, lf_iteration, hf_setting)

            # Plot the spectrum
            # plot_spectrum(nmr_spectrum, counter)
            # counter +=1

    # Save Spectrum
    save_spectrum(nmr_spectrum[1,:], name=path[26:])

    return


def extract_decimal(input_str):
    # Initialize an empty string to store the numerical part
    num_str = ""

    # Iterate through the characters in the input string
    for char in input_str:
        # If the character is a digit or a decimal point, add it to num_str
        if char.isdigit():
            num_str += char

    # Convert the extracted string to a decimal number
    decimal_number = float(num_str)

    # Scale number
    decimal_number = decimal_number/10000

    return decimal_number


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
        
    # Merge the slices
    NMR_merged = np.zeros([np.shape(NMR_slices)[1]])
    LF_merged = np.zeros([np.shape(LF_slices)[1]])
    for data_point in range(np.shape(NMR_slices)[1]):
        for slice in range(np.shape(NMR_slices)[0]):
            NMR_merged[data_point] += NMR_slices[slice,data_point]
            LF_merged[data_point] += LF_slices[slice,data_point]
    NMR_merged = NMR_merged/5
    LF_merged = LF_merged/5

    # Plot Slices
    # plot_merge_iteration(NMR_signal, NMR_slices, NMR_merged, LF_signal, LF_slices, LF_merged)

    return NMR_merged, LF_merged


def iteration_combine(Spectrum, NMR_iteration, LF_iteration, HF_setting):

    # Locate absolute position of iteration
    LF_iteration = LF_iteration + HF_setting

    # Find first close index pair
    idx_spec, idx_lf = find_closest(LF_iteration, Spectrum[0,:])

    # Test two closest spectrum points
    lower = abs(LF_iteration[idx_lf] - Spectrum[0,idx_spec])
    if idx_spec+1 < 1200:
        upper = abs(LF_iteration[idx_lf] - Spectrum[0,idx_spec+1])
    else:
        upper = 1
    diff = [lower, upper]

    # Set the index to closest of the two
    if diff[1] < diff[0]:
        idx_spec += 1
    # Number of values beyond Spec Range
    idx_end = 0
    if idx_spec > len(Spectrum[0,:])-len(NMR_iteration) - 1:
        idx_end = len(NMR_iteration) - (len(Spectrum[0,:]) - idx_spec)

    # Set absolute postion of data within spectrum
    LF_iteration = Spectrum[0,idx_spec:idx_spec+len(LF_iteration)]

    # Insert NMR data into spectrum
    for i in range(len(NMR_iteration)-idx_lf-idx_end):
        # Check for current index being within spectrum
        if 16 <= LF_iteration[idx_lf+i] <= 20:
            # If value at index is nonzero
            if Spectrum[1,idx_spec+i] != 0:
                Spectrum[1,idx_spec+i] = (Spectrum[1,idx_spec+i]*Spectrum[2,idx_spec+i] + NMR_iteration[idx_lf+i])/(Spectrum[2,idx_spec+i]+1)
                Spectrum[2,idx_spec+i] += 1
            # If value at index is zero
            else:
                Spectrum[1,idx_spec+i] = NMR_iteration[i]
                Spectrum[2,idx_spec+i] += 1

    return Spectrum


def find_closest(array, baseline):
    
    for value in array:
        for value_baseline in baseline:
            if abs(value - value_baseline) < 0.00336:
                idx_spec = np.where(baseline==value_baseline)[0][0]
                idx_lf = np.where(array==value)[0][0] 
    
                return idx_spec, idx_lf


def save_spectrum(spectrum, name):

    # Create save folder
    newpath = f"data/processed_nmr_data/"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    # Save signals to single .txt
    np.savetxt(f"data/processed_nmr_data/{name}.txt", spectrum)


def plot_merge_iteration(NMR_signal, NMR_slices, NMR_merged, LF_signal, LF_slices, LF_merged):
    
    # Define number of slices
    slices = np.shape(NMR_slices)[0]

    # Plot the Signals
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 10))
    gs = GridSpec(nrows=6, ncols=slices)
    # fig, (ax0, ax1, ax2, ax3, ax4, ax5) = plt.subplots(6, 5)
    fig.suptitle("Merge Iteration")

    # Orignal Data
    ax0 = fig.add_subplot(gs[0,:])
    ax0.plot(NMR_signal, color='lightcoral') # NMR signal
    ax0.set_title("Original Data")
    ax0.grid(color='dimgrey')
    ax0.set_xticklabels([])
    ax0.set_yticklabels([])
    ax0.set_ylim((.9, 4.1))
    ax1 = fig.add_subplot(gs[1,:])
    ax1.plot(LF_signal, color='deepskyblue') # LF signal
    ax1.grid(color='dimgrey')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])

    # Data Slices - NMR Data
    ax4 = fig.add_subplot(gs[2,0])
    ax5 = fig.add_subplot(gs[2,1])
    ax6 = fig.add_subplot(gs[2,2])
    ax7 = fig.add_subplot(gs[2,3])
    ax8 = fig.add_subplot(gs[2,4])
    ax_list = [ax4, ax5, ax6, ax7, ax8]
    for i in range(len(ax_list)):
        ax = ax_list[i]
        ax.plot(NMR_slices[i,:], color='lightcoral')
        ax.grid(color='dimgrey')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_ylim((.9, 4.1))
    ax6.set_title("Sliced Data")

    # Data Slices - LF Data
    ax9 = fig.add_subplot(gs[3,0])
    ax10 = fig.add_subplot(gs[3,1])
    ax11 = fig.add_subplot(gs[3,2])
    ax12 = fig.add_subplot(gs[3,3])
    ax13 = fig.add_subplot(gs[3,4])
    ax_list = [ax9, ax10, ax11, ax12, ax13]
    for i in range(len(ax_list)):
        ax = ax_list[i]
        ax.plot(LF_slices[0,:], color='deepskyblue')
        ax.grid(color='dimgrey')
        ax.set_xticklabels([])
        ax.set_yticklabels([])

    # Merged Data
    ax2 = fig.add_subplot(gs[4,1:-1])
    ax2.plot(NMR_merged, color='lightcoral') # NMR merged
    ax2.set_title("Merged Data")
    ax2.grid(color='dimgrey')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.set_ylim((.9, 4.1))
    ax3 = fig.add_subplot(gs[5,1:-1])
    ax3.plot(LF_merged, color='deepskyblue') # LF merged
    ax3.grid(color='dimgrey')
    ax3.set_xticklabels([])
    ax3.set_yticklabels([])

    # Save and close plot
    plt.savefig(f"figures/merge_iteration.png")
    plt.close()


def plot_spectrum(Spectrum, counter):

    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 5))
    plt.plot(Spectrum[0,:], Spectrum[1,:])
    plt.grid(color='dimgrey')
    plt.title("Spectrum")
    plt.ylim([0,4])
    plt.xlim([16,20])
    plt.savefig(f"figures/spec/spectrum_{counter}.png")
    plt.close()


if __name__ == '__main__':

    path = 'data/unprocessed_nmr_data/'
    
    dir_list = []
    for subdir in os.walk(path):
        
        dir_list += [subdir[0]]


    for subdir in dir_list[1:]:

        print(f"Processing: {subdir[26:]}")
        process_data(subdir)
