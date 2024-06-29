import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import random

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


class NMRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NMR App")
        self.root.configure(bg='#4c4c4c')

        font_size = 12
        bg_color = '#4c4c4c'

        HF_setting = 16.0000
        LF_setting = 27
        
        # HF Setting
        self.label1 = tk.Label(self.root, text=f"HF Seeting: {HF_setting:.4f}MHz", font=('Courier', 36), bg=bg_color)
        self.label1.grid(row=0, column=0, columnspan=2)

        # LF Setting
        self.label2 = tk.Label(self.root, text=f"LF Setting: {LF_setting}Hz", font=('Courier', 36), bg=bg_color)
        self.label2.grid(row=0, column=3, columnspan=2)

        # NMR Signal
        self.frame3 = ttk.Frame(self.root)
        self.frame3.grid(row=1, column=0, columnspan=5)
        # Create NMR Signal
        x = np.linspace(0, 5/28, 2000)
        lf_signal = np.zeros(len(x))
        nmr_signal = np.zeros(len(x))
        # Plot NMR Signal
        fig = plot(name="NMR Signal", x=x, y=[lf_signal, nmr_signal], plot_rgb=["#4976fc", "#ff4f4d"])
        # Embed the plot in the Tkinter frame
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame3)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)

        # NMR SPectrum
        self.frame4 = tk.Frame(self.root)
        self.frame4.grid(row=2, column=0, columnspan=5)
        # Create NMR Spectrum
        x = np.linspace(16, 20, 1200)
        nmr_spectrum = np.zeros(len(x))
        # Plot NMR Spectrum
        fig2 = plot(name="NMR Spectrum", x=x, y=[nmr_spectrum], plot_rgb=["#02edaf"])
        # Embed the plot in the Tkinter frame
        self.canvas = FigureCanvasTkAgg(fig2, master=self.frame4)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)

        # Pattern Recognition
        self.frame5 = tk.Frame(self.root)
        self.frame5.grid(row=3, column=0, columnspan=3)
        x = [1, 2, 3, 4, 5]
        pattern_rec = np.random.rand(5)
        fig3 = bar(name="Pattern Recognition", x=x, y=pattern_rec)
        self.canvas = FigureCanvasTkAgg(fig3, master=self.frame5)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)

        # Material Guess
        self.label6 = tk.Label(self.root, text=f"Guess: Material {np.argmax(pattern_rec) + 1}", font=('Helvetica', 25), bg=bg_color)#, width=30, height=10)
        self.label6.grid(row=3, column=3)

        # Buttons for Application
        self.label7 = tk.Label(self.root, font=('Helvetica', font_size), bg=bg_color, width=30, height=10)
        self.label7.grid(row=3, column=4)
        self.run_button = ttk.Button(self.label7, text="Run", command=self.nmr_function, style='Red.TButton')
        self.run_button.grid(ipady=10, ipadx=10, pady=20)
        self.close_button = ttk.Button(self.label7, text="Close", command=self.root.destroy, style='Red.TButton')
        self.close_button.grid(ipady=10, ipadx=10, pady=20)

        # Material Selection
        self.label8 = tk.Label(self.root, text="Material Selection", wraplength=1, font=('Helvetica', font_size), bg=bg_color, highlightbackground="black", highlightthickness=2, width=30, height=40)
        self.label8.grid(row=0, rowspan=4, column=5)

    # NMR function
    def nmr_function(self):

        HF_setting = 15.75

        # while HF_setting <= 20:
        for i in range(5):

            # Add Randomization of the HF Setting
            HF_actual = HF_setting + ((random.random()-.5)/50)

            # Generate NMR Signal
            x, lf_signal, nmr_signal = nmr_signal_generator(material=materials[4], HF_actual=HF_actual)
            
            # Plot NMR Signal
            fig = plot(name="NMR Signal", x=x, y=[lf_signal*2-0.5, nmr_signal], plot_rgb=["#4976fc", "#ff4f4d"])
            self.canvas = FigureCanvasTkAgg(fig, master=self.frame3)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=0, column=0)

            HF_setting += .03125

            self.root.after(500)

if __name__ == "__main__":
    root = tk.Tk()
    app = NMRApp(root)
    root.mainloop()