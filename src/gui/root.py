import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from upload.upload_file import upload_file
from gui.filterWindow import FilterWindow
from gui.sortWindow import SortWindow
from stats.state import calculate_stats

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title('-- Data Filter --')
        self.geometry(f'{800}x{800}')
        # self.resizable(False,False)
        self.grid()

        # Variables
        self.initial_datas = []
        self.filtred_datas = []
        self.filters = []
        self.sorts = []
    
        # Frame pour les boutons
        self.btn_frame = tk.Frame(self)
        
        self.sort_btn = tk.Button(self.btn_frame, text="Sort", command=self.open_sort_window)
        self.filter_btn = tk.Button(self.btn_frame, text="Filter", command=self.open_filter_window)
        
        self.sort_btn.pack(side=tk.LEFT)
        self.filter_btn.pack(side=tk.RIGHT)
        
        self.btn_frame.grid(column=0, row=0)

        # Tree view
        self.tree_widget = None
        self.tree_frame = tk.Frame(self)
        self.tree_frame.grid(column=0, row=1)

    def create_tree_widget(self, datas):
        # print(datas)
        if (self.tree_widget != None):
            self.clear_tree_frame()
        columns = list(datas[0].keys())
        self.tree_widget = ttk.Treeview(self.tree_frame, columns=columns, show="headings")
        for col in columns:
            self.tree_widget.heading(col, text=col)
            self.tree_widget.column(col, anchor="center")

        values = []
        for c in columns:
            values.append(str(calculate_stats(datas, c, type(datas[0][c]))))
        self.tree_widget.insert('', 'end', values=values)
    
        for item in datas:
            values = [str(item[col]) for col in columns]
            self.tree_widget.insert('', 'end', values=values)
        self.tree_widget.pack(expand=True, fill=tk.BOTH)

    def open_filter_window(self):
        fw = FilterWindow(self)
        fw.grab_set()
    def open_sort_window(self):
        sw = SortWindow(self)
        sw.grab_set()

    def clear_tree_frame(self):
        for widget in self.tree_frame.winfo_children():
            widget.destroy()
