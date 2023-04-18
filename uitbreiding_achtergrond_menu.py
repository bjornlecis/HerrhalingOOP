import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the menu background color to navy blue
        self.option_add('*Menu.background', 'navy')

        # Set the menu item foreground color to white
        self.option_add('*Menu.foreground', 'white')

        # Create the menu bar
        menu = tk.Menu(self)
        self.config(menu=menu)

        # Create the "File" menu
        file_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.quit)

        # Create the "Screens" menu
        screens_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Screens", menu=screens_menu)
        screens_menu.add_command(label="Screen 2", command=self.show_screen_2)
        screens_menu.add_command(label="Screen 3", command=self.show_screen_3)

        # Create the "Color" menu
        color_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Color", menu=color_menu)
        color_menu.add_command(label="Blue", command=lambda: self.set_background_color("#00BFFF"))
        color_menu.add_command(label="Red", command=lambda: self.set_background_color("#FF4500"))
        color_menu.add_command(label="Green", command=lambda: self.set_background_color("#00FF00"))
        color_menu.add_command(label="Pink", command=lambda: self.set_background_color("#FF69B4"))
        color_menu.add_command(label="Orange", command=lambda: self.set_background_color("#FFA500"))

        # Set the initial background color
        self.set_background_color("#FFFFFF")

    def set_background_color(self, color):
        # Set the background color of the main window
        self.configure(background=color)

    def show_screen_2(self):
        # Create a new window for screen 2
        screen_2_window = tk.Toplevel(self)
        tk.Label(screen_2_window, text="Test").pack()

    def show_screen_3(self):
        # Create a new window for screen 3
        screen_3_window = tk.Toplevel(self)
        tk.Label(screen_3_window, text="Test").pack()

if __name__ == "__main__":
    app = Application()

    # Set the menu item hover background color to yellow
    app.option_add('*Menu.activeBackground', 'yellow')

    app.mainloop()
