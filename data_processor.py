import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os


# TODO load all data 
# TODO Create single nmr resonance data
# TODO reshape NMR SPectrum
def process_data(path):

    # Initialize empty NMR Spectrum
    nmr_spectrum = np.zeros([2, 1200])
    nmr_spectrum[0,:] = np.linspace(16, 20, num=1200)

    # Create list of files within path
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break

    # Iterate trough files
    for file in files:

        print(file)

        # Load data
        data_load = np.loadtxt(path + file)
        lf = data_load[0,:]
        nmr = data_load[1,:]

        # Extract hf_setting
        hf_setting = extract_decimal(file)

        # Merge data from single iteration
        nmr_iteration, lf_iteration = merge_iteration(nmr, lf)

        nmr_spectrum = iteration_combine(nmr_spectrum, nmr_iteration, lf_iteration, hf_setting)

    # Plot the spectrum
    plot_spectrum(nmr_spectrum)

    return nmr_spectrum


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


# TODO Plot iteration_combine function
def iteration_combine(Spectrum, NMR_iteration, LF_iteration, HF_setting):

    # Locate absolute position of iteration
    LF_iteration = LF_iteration + HF_setting

    # Find first close index pair
    idx_spec, idx_lf = find_closest(LF_iteration, Spectrum[0,:])

    # Test two closest spectrum points
    diff = [abs(LF_iteration[idx_lf] - Spectrum[0,idx_spec]), 
            abs(LF_iteration[idx_lf] - Spectrum[0,idx_spec+1])]
    # Set the index to closest of the two
    if diff[1] < diff[0]:
        idx_spec += 1

    # Set absolute postion of data within spectrum
    LF_iteration = Spectrum[0,idx_spec:idx_spec+len(LF_iteration)]

    # Insert NMR data into spectrum
    for i in range(len(NMR_iteration)):
        if i < idx_lf-1:
            if 16 <= LF_iteration[idx_lf+i] <= 20:
                if Spectrum[1,idx_spec+i] != 0:
                    Spectrum[1,idx_spec+i] = (Spectrum[1,idx_spec+i] + NMR_iteration[idx_lf+i])/2
                else:
                    Spectrum[1,idx_spec+i] = NMR_iteration[i]

    return Spectrum


def find_closest(array, baseline):
    
    for value in array:
        for value_baseline in baseline:
            if abs(value - value_baseline) < 0.00336:
                idx_spec = np.where(baseline==value_baseline)[0][0]
                idx_lf = np.where(array==value)[0][0] 
    
                return idx_spec, idx_lf


# TODO make a loop to reduce code length in sliced plots
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

    # Data Slices
    ax4 = fig.add_subplot(gs[2,0])
    ax4.plot(NMR_slices[0,:], color='lightcoral')
    ax4.grid(color='dimgrey')
    ax4.set_xticklabels([])
    ax4.set_yticklabels([])
    ax4.set_ylim((.9, 4.1))
    ax5 = fig.add_subplot(gs[2,1])
    ax5.plot(NMR_slices[1,:], color='lightcoral')
    ax5.grid(color='dimgrey')
    ax5.set_xticklabels([])
    ax5.set_yticklabels([])
    ax5.set_ylim((.9, 4.1))
    ax6 = fig.add_subplot(gs[2,2])
    ax6.plot(NMR_slices[2,:], color='lightcoral')
    ax6.grid(color='dimgrey')
    ax6.set_xticklabels([])
    ax6.set_yticklabels([])
    ax6.set_ylim((.9, 4.1))
    ax7 = fig.add_subplot(gs[2,3])
    ax7.plot(NMR_slices[3,:], color='lightcoral')
    ax7.grid(color='dimgrey')
    ax7.set_xticklabels([])
    ax7.set_yticklabels([])
    ax7.set_ylim((.9, 4.1))
    ax8 = fig.add_subplot(gs[2,4])
    ax8.plot(NMR_slices[4,:], color='lightcoral')
    ax8.grid(color='dimgrey')
    ax8.set_xticklabels([])
    ax8.set_yticklabels([])
    ax8.set_ylim((.9, 4.1))
    ax6.set_title("Sliced Data")

    ax9 = fig.add_subplot(gs[3,0])
    ax9.plot(LF_slices[0,:], color='deepskyblue')
    ax9.grid(color='dimgrey')
    ax9.set_xticklabels([])
    ax9.set_yticklabels([])
    ax10 = fig.add_subplot(gs[3,1])
    ax10.plot(LF_slices[1,:], color='deepskyblue')
    ax10.grid(color='dimgrey')
    ax10.set_xticklabels([])
    ax10.set_yticklabels([])
    ax11 = fig.add_subplot(gs[3,2])
    ax11.plot(LF_slices[2,:], color='deepskyblue')
    ax11.grid(color='dimgrey')
    ax11.set_xticklabels([])
    ax11.set_yticklabels([])
    ax12 = fig.add_subplot(gs[3,3])
    ax12.plot(LF_slices[3,:], color='deepskyblue')
    ax12.grid(color='dimgrey')
    ax12.set_xticklabels([])
    ax12.set_yticklabels([])
    ax13 = fig.add_subplot(gs[3,4])
    ax13.plot(LF_slices[4,:], color='deepskyblue')
    ax13.grid(color='dimgrey')
    ax13.set_xticklabels([])
    ax13.set_yticklabels([])

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


def plot_spectrum(Spectrum):
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 5))
    plt.plot(Spectrum[0,:], Spectrum[1,:])
    plt.grid(color='dimgrey')
    plt.title("Spectrum")
    plt.savefig(f"figures/spectrum.png")
    plt.close()


# TODO save spectrum
if __name__ == '__main__':
    path = 'data/unprocessed_nmr_data/Material_1/'
    directory = os.fsencode(path)

    nmr_spectrum = process_data(path)

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
