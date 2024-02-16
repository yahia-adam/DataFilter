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
            command=lambda: self.read_set_app_data(app)
        )
        self.file_menu.add_command(label='Save')
        self.file_menu.add_command(label='Save as', command=self.file_as_save)
        self.file_menu.add_command(label='Close')
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Exit",
            command=app.destroy,
        )
    
    def read_set_app_data(self, app):
        filetypes = (
            ('json files', '*.json'),
            ('csv files', '*.csv')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='./datas/inputs',
            filetypes=filetypes)
        datas = FileData(upload_file(filename))
        app.file_name = filename
        app.datas = datas
        app.filtered_datas = datas
    
    def file_as_save(self):
        f = fd.asksaveasfile(mode='w',
            initialdir="./datas/outputs",
            defaultextension=".json")
        if f is None:
            return
        f.close()
        print(f.name())
