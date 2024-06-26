import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()
root.title("Tkinter App with Plots")
# frame = tk.Frame(root)
# frame.pack()
root.configure(bg='#4c4c4c')

font_size = 12

# HF Setting
label1 = tk.Label(root, text="HF Setting", font=('Helvetica', font_size), bg='#4c4c4c', highlightbackground="black", highlightthickness=2, width=60, height=10)
label1.grid(row=0, column=0, columnspan=2)

# LF Setting
label2 = tk.Label(root, text="LF Setting", font=('Helvetica', font_size), bg='#4c4c4c', highlightbackground="black", highlightthickness=2, width=60, height=10)
label2.grid(row=0, column=3, columnspan=2)

# NMR Signal
label3 = tk.Label(root, text="NMR Signal", font=('Helvetica', font_size), bg='#4c4c4c', highlightbackground="black", highlightthickness=2, width=150, height=10)
label3.grid(row=1, column=0, columnspan=5)

# NMR SPectrum
label4 = tk.Label(root, text="NMR Spectrum", font=('Helvetica', font_size), bg='#4c4c4c', highlightbackground="black", highlightthickness=2, width=150, height=10)
label4.grid(row=2, column=0, columnspan=5)

# Pattern Recognition
label5 = tk.Label(root, text="Patern Recognition", font=('Helvetica', font_size), bg='#4c4c4c', highlightbackground="black", highlightthickness=2, width=90, height=10)
label5.grid(row=3, column=0, columnspan=3)

# Run application
label6 = tk.Label(root, text="Run", font=('Helvetica', font_size), bg='#4c4c4c', highlightbackground="black", highlightthickness=2, width=30, height=10)
label6.grid(row=3, column=3)

# Close Application
label7 = tk.Label(root, text="Close", font=('Helvetica', font_size), bg='#4c4c4c', highlightbackground="black", highlightthickness=2, width=30, height=10)
label7.grid(row=3, column=4)

# Material Selection
label8 = tk.Label(root, text="Material Selection", wraplength=1, font=('Helvetica', font_size), bg='#4c4c4c', highlightbackground="black", highlightthickness=2, width=30, height=40)
label8.grid(row=0, rowspan=4, column=5)

# # Create a frame for the buttons
# button_frame = tk.Frame(root, bg='#4c4c4c', highlightbackground="black", highlightthickness=1)
# button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# # Button to create the plots
# plot_button = ttk.Button(button_frame, text="Plot Data", command=create_plots(), style='Blue.TButton')
# plot_button.pack(side=tk.LEFT, padx=10)

# # Button to close the application
# close_button = ttk.Button(button_frame, text="Close", command=root.destroy, style='Red.TButton')
# close_button.pack(side=tk.RIGHT, padx=10)

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

# # Button to close the application
# close_button = ttk.Button(button_frame, text="Close", command=root.destroy, style='Red.TButton')
# close_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()