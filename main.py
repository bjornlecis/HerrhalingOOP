import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

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
    app.mainloop()
