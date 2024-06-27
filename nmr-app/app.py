import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

from nmr_signal import nmr_signal_generator
from plot import plot, bar


# Materials
material_1 = {
    'Name': "Material_1",
    'Resonances': [16.5, 18, 19.1],
    'Peaks': [1, 2, 1]
}
material_2 = {
    'Name': "Material_2",
    'Resonances': [17],
    'Peaks': [1]
}
material_3 = {
    'Name': "Material_3",
    'Resonances': [18.4],
    'Peaks': [3]
}
material_4 = {
    'Name': "Material_4",
    'Resonances': [16.8, 18.9],
    'Peaks': [1, 3]
}
material_5 = {
    'Name': "Material_5",
    'Resonances': [16.2, 17.5],
    'Peaks': [1, 1]
}

materials = [
    material_1, 
    material_2, 
    material_3, 
    material_4, 
    material_5
]

root = tk.Tk()
root.title("Tkinter App with Plots")
root.configure(bg='#4c4c4c')

font_size = 12
bg_color = '#4c4c4c'

HF_setting = 16.0000
LF_setting = 27

# HF Setting
label1 = tk.Label(root, text=f"HF Seeting: {HF_setting:.4f}MHz", font=('Courier', 36), bg=bg_color)
label1.grid(row=0, column=0, columnspan=2)

# LF Setting
label2 = tk.Label(root, text=f"LF Setting: {LF_setting}Hz", font=('Courier', 36), bg=bg_color)
label2.grid(row=0, column=3, columnspan=2)

# NMR Signal
frame3 = ttk.Frame(root)
frame3.grid(row=1, column=0, columnspan=5)
# Create NMR Signal
x, lf_signal, nmr_signal = nmr_signal_generator(material=materials[4], HF_actual=16.0000)
# Plot NMR Signal
fig = plot(name="NMR Signal", x=x, y=[lf_signal, nmr_signal], plot_rgb=["#f01d51", "#1d78f0"])
# Embed the plot in the Tkinter frame
canvas = FigureCanvasTkAgg(fig, master=frame3)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0)

# NMR SPectrum
frame4 = tk.Frame(root)
frame4.grid(row=2, column=0, columnspan=5)
# Create NMR Spectrum
x = np.linspace(16, 20, 1200)
lf = np.random.rand(len(x))
nmr_spectrum = np.zeros(len(x))
# Plot NMR Spectrum
fig2 = plot(name="NMR Spectrum", x=x, y=[nmr_spectrum], plot_rgb=["#2cde5c"])
# Embed the plot in the Tkinter frame
canvas = FigureCanvasTkAgg(fig2, master=frame4)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0)

# Pattern Recognition
frame5 = tk.Frame(root)
frame5.grid(row=3, column=0, columnspan=3)
x = [1, 2, 3, 4, 5]
pattern_rec = np.random.rand(5)
fig3 = bar(name="Pattern Recognition", x=x, y=pattern_rec)
canvas = FigureCanvasTkAgg(fig3, master=frame5)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0)

# Material Guess
label6 = tk.Label(root, text=f"Guess: Material {np.argmax(pattern_rec) + 1}", font=('Helvetica', 25), bg=bg_color)#, width=30, height=10)
label6.grid(row=3, column=3)

# Close Application
label7 = tk.Label(root, text="Close", font=('Helvetica', font_size), bg=bg_color, width=30, height=10)
label7.grid(row=3, column=4)
run_button = ttk.Button(label7, text="Run", command=root.destroy, style='Red.TButton')
run_button.grid(ipady=10, ipadx=10)
close_button = ttk.Button(label7, text="Close", command=root.destroy, style='Red.TButton')
close_button.grid(ipady=10, ipadx=10, pady=12)

# Material Selection
label8 = tk.Label(root, text="Material Selection", wraplength=1, font=('Helvetica', font_size), bg=bg_color, highlightbackground="black", highlightthickness=2, width=30, height=40)
label8.grid(row=0, rowspan=4, column=5)

# # Create the main Tkinter window
# root = tk.Tk()
# root.title("NMR Application")
# root.geometry("1200x525")
# root.configure(bg='#4c4c4c')

# # Create a style for the close button
# style = ttk.Style()
# style.configure('Red.TButton', 
#                 background='#dc3545', 
#                 foreground='#dc3545', 
#                 font=('Helvetica', 12),
#                 padding=6)
# style.map('Red.TButton',
#           background=[('active', '#dc3545'), ('pressed', '#bd2130')])

# # Create a style for the plot button
# style = ttk.Style()
# style.configure('Blue.TButton', 
#                 background='#3556dc', 
#                 foreground='#3556dc', 
#                 font=('Helvetica', 12),
#                 padding=6)
# style.map('Red.TButton',
#           background=[('active', '#3556dc'), ('pressed', '#bd2130')])

# # Create a frame for the plot
# plot_frame = tk.Frame(root)
# plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# # Create a label
# label = tk.Label(root, text="NMR Application", bg='#4c4c4c')
# label.pack(pady=20)

# # # Function to create a plot
# # def create_plots():
# #     fig = Figure(figsize=(10, 4), dpi=100, constrained_layout=True)
# #     # fig.tight_layout()
    
# #     # Create subplot 1
# #     ax1 = fig.add_subplot(211)
# #     x1 = np.linspace(0, 200, 100)
# #     y1 = np.random.rand(100)
# #     y1_sin = np.sin(x1) + 0.5
# #     ax1.plot(x1, y1, y1_sin)
# #     ax1.set_title("NMR Signal") # TODO name better
# #     # ax1.set_yticks([])
# #     ax1.set_xlim([0, 200])
# #     ax1.set_ylim([0, 4])
# #     ax1.grid()
    
# #     # Create subplot 2
# #     range = [16, 20]
# #     length = 1200
# #     ax2 = fig.add_subplot(212)
# #     x2 = np.linspace(range[0], range[1], length)
# #     y2 = np.random.rand(length)*0.5
# #     ax2.plot(x2, y2)
# #     ax2.set_title("NMR Data") # TODO name better
# #     # ax2.set_yticks([])
# #     ax2.set_xlim([range[0], range[1]])
# #     ax2.set_ylim([0, 4])
# #     ax2.grid()

# #     canvas = FigureCanvasTkAgg(fig, master=root)  # A Tkinter canvas for the Matplotlib figure
# #     canvas.draw()
# #     canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
# def create_plots():
#     # y1 = np.random.rand((len(x1)))
#     # ax1.plot(x1, y1, y1_sin)
#     pass

# # fig = Figure(figsize=(10, 4), dpi=100, constrained_layout=True)
# # fig.patch.set_facecolor('#4c4c4c')

# # # Create subplot 1
# # ax1 = fig.add_subplot(211)
# # x1 = np.linspace(0, 200, 100)
# # y1 = np.zeros((len(x1)))
# # y1_sin = np.zeros((len(x1)))
# # ax1.plot(x1, y1, y1_sin)
# # ax1.set_title("NMR Signal", color=(0.9, 0.9, 0.9)) # TODO name better
# # # ax1.set_yticks([])
# # ax1.set_xlim([0, 200])
# # ax1.set_ylim([0, 4])
# # ax1.set_facecolor((0.5, 0.5, 0.5))
# # ax1.grid()

# # # Create subplot 2
# # range = [16, 20]
# # length = 1200
# # ax2 = fig.add_subplot(212)
# # x2 = np.linspace(range[0], range[1], length)
# # y2 = np.zeros((len(x2)))
# # ax2.plot(x2, y2)
# # ax2.set_title("NMR Data", color=(0.9, 0.9, 0.9)) # TODO name better
# # # ax2.set_yticks([])
# # ax2.set_xlim([range[0], range[1]])
# # ax2.set_ylim([0, 4])
# # ax2.set_facecolor((0.5, 0.5, 0.5))
# # ax2.grid()

# # canvas = FigureCanvasTkAgg(fig, master=root)  # A Tkinter canvas for the Matplotlib figure
# # canvas.draw()
# # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# # Create a frame for HF Setting
# hf_signal_frame = tk.Frame(root, bg='#4c4c4c', highlightbackground="black", highlightthickness=2)
# hf_signal_frame.pack(side=tk.TOP, fill=tk.X, pady=10)
# label = tk.Label(root, text="NMR Application", bg='#4c4c4c')
# label.pack(pady=20)

# # Create a frame for the buttons
# button_frame = tk.Frame(root, bg='#4c4c4c', highlightbackground="black", highlightthickness=1)
# button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# # Button to create the plots
# plot_button = ttk.Button(button_frame, text="Plot Data", command=create_plots(), style='Blue.TButton')
# plot_button.pack(side=tk.LEFT, padx=10)

root.mainloop()