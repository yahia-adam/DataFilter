import tkinter as tk
from tkinter import ttk
from sort import sort
class SortWindow(tk.Toplevel):
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
        self.title('Sort')
        self.grid()

        self.sorts = None

        if app.filtred_datas:
            self.filter_frame = ttk.Frame(self)
            self.create_filter(app)
            self.filter_frame.grid(column=0, row=0)
            self.button_frame = ttk.Frame(self)
            self.button_frame.grid(column=0, row=1)

            self.submit_button = ttk.Button(self.button_frame, text="Submit", command=lambda: self.on_submit(app))
            self.clear_button = ttk.Button(self.button_frame, text="Reset", command=lambda: self.clear_sort(app))
            self.submit_button.grid(column=0, row=0, padx=5, pady=5)
            self.clear_button.grid(column=2, row=0,padx=5, pady=5)

    def create_filter(self, app):
        sorts = []
        max_label_width = max(len(key) for key in app.filtred_datas[0].keys())
        for key, value in app.filtred_datas[0].items():
            if type(value) == int:
                value_options = ['Ascending', 'Descending']                
            elif type(value) == str:
                value_options = ['ascending alphabetical order', 'descending alphabetical order']                
            elif type(value) == list:
                value_options = ['ascending by length', 'descending by length']                
            elif type(value) == bool:
                value_options = ['ascending with True first', 'descending with False first']                
            else:
                continue

            frame = ttk.Frame(self.filter_frame, padding=(5, 5, 5, 5), borderwidth=1, relief="solid")
            frame.pack(side=tk.TOP, pady=5)
            f = {'col_name': key, 'sort': tk.StringVar(), 'value': tk.StringVar(), 'type': int}
            name_label = ttk.Label(frame, text=f['col_name'] + ' : ', width=max_label_width)
            name_label.pack(side=tk.LEFT, padx=5)
            sort = tk.Checkbutton(frame, textvariable=f['sort'], onvalue="True", offvalue="False", width=(5))
            sort.pack(side=tk.LEFT, padx=5)
            value = ttk.Combobox(frame, values=value_options, textvariable=f['value'], state="readonly", width=(30))
            value.pack(side=tk.LEFT, padx=5)
            sorts.append(f)

        self.sorts = sorts

    def on_focus_in(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(foreground='black')

    def on_focus_out(self, event, entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(foreground='grey')
        
    def on_submit(self, app):
        for s in self.sorts:
            if (s['sort'].get() == "True"):
                value  = s['value'].get()
                app.filtred_datas = sort.sort(app.filtred_datas, 'json', )
        # app.create_tree_widget(app.filtred_datas)
        self.destroy()
    def clear_sort(self, app):
        app.filtred_datas = app.initial_datas
        app.create_tree_widget(app.filtred_datas)
        self.destroy()
