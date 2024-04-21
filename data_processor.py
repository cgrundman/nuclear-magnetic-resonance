import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
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
    plot_merge_iteration(NMR_signal, NMR_slices, NMR_merged, LF_signal, LF_slices, LF_merged)
    print(np.shape(NMR_merged))
    print(np.shape(LF_merged))


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
    # for slice in range(slices):
    #     ax[slice]
    # x0 = 0
    # for slice in range(slices):
    #     num = slice + 2
    #     x{num} = fig.add_subplot(gs[2,slice])
        

    # ax2.plot(time, LF_signal, color='deepskyblue')
    # ax2.set_title("LF Signal")
    # ax2.grid(color='dimgrey')
    # ax2.set_xticklabels([])
    # ax2.set_yticklabels([])
    # ax2.set_xlim((0, 5/28))

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

    # ax2.plot(time, LF_signal, color='deepskyblue')
    # ax2.set_title("LF Signal")
    # ax2.grid(color='dimgrey')
    # ax2.set_xticklabels([])
    # ax2.set_yticklabels([])
    # ax2.set_xlim((0, 5/28))

    # Save and close plot
    plt.savefig(f"figures/merge_iteration.png")
    plt.close()


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
