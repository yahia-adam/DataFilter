from functools import partial
from tkinter import ttk
import tkinter as tk
from filter import filter

class FilterWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__(app)
        window_width = 460
        window_height = 500

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False,True)
        self.title('Filter')
        self.grid()

        self.filters = None

        if app.filtred_datas:
            self.filter_frame = ttk.Frame(self)
            self.create_filter(app)
            self.filter_frame.grid(column=0, row=0)
            self.button_frame = ttk.Frame(self)
            self.button_frame.grid(column=0, row=1)

            self.submit_button = ttk.Button(self.button_frame, text="Submit", command=lambda: self.on_submit(app))
            self.clear_button = ttk.Button(self.button_frame, text="Reset", command=lambda: self.clear_filter(app))
            self.submit_button.grid(column=0, row=0, padx=5, pady=5)
            self.clear_button.grid(column=2, row=0,padx=5, pady=5)

    def create_filter(self, app):
        filters = []
        max_label_width = max(len(key) for key in app.filtred_datas[0].keys())
        for key, value in app.filtred_datas[0].items():
            if type(value) == int:
                frame = ttk.Frame(self.filter_frame, padding=(5, 5, 5, 5), borderwidth=1, relief="solid")
                frame.pack(side=tk.TOP, pady=5)
                f = {'col_name': key, 'min': tk.StringVar(), 'max': tk.StringVar(), 'type': int}
                name_label = ttk.Label(frame, text=f['col_name'] + ' : ', width=max_label_width)
                name_label.pack(side=tk.LEFT, padx=5)
                min_entry = tk.Entry(frame, textvariable=f['min'],width=(20))
                min_entry.pack(side=tk.LEFT, padx=5)
                max_entry = tk.Entry(frame, textvariable=f['max'], width=(20))
                max_entry.pack(side=tk.LEFT, padx=5)
                min_entry.insert(0, 'Min')
                max_entry.insert(0, 'Max')
                min_entry.bind("<FocusIn>", lambda event, entry=min_entry: self.on_focus_in(event, entry, 'Min'))
                min_entry.bind("<FocusOut>", lambda event, entry=min_entry: self.on_focus_out(event, entry, 'Min'))
                max_entry.bind("<FocusIn>", lambda event, entry=max_entry: self.on_focus_in(event, entry, 'Max'))
                max_entry.bind("<FocusOut>", lambda event, entry=max_entry: self.on_focus_out(event, entry, 'Max'))
                filters.append(f)
            elif type(value) == str:
                frame = ttk.Frame(self.filter_frame, padding=(5, 5, 5, 5), borderwidth=1, relief="solid")
                frame.pack(side=tk.TOP, pady=5)
                f = {'col_name': key, 'equal': tk.StringVar(), 'contain': tk.StringVar(), 'type': str}
                name_label = ttk.Label(frame, text=f['col_name'] + ' : ', width=max_label_width)
                name_label.pack(side=tk.LEFT, padx=5)
                equal_entry = tk.Entry(frame, textvariable=f['equal'],  width=(20))
                equal_entry.pack(side=tk.LEFT, padx=5)
                contain_entry = tk.Entry(frame, textvariable=f['contain'],  width=(20))
                contain_entry.pack(side=tk.LEFT, padx=5)
                equal_entry.insert(0, 'Equal')
                contain_entry.insert(0, 'Contain')
                equal_entry.bind("<FocusIn>", lambda event, entry=equal_entry: self.on_focus_in(event, entry, 'Equal'))
                equal_entry.bind("<FocusOut>", lambda event, entry=equal_entry: self.on_focus_out(event, entry, 'Equal'))
                contain_entry.bind("<FocusIn>", lambda event, entry=contain_entry: self.on_focus_in(event, entry, 'Contain'))
                contain_entry.bind("<FocusOut>", lambda event, entry=contain_entry: self.on_focus_out(event, entry, 'Contain'))
                filters.append(f)
            elif type(value) == list:
                frame = ttk.Frame(self.filter_frame, padding=(5, 5, 5, 5), borderwidth=1, relief="solid")
                frame.pack(side=tk.TOP, pady=5)
                f = {'col_name': key, 'len_equal': tk.StringVar(), 'contain': tk.StringVar(), 'type': list}
                name_label = ttk.Label(frame, text=f['col_name'] + ' : ', width=max_label_width)
                name_label.pack(side=tk.LEFT, padx=5)
                len_equal_entry = tk.Entry(frame, textvariable=f['len_equal'],  width=(20))
                len_equal_entry.pack(side=tk.LEFT, padx=5)
                contain_entry = tk.Entry(frame, textvariable=f['contain'], width=(20))
                contain_entry.pack(side=tk.LEFT, padx=5)
                len_equal_entry.insert(0, 'Length Equal')
                contain_entry.insert(0, 'Contain')
                len_equal_entry.bind("<FocusIn>", lambda event, entry=len_equal_entry: self.on_focus_in(event, entry, 'Length Equal'))
                len_equal_entry.bind("<FocusOut>", lambda event, entry=len_equal_entry: self.on_focus_out(event, entry, 'Length Equal'))
                contain_entry.bind("<FocusIn>", lambda event, entry=contain_entry: self.on_focus_in(event, entry, 'Contain'))
                contain_entry.bind("<FocusOut>", lambda event, entry=contain_entry: self.on_focus_out(event, entry, 'Contain'))
                filters.append(f)
            elif type(value) == bool:
                frame = ttk.Frame(self.filter_frame, padding=(5, 5, 5, 5), borderwidth=1, relief="solid")
                frame.pack(side=tk.TOP, pady=5)
                f = {'col_name': key, 'value': tk.StringVar(), 'type': bool}
                name_label = ttk.Label(frame, text=f['col_name'] + ' : ', width=max_label_width)
                name_label.pack(side=tk.LEFT, padx=5)
                value_options = ['True', 'False']
                value_combobox = ttk.Combobox(frame, values=value_options, textvariable=f['value'], state="readonly", width=(41))
                value_combobox.pack(side=tk.LEFT, padx=5)
                filters.append(f)
            else:
                continue

        self.filters = filters

    def on_focus_in(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(foreground='black')

    def on_focus_out(self, event, entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(foreground='grey')
        
    def on_submit(self, app):
        for f in self.filters:
            # if f['type'] == int:
            #     print(f['col_name'])
            #     print(f['min'].get())
            #     print(f['max'].get())
            if f['type'] == str:
                col_name = f['col_name']
                col_equal = f['equal'].get() 
                col_contain = f['contain'].get()
                if (col_equal != "Equal"):
                    app.filtred_datas = filter.equals(app.filtred_datas, 'json', col_name, col_equal)
                if col_contain != "Contain":
                    app.filtred_datas = filter.contains(app.filtred_datas, 'json', col_name, col_contain)
            if f['type'] == bool:
                col_name = f['col_name']
                col_equal = f['value'].get()
                if col_equal == "True":
                    app.filtred_datas = filter.equals(app.filtred_datas, 'json', col_name, True)
                if col_equal == "False":
                    app.filtred_datas = filter.equals(app.filtred_datas, 'json', col_name, False)
            # if f['type'] == list:
            #     col_name = f['col_name']
            #     col_equal = f['value'].get()
            #     if col_equal == "True":
            #         app.filtred_datas = filter.equals(app.filtred_datas, 'json', col_name, True)
            #     if col_equal == "False":
            #         app.filtred_datas = filter.equals(app.filtred_datas, 'json', col_name, False)
            
            app.create_tree_widget(app.filtred_datas)
        self.destroy()
    def clear_filter(self, app):
        app.filtred_datas = app.initial_datas
        app.create_tree_widget(app.filtred_datas)
        self.destroy()
