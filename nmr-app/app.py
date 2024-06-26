import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Create the main Tkinter window
root = tk.Tk()
root.title("NMR Application")
root.geometry("1200x525")
root.configure(bg='#4c4c4c')

# Create a style for the close button
style = ttk.Style()
style.configure('Red.TButton', 
                background='#dc3545', 
                foreground='#dc3545', 
                font=('Helvetica', 12),
                padding=6)
style.map('Red.TButton',
          background=[('active', '#dc3545'), ('pressed', '#bd2130')])

# Create a style for the plot button
style = ttk.Style()
style.configure('Blue.TButton', 
                background='#3556dc', 
                foreground='#3556dc', 
                font=('Helvetica', 12),
                padding=6)
style.map('Red.TButton',
          background=[('active', '#3556dc'), ('pressed', '#bd2130')])

# Create a frame for the plot
plot_frame = tk.Frame(root)
plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a label
label = tk.Label(root, text="NMR Application", bg='#4c4c4c')
label.pack(pady=20)

# # Function to create a plot
# def create_plots():
#     fig = Figure(figsize=(10, 4), dpi=100, constrained_layout=True)
#     # fig.tight_layout()
    
#     # Create subplot 1
#     ax1 = fig.add_subplot(211)
#     x1 = np.linspace(0, 200, 100)
#     y1 = np.random.rand(100)
#     y1_sin = np.sin(x1) + 0.5
#     ax1.plot(x1, y1, y1_sin)
#     ax1.set_title("NMR Signal") # TODO name better
#     # ax1.set_yticks([])
#     ax1.set_xlim([0, 200])
#     ax1.set_ylim([0, 4])
#     ax1.grid()
    
#     # Create subplot 2
#     range = [16, 20]
#     length = 1200
#     ax2 = fig.add_subplot(212)
#     x2 = np.linspace(range[0], range[1], length)
#     y2 = np.random.rand(length)*0.5
#     ax2.plot(x2, y2)
#     ax2.set_title("NMR Data") # TODO name better
#     # ax2.set_yticks([])
#     ax2.set_xlim([range[0], range[1]])
#     ax2.set_ylim([0, 4])
#     ax2.grid()

#     canvas = FigureCanvasTkAgg(fig, master=root)  # A Tkinter canvas for the Matplotlib figure
#     canvas.draw()
#     canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
def create_plots():
    # y1 = np.random.rand((len(x1)))
    # ax1.plot(x1, y1, y1_sin)
    pass

fig = Figure(figsize=(10, 4), dpi=100, constrained_layout=True)
fig.patch.set_facecolor('#4c4c4c')

# Create subplot 1
ax1 = fig.add_subplot(211)
x1 = np.linspace(0, 200, 100)
y1 = np.zeros((len(x1)))
y1_sin = np.zeros((len(x1)))
ax1.plot(x1, y1, y1_sin)
ax1.set_title("NMR Signal", color=(0.9, 0.9, 0.9)) # TODO name better
# ax1.set_yticks([])
ax1.set_xlim([0, 200])
ax1.set_ylim([0, 4])
ax1.set_facecolor((0.5, 0.5, 0.5))
ax1.grid()

# Create subplot 2
range = [16, 20]
length = 1200
ax2 = fig.add_subplot(212)
x2 = np.linspace(range[0], range[1], length)
y2 = np.zeros((len(x2)))
ax2.plot(x2, y2)
ax2.set_title("NMR Data", color=(0.9, 0.9, 0.9)) # TODO name better
# ax2.set_yticks([])
ax2.set_xlim([range[0], range[1]])
ax2.set_ylim([0, 4])
ax2.set_facecolor((0.5, 0.5, 0.5))
ax2.grid()

canvas = FigureCanvasTkAgg(fig, master=root)  # A Tkinter canvas for the Matplotlib figure
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg='#4c4c4c')
button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# Button to create the plots
plot_button = ttk.Button(button_frame, text="Plot Data", command=create_plots(), style='Blue.TButton')
plot_button.pack(side=tk.LEFT, padx=10)

# Button to close the application
close_button = ttk.Button(button_frame, text="Close", command=root.destroy, style='Red.TButton')
close_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()