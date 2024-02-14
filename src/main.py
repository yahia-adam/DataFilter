from outils import read_file
from gui import root
import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    app = root.App()

    app.menu = app.create_menu()
    app.tree = app.create_tree_widget()

    app.mainloop()