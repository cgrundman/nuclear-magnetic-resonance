from matplotlib.figure import Figure
import numpy as np

# Function to create a plot
def nmr_signal_plot():
    # Create a Matplotlib figure
    fig = Figure(figsize=(13.5, 2), dpi=100)
    fig.tight_layout()
    plot = fig.add_subplot(111)
    data_points = 400
    x1 = np.linspace(0, 100, data_points)
    y1 = np.random.rand(data_points)
    y1_sin = np.sin(x1/3) + 2
    plot.plot(x1, y1, y1_sin)
    # plot.set_title(title)
    plot.set_xlim([x1[0], x1[-1]])
    plot.set_ylim([0, 4])
    plot.set_ylabel("NMR Signal")
    plot.set_yticklabels([])
    plot.set_xticklabels([])
    plot.grid(True)

    return fig