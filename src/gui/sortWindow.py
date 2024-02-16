import tkinter as tk
from tkinter import ttk

class SortWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        window_width = 300
        window_height = 200

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.title('Filter')
