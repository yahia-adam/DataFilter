from tkinter import Menu, filedialog as fd
from upload.upload_file import upload_file
from gui.root import App
from fileData.filedata import FileData
import tkinter as tk
from tkinter import *

class AppMenu(Menu):
    def __init__(self, app: App):
        super().__init__(app)
        app.config(menu=self)
        self.file_menu = Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(
            label='Open',
            command=lambda: self.select_file(app)
        )
        self.file_menu.add_command(label='Save')
        self.file_menu.add_command(label='Save as', command=self.file_as_save)
        self.file_menu.add_command(label='Close')
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Exit",
            command=app.destroy,
        )
    
    def select_file(self, app):
        filetypes = (
                ('CSV files', '*.csv'),
                ('JSON files', '*.json'),
                ('All files', '*.*')
            )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='./datas',
            filetypes=filetypes
        )
        datas = upload_file(filename)
        app.file_name = filename
        app.initial_datas = datas
        app.filtred_datas = datas
        app.create_tree_widget(datas)

    def file_as_save(self):
        f = fd.asksaveasfile(mode='w',
            initialdir="./datas/outputs",
            defaultextension=".json")
        
        f.close()
        print(f.name())
