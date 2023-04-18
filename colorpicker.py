import tkinter as tk

def update_color(r, g, b):
    color = '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))
    color_canvas.configure(bg=color)

root = tk.Tk()
root.title('Color Picker')

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

r_var = tk.DoubleVar()
r_slider = tk.Scale(frame, from_=0, to=255, orient='horizontal', label='R', variable=r_var, command=lambda value: update_color(r_var.get(), g_var.get(), b_var.get()))
r_slider.pack(padx=10, pady=10)

g_var = tk.DoubleVar()
g_slider = tk.Scale(frame, from_=0, to=255, orient='horizontal', label='G', variable=g_var, command=lambda value: update_color(r_var.get(), g_var.get(), b_var.get()))
g_slider.pack(padx=10, pady=10)

b_var = tk.DoubleVar()
b_slider = tk.Scale(frame, from_=0, to=255, orient='horizontal', label='B', variable=b_var, command=lambda value: update_color(r_var.get(), g_var.get(), b_var.get()))
b_slider.pack(padx=10, pady=10)

color_canvas = tk.Canvas(frame, width=100, height=100)
color_canvas.pack(padx=10, pady=10)

root.mainloop()
