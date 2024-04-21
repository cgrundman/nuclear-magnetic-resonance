# NMR Signal

This is the repository for generating NMR signal, and showing how pattern recognition can be performed on the generated data.

There are three main components: Signal Generation, Data Processing, and Pattern Recognition.

## Signal Generation

The following gif shows a full sweep through the full range of high frequency .

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/full_sweep.gif" />

The simulated full data is seen below:

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/full_data_iteration.png" />

The useful data ranges lie in the same data ranges. Because of error in the measurement, several samples are needed to reconstruct the signal. The valid ranges are where the rate of the low frequncy signal is 1) essentially flat and 2) increasing. It is important to only select the increasing rate regions, becuase the resonance happens differently depending on whether the low frequency signal is increasing or decreasing. These regions are highlighed in yellow below: 

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/highlighted_data.png" />


From here, the signals are trimmed to only include the highlighted regions. The trimmed data is then saved to have preprocessed later. After trimming, the raw NMR data appears as below:


<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/trimmed_data.png" />

## Data Processing

THe data processing step is broken down into 2 substeps: merge iteration and iteration combination.

### Merge Iteration

Merge iteration, as pictured below, is the process of using data collected from a common setting, and merging it to reduce noise from the data colection. The data was slices and saved as a single stream. This stream is resliced, and then the values averaged to smooth out errors.

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/merged_iteration.png" />

### Iteration Combination


## Pattern Recognition
