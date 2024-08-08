import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import random
import mss

from nmr_signal import nmr_signal_generator
from nmr_spectrum import nmr_spectrum_compiler
from tf_model import load_pattern_search
from tf_model import predict


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

# Pattern Search
pattern_search = load_pattern_search()

# Screen Grab
screen_grab = False

class NMRApp:
    def __init__(self, root):
        bg_color = '#4c4c4c'
        self.plt_color = '#5a5a5a'

        self.root = root
        self.root.title("NMR App")
        self.root.configure(bg=bg_color)

        self.style = ttk.Style()
        self.style.configure('Red.TButton', 
                        background='#fa1505', # Red
                        font=('Helvetica', 20),
                        padding=6)
        self.style.map('Red.TButton',
                       foreground=[('active', '#fa1505')])

        font_size = 12

        HF_setting = 16.0000
        LF_setting = 27
        
        # HF Setting
        self.label1 = tk.Label(self.root, text=f"HF Setting: {HF_setting:.4f}MHz", font=('Courier', 36), bg=bg_color)
        self.label1.grid(row=0, column=0, columnspan=2)

        # LF Setting
        self.label2 = tk.Label(self.root, text=f"LF Setting: {LF_setting}Hz", font=('Courier', 36), bg=bg_color)
        self.label2.grid(row=0, column=3, columnspan=2)

        # NMR Signal
        self.frame3 = ttk.Frame(self.root)
        self.frame3.grid(row=1, column=0, columnspan=5)
        # Create NMR Signal Plot
        self.fig_sig = Figure(figsize=(13.5, 2), dpi=100)
        self.fig_sig.patch.set_facecolor(bg_color)
        self.fig_sig.tight_layout()
        self.ax_sig = self.fig_sig.add_subplot(111)
        self.ax_sig.set_ylabel("NMR Signal")
        self.ax_sig.set_facecolor(self.plt_color)
        self.ax_sig.grid(True)
        self.ax_sig.set_xlim([0, 5/28])
        self.ax_sig.set_ylim([0, 4])
        # Embed the plot in the Tkinter frame
        self.canvas_sig = FigureCanvasTkAgg(self.fig_sig, master=self.frame3)
        self.canvas_widget_sig = self.canvas_sig.get_tk_widget()
        self.canvas_widget_sig.grid(row=0, column=0)

        # NMR SPectrum
        self.frame4 = tk.Frame(self.root)
        self.frame4.grid(row=2, column=0, columnspan=5)
        # Create NMR Spectrum Plot
        self.fig_spec = Figure(figsize=(13.5, 2), dpi=100)
        self.fig_spec.patch.set_facecolor(bg_color)
        self.fig_spec.tight_layout()
        self.ax_spec = self.fig_spec.add_subplot(111)
        self.ax_spec.set_ylabel("NMR Spectrum")
        self.ax_spec.set_facecolor(self.plt_color)
        self.ax_spec.grid(True)
        self.ax_spec.set_xlim([16, 20])
        self.ax_spec.set_ylim([0, 4])
        # Embed the plot in the Tkinter frame
        self.canvas_spec = FigureCanvasTkAgg(self.fig_spec, master=self.frame4)
        self.canvas_widget_spec = self.canvas_spec.get_tk_widget()
        self.canvas_widget_spec.grid(row=0, column=0)

        # Pattern Recognition
        self.frame5 = tk.Frame(self.root)
        self.frame5.grid(row=3, column=0, columnspan=3)
        x = [1, 2, 3, 4, 5]
        pattern_rec = np.random.rand(5)
        self.fig_pat = Figure(figsize=(7, 2), dpi=100)
        self.fig_pat.patch.set_facecolor(bg_color)
        self.fig_pat.tight_layout()
        self.ax_pat = self.fig_pat.add_subplot(111)
        self.ax_pat.set_xlim([0.4, 5.6])
        self.ax_pat.set_ylim([0, 1])
        self.ax_pat.set_title(f"Guess: ", x=1.3, y=0.5)
        self.ax_pat.set_facecolor(self.plt_color)
        # fig3 = bar(name="Pattern Recognition", x=x, y=pattern_rec)
        self.canvas_pat = FigureCanvasTkAgg(self.fig_pat, master=self.frame5)
        self.canvas_widget_pat = self.canvas_pat.get_tk_widget()
        self.canvas_widget_pat.grid(row=0, column=0)
        
        # Material Guess
        self.label6 = tk.Label(self.root, text=f"Guess: Material {np.argmax(pattern_rec) + 1}\nConfidence: {pattern_rec[np.argmax(pattern_rec)]*100:.1f}%", font=('Helvetica', 25), bg=bg_color)#, width=30, height=10)
        self.label6.grid(row=3, column=3)

        # Buttons for Application
        self.label7 = tk.Label(self.root, font=('Helvetica', font_size), bg=bg_color, width=30, height=10)
        self.label7.grid(row=3, column=5)
        self.run_button = ttk.Button(self.label7, text="Run", command=self.nmr_function, style='Red.TButton')
        self.run_button.grid(ipady=10, ipadx=10, pady=20)
        self.close_button = ttk.Button(self.label7, text="Close", command=self.root.destroy, style='Red.TButton')
        self.close_button.grid(ipady=10, ipadx=10, pady=20)

        # Material Selection
        self.label7 = tk.Label(self.root, text=f"Material Selection:", font=('Helvetica', 20), bg=bg_color, width=30, height=10)
        self.label7.grid(row=1, column=5, sticky="S")
        self.options = [1,2,3,4,5]
        self.selected_option = tk.IntVar()
        self.drop_list = ttk.Combobox(self.root, textvariable=self.selected_option, values=self.options, state='readonly', font=("Helvetica",20))
        self.drop_list.grid(row=2, column=5, sticky="N", ipady=10)
        self.drop_list.current(0)  # Set the default selected option


    # NMR function
    def nmr_function(self):

        HF_setting = 15.75
        # HF_setting = 17.7
        nmr_spectrum = np.zeros([3, 1200])
        nmr_spectrum[0,:] = np.linspace(16, 20, num=1200)

        num_scanned = 0

        while HF_setting <= 20:
        # for i in range(10):

            # Update the HF setting display
            self.label1.config(text=f"HF Setting: {HF_setting:.4f}MHz")

            # Add Randomization of the HF Setting
            HF_actual = HF_setting + ((random.random()-.5)/50)

            # Generate NMR Signal
            x, lf_signal, nmr_signal = nmr_signal_generator(material=materials[self.selected_option.get()-1], HF_actual=HF_actual)
            
            # Plot NMR Signal
            self.plot_nmr_signal(x=x, y=[lf_signal*2-0.5, nmr_signal], plot_rgb=["#4976fc", "#ff4f4d"])
            self.root.after(50)

            # Generate NMR Spectrum
            nmr_spectrum = nmr_spectrum_compiler(
                NMR_spectrum=nmr_spectrum,
                NMR_signal=nmr_signal,
                LF_signal=lf_signal,
                HF_setting=HF_actual,
                time=x
            )

            # Plot NMR Spectrum
            self.plot_nmr_spectrum(x=np.linspace(16, 20, 1200), y=nmr_spectrum[1], plot_rgb="#02edaf")
            self.root.after(50)
            # if screen_grab:
            #     self.setting = int(HF_setting * 1000)
            #     self.num = 1
            #     self.take_screenshot()

            # Generate Pattern Search
            material_list = [1, 2, 3, 4, 5]
            random_guess = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
            pattern_rec = predict(model=pattern_search, input=nmr_spectrum[1])
            while num_scanned < 1200 and nmr_spectrum[1,num_scanned] > 0:
                num_scanned += 1
            scanned_percent = num_scanned/len(nmr_spectrum[0])
            guess = random_guess*(1-scanned_percent) + pattern_rec*scanned_percent

            # Plot Pattern Recognition
            self.plot_pattern_recognition(x=material_list, y=guess)
            # if screen_grab:
            #     self.setting = int(HF_setting * 1000)
            #     self.num = 2
            #     self.take_screenshot()

            # Update the Pattern Recognition display
            self.label6.config(text=f"Guess: Material {np.argmax(guess) + 1}\nConfidence: {guess[np.argmax(guess)]*100:.1f}%")
            self.root.after(50)
            if screen_grab:
                self.setting = int(HF_setting * 1000)
                self.num = 3
                self.take_screenshot()

            HF_setting += .03125

    # Plot the NMR Signal
    def plot_nmr_signal(self, x, y, plot_rgb):
        # Create a Matplotlib figure
        self.ax_sig.clear()
        for i in range(len(y)):
            self.ax_sig.plot(x, y[i], color=plot_rgb[i])
        self.ax_sig.set_xlim([x[0], x[-1]])
        self.ax_sig.set_ylim([0, 4])
        self.ax_sig.set_ylabel("NMR Signal")
        self.ax_sig.set_facecolor(self.plt_color)
        self.ax_sig.grid(True)
        self.canvas_sig.draw()
        self.root.update_idletasks()

    # Plot the NMR Spectrum
    def plot_nmr_spectrum(self, x, y, plot_rgb):
        # Create a Matplotlib figure
        self.ax_spec.clear()
        self.ax_spec.plot(x, y, color=plot_rgb)
        self.ax_spec.set_xlim([x[0], x[-1]])
        self.ax_spec.set_ylim([0, 4])
        self.ax_spec.set_ylabel("NMR Signal")
        self.ax_spec.set_facecolor(self.plt_color)
        self.ax_spec.grid(True)
        self.canvas_spec.draw()
        self.root.update_idletasks()

    # Plot the Patern Recognition Result
    def plot_pattern_recognition(self, x, y):
        # Create a Matplotlib figure
        material_guess = np.argmax(y) + 1
        self.ax_pat.clear()
        self.ax_pat.bar(x, y, width=1, edgecolor="#000000")
        self.ax_pat.set_xlim([0.4, 5.6])
        self.ax_pat.set_ylim([0, 1])
        self.ax_pat.set_title(f"Guess: Material {material_guess}", x=1.3, y=0.5)
        self.ax_pat.set_facecolor(self.plt_color)
        self.canvas_pat.draw()
        self.root.update_idletasks()

    def take_screenshot(self):
        with mss.mss() as sct:

            # The screen part to capture
            monitor = {"top": 20, "left": 20, "width": 2000, "height": 900}
            output = f"figures/screenshots/sct_{self.setting}_{self.num}.png".format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            # print(output)


if __name__ == "__main__":
    root = tk.Tk()
    app = NMRApp(root)
    root.mainloop()