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

The collected NMR data must be processed to produce the NMR spectrum of the material sample. The data processing step is broken down into 2 substeps: merge iteration and iteration combination. Because the LF signal variance is less than the entire spectrum, the full spectrum needs a series of data collections.

Merge iteration, as pictured below, is the process of using data collected from a common setting, and merging it to reduce noise from the data colection. The data was slices and saved as a single stream. This stream is resliced, and then the values averaged to smooth out errors.

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/merge_iteration.png" />

Iteration combination recieves the merged iterations and adds them to the spectrum. The spectrum is initialized empty and value are added in a weighted manner, to reduce signal noise. This process creates the full spectrum of NMR data and is visualized below:

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/spectrum.gif" />

With the ability to create a full spectrum, the next task will be to reduce the data further and identify the material being sampled. This is done through a deep learning model in the next step.

## Pattern Recognition

The next task is to take the now processed NMR data, and classify it into a material. This is done by exposing a neural network model to many examples and training it to guess the material.

test
