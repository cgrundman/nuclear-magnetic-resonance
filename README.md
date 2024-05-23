# Nuclear Magnetic Resonance

NMR spectroscopy is a non-destructive method for material identification. It is a unique process that may become very prevelent in the future in diagnostics and material analysis. The current state-of-the-art machines are expensive and in high demand. Therefor NMR Data is difficult to come by.

This repository is meant to serve as a supplement to NMR fundamentals, more specifically Continuous Wave (CW) NMR. This repo contains code for generating an NMR signal, processing the raw signal into tradition NMR data, and then showing how pattern recognition can be performed on the generated data.

To note, most NMR resources will show Fourier Transform (FT) NMR. And there are even further many types of producing material data, incuding multidimensional arrays. FT NMR is important, as it allows much much faster material analysis using one of the most important algorithms of the 20th century: the Fourier Transform. This data set is for simple 1D data, and will showcase CW NMR, though I hope to add sections of FT NMr at a later time. 

There are three main components discussed below: Signal Generation, Data Processing, and Pattern Recognition.

## 1. Signal Generation

The following gif shows a full sweep through the full range of high frequency.

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/full_sweep.gif" />

The simulated full data is seen below:

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/full_data_iteration.png" />

The useful data ranges lie in the same data ranges. Because of error in the measurement, several samples are needed to reconstruct the signal. The valid ranges are where the rate of the low frequncy signal is 1) essentially flat and 2) increasing. It is important to only select the increasing rate regions, becuase the resonance happens differently depending on whether the low frequency signal is increasing or decreasing. These regions are highlighed in yellow below: 

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/highlighted_data.png" />

From here, the signals are trimmed to only include the highlighted regions. The trimmed data is then saved to have preprocessed later. After trimming, the raw NMR data appears as below:

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/trimmed_data.png" />

## 2. Data Processing

The collected NMR data must be processed to produce the NMR spectrum of the material sample. The data processing step is broken down into 2 substeps: merge iteration and iteration combination. Because the LF signal variance is less than the entire spectrum, the full spectrum needs a series of data collections.

Merge iteration, as pictured below, is the process of using data collected from a common setting, and merging it to reduce noise from the data colection. The data was slices and saved as a single stream. This stream is resliced, and then the values averaged to smooth out errors.

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/merge_iteration.png" />

Iteration combination recieves the merged iterations and adds them to the spectrum. The spectrum is initialized empty and value are added in a weighted manner, to reduce signal noise. This process creates the full spectrum of NMR data and is visualized below:

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/spectrum.gif" />

With the ability to create a full spectrum, the next task will be to reduce the data further and identify the material being sampled. This is done through a deep learning model in the next step.

## 3. Pattern Recognition

The next task is to recognize the patterns present in the data. At a quick glance, one can see that the materials are very different. The challenge is developing a mathematical model that estimates the 1200 datapoints into a single material. 

This mathematical model is developed using machine learning. While this is a very hot topic right now, the mathematics behind it have been around for many years. To avoid making this too "mystical" for the average viewer, pattern recognition is used to take the stigma away from what we are doing. So don't worry, this isn't another ChatGPT API.

As disclosure, the model will be devoloped in Google Colab, a jupyter notebook environment that is easily accessible (at the moment at least). This allows for a more simple setup than a local installation of machine learning libraries. TensorFlow will be used for the model creation. For the technical machine learning algorithms and documentation, please refer to the Colab page, as it contains notebook documentaiton. 

Three model architectures were tested for this task: a [neural network](https://www.ibm.com/topics/neural-networks) (think of this as very basic), a [recurrent neural network (RNN)](https://www.ibm.com/topics/recurrent-neural-networks), and a [Long-Short Term Memory (LSTM)](https://medium.com/@ottaviocalzone/an-intuitive-explanation-of-lstm-a035eb6ab42c) Model. These all have success in tasks involving sequetial data. 


