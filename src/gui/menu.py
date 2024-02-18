from tkinter import Menu, filedialog as fd
from upload.upload_file import upload_file
from gui.root import App
import tkinter as tk
from tkinter import *
from save import save_file

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
        self.file_menu.add_command(label='Save', command=lambda: self.save_file(app))
        self.file_menu.add_command(label='Save as', command=lambda: self.save_sa_file(app))
        self.file_menu.add_command(label='Close')
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Exit",
            command=app.destroy,
        )
    
    def select_file(self, app):

        allowed_filetypes = [('JSON files', '*.json'),('CSV files', '*.csv'),('YAML files', '*.yaml')]

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='./datas',
            filetypes=allowed_filetypes
        )
        if filename:
            datas = upload_file(filename)
            app.file_name = filename
            app.initial_datas = datas
            app.filtred_datas = datas
            app.create_tree_widget(datas)

    def save_sa_file(self, app):
        allowed_filetypes = [('JSON files', '*.json'),('CSV files', '*.csv'),('YAML files', '*.yaml')]
        f = fd.asksaveasfile(mode='w',
            initialdir="./datas/outputs",
            defaultextension=".json",
            filetypes=allowed_filetypes,
        )
        save_file.save_sa_file(filepath=f.name, datas=app.filtred_datas)
        f.close()

    def save_file(self, app):
        if (app.file_name and app.filtred_datas):
            save_file.save_sa_file(filepath=app.file_name, datas=app.filtred_datas)
