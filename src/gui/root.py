import tkinter as tk
from tkinter import ttk
from fileData.filedata import FileData
from tkinter.messagebox import showinfo
from upload.upload_file import upload_file

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title('-- Data Filter --')
        self.grid()
        self.resizable(False,False)
        # Variables
        self.datas = FileData([])
        self.filtered_datas = FileData(upload_file("/home/adam/Documents/esgi/DataFilter/datas/inputs/json/students.json"))
        self.file_name = ""

        # Frame pour les boutons
        btn_frame = tk.Frame(self)
        sort_btn = tk.Button(btn_frame, text="Sort")
        filter_btn = tk.Button(btn_frame, text="Filter")
        sort_btn.pack(side=tk.LEFT)
        filter_btn.pack(side=tk.RIGHT)
        btn_frame.grid(column=0, row=0)

        # Frame pour le tableau
        tab_frame = tk.Frame(self)
        columns = tuple(self.filtered_datas.get_columns_name())
        self.tree = ttk.Treeview(tab_frame, height=30, columns=columns, show='headings')
        for c in columns:
            self.tree.heading(c, text=c)
        for data in self.filtered_datas.datas:
            data = (tuple(str(value) for value in data.values()))
            self.tree.insert('', tk.END, values=data)
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        self.tree.grid(row=0, column=0, sticky='nsew')
        scrollbar = ttk.Scrollbar(tab_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        tab_frame.grid(column=0, row=1)

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            showinfo(title='Information', message=','.join(record))
