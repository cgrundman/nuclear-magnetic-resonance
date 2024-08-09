# Nuclear Magnetic Resonance

This repository is for NMR simulation and education about the NMR field. Any thing here is free to use under the MIT License.

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/app_example.gif" width=600 />

## Continuous Wave NMR

NMR spectroscopy is a non-destructive method for material identification. The current state-of-the-art machines are expensive and in high demand. Therefor, NMR Data is difficult to come by. This repository creates and and used fake NMR data to exemplify how NMR machines are used.

The first NMR machines used a continuous wave to bring protons (H atoms) in and out of resonance. This technology is called Continuous Wave Nuclear Magnetic Resonanse (CW-NMR). There are three main components discussed below: Signal Generation, Data Processing, and Pattern Recognition.

### 1. Signal Generation

CW-NMR can only "see" part of the the resonance spectrum at any given iteration. The device must be iterated through a sweep of resonance ranges to produce a spectrum. The following gif shows a full sweep through the full range of high frequency.

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/full_sweep.gif" width=400 />

A single iteration is seen below:

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/full_data_iteration.png" width=400 /> 

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/highlighted_data.png" width=400 />

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/trimmed_data.png" width=400 />

Several samples are needed in a single iteration to reduce the signal noise. The valid ranges are where the rate of the low frequncy signal is:
<ol>
  <li>Essentially flat - where the signal is linear</li>
  <li>Increasing - resonance peaks occur at diferent points according to increasing or decreasing magnetic field</li>
</ol>
The signals are then trimmed and saved for later preprocessing.

### 2. Data Processing

The data processing step is broken down into 2 substeps: merge iteration and iteration combination.

Merge iteration merges all of the data from a single iteration to reduce noise from the data colection. The data was slices and saved as a single stream. This stream is resliced, and then the values averaged to smooth out errors.

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/merge_iteration.png" width=400 />

Iteration combination recieves the merged iterations and adds them to the spectrum. The spectrum is initialized empty and value are added in a weighted manner, to reduce signal noise. This process creates the full spectrum of NMR data and is visualized below:

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/spectrum.gif" width=400 />

With the ability to create a full spectrum, the next task will be to reduce the data further and identify the material being sampled. This is done through a deep learning model in the next step.

### 3. Pattern Recognition

Pattern recognition means developing a mathematical model that estimates the 1200 datapoints into a single material. This mathematical model is developed using machine learning. THe process of selecting an algorithm or architecture means looking at the data. This is seq2seq (sequence to sequence) problem that is further classified as a many-to-one. This means that many data points (an NMR spectrum) are translated into one data point (material classification.

The common approach to any ML problem is to pick an ML baseline from scikit-learn and then try to beat that baseline with a deep learning architecture. Scikit-learn provides a [great tool](https://scikit-learn.org/1.3/tutorial/machine_learning_map/index.html) for selecting an ML algorithm seen below:

<img src="https://scikit-learn.org/1.3/_static/ml_map.png" width=400 />

For this problem, a Linear Support Vector Classification (SVC) function was implemented. It had a 100% classification rate for the 2000 test samples. So it is pretty unneccesary to create a Neural Network for the data as it exists now (remember that this is idealized data, and there are other missing phenomenon). 

A [dense neural network](https://www.ibm.com/topics/neural-networks) is the obvious first choice for a deep leanring model. For sequential data classification [Recurrent Neural Networks (RNNs)](https://www.ibm.com/topics/recurrent-neural-networks), and [Long-Short Term Memory (LSTMs)](https://medium.com/@ottaviocalzone/an-intuitive-explanation-of-lstm-a035eb6ab42c) are appropriate choices, however they are very large and not needed in this application.

The neural network proived 100% classification as well. While it is ~10x slower than the Linear SVC, it provides regression data for all 5 materials. The Linear SVC returns a single number. The NN returns 5 numbers, confidences in each material positionally encoded to match the material. Below is an example of material classification:

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/model_demo.png" width=400 />

### Application

The application, written with python/tkinter, combines all of the functions above to show how a CW-NMR device works.

<img src="https://github.com/cgrundman/NMR-Signal/blob/master/figures/material_4_full_run.gif" />

## Fourier Transform NMR

Coming Soon...

## License

[MIT](https://choosealicense.com/licenses/mit/)
