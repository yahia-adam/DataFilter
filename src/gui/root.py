import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from tkinter import Menu

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('-- Data Filter --')

        self.datas = []
        self.filtred_datas = []

if __name__ == "__main__":
    app = App()
    app.mainloop()
