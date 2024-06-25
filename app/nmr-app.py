import tkinter as tk

root = tk.Tk()
root.title("Tkinter App")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=root.destroy)
button.pack(pady=20)

root.mainloop()