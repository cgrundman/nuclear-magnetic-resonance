from matplotlib.figure import Figure
import numpy as np

def plot(name, x, y, plot_rgb):
    # Create a Matplotlib figure
    fig = Figure(figsize=(13.5, 2), dpi=100)
    fig.patch.set_facecolor('#4c4c4c')
    fig.tight_layout()
    plot = fig.add_subplot(111)
    # print(np.size(y))
    for i in range(len(y)):
        plot.plot(x, y[i], color=plot_rgb[i])
    plot.set_xlim([x[0], x[-1]])
    plot.set_ylim([0, 4])
    plot.set_ylabel(name)
    plot.set_facecolor('#7f7f7f')
    plot.grid(True)

    return fig