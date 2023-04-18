import tkinter as tk

def calculate_area():
    width = width_var.get()
    height = height_var.get()
    area = width * height
    result_label.config(text="Area: {}".format(area))

root = tk.Tk()
root.title("Rectangle Area Calculator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

width_label = tk.Label(frame, text="Width")
width_label.grid(row=0, column=0)

width_var = tk.IntVar()
width_slider = tk.Scale(frame, from_=0, to=100, orient="horizontal", variable=width_var, command=lambda value: width_entry.delete(0, tk.END) or width_entry.insert(0, value))
width_slider.grid(row=0, column=1)

width_entry = tk.Entry(frame)
width_entry.grid(row=0, column=2)

height_label = tk.Label(frame, text="Height")
height_label.grid(row=1, column=0)

height_var = tk.IntVar()
height_slider = tk.Scale(frame, from_=0, to=100, orient="horizontal", variable=height_var, command=lambda value: height_entry.delete(0, tk.END) or height_entry.insert(0, value))
height_slider.grid(row=1, column=1)

height_entry = tk.Entry(frame)
height_entry.grid(row=1, column=2)

calculate_button = tk.Button(frame, text="Calculate", command=calculate_area)
calculate_button.grid(row=2, column=0, columnspan=3)

result_label = tk.Label(frame)
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
