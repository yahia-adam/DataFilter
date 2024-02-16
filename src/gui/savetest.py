'''
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from tkinter import Menu

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('-- Data Filter --')
        self.geometry('620x200')
        self.grid()

        self.menu = self.create_menu()
        self.tree = self.create_tree_widget()

    def create_menu(self):
        # create a menubar
        menubar = Menu(self)
        self.config(menu=menubar)
        # create the file_menu
        file_menu = Menu(
            menubar,
            tearoff=0
        )
        # add menu items to the File menu
        file_menu.add_command(
            label='Open',
            command=self.select_file
        )
        file_menu.add_command(label='Save')
        file_menu.add_command(label='Save as')
        file_menu.add_command(label='Close')
    
        # add Exit menu item
        file_menu.add_separator()
        file_menu.add_command(
            label='Exit',
            command=self.destroy
        )
        menubar.add_cascade(
            label="File",
            menu=file_menu,
            underline=0
        )
        # create the Help menu
        help_menu = Menu(
            menubar,
            tearoff=0
        )
        help_menu.add_command(label='Welcome')
        help_menu.add_command(label='About...')
        # add the Help menu to the menubar
        menubar.add_cascade(
            label="Help",
            menu=help_menu,
            underline=0
        )

    def select_file(self):
        filetypes = (
            ('json files', '*.json'),
            ('csv files', '*.csv')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)


    def create_tree_widget(self):
        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        tree.bind('<<TreeviewSelect>>', self.item_selected)
        tree.grid(row=1, column=0, columnspan=len(columns))

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=len(columns) +1, sticky='ns')

        # generate sample data
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        for contact in contacts:
            tree.insert('', tk.END, values=contact)

        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))


        self.mystr = tk.StringVar()
        label = tk.Label(self, textvariable=self.mystr)
        self.mystr.set("hello world!")
        label.pack()
        btn = tk.Button(self, text="btn", command=self.add_number)
        btn.pack()
        self.number = 0

    def get_mystr(self):
        return self.mystr()
    def set_mystr(self, mystr):
        self.mystr.set(mystr)

    def add_number(self):
        self.number = self.number + 1
        self.set_mystr(str(self.number))


# from tkinter import *
# from tkinter import ttk
# import threading
# import time

# def fun():
#     for i in range(10):
#         var.set(var.get() + 1)
#         x = tree.get_children()
#         tree.item(x, text = 'Number', values = var.get())
#         time.sleep(.5)
        
# t = threading.Thread(target=fun)

# root = Tk()

# var = IntVar()
# var.set(0)

# mainframe = ttk.Frame(root)
# mainframe.grid(column = 0, row = 0)

# tree = ttk.Treeview(mainframe, columns = ('number'), height = 1)

# tree.insert('', 'end', text = 'Number', values = var.get())
# tree.grid(column=0, row=0)

# t.start()
# root.mainloop()
        

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3",
        )
        style.map('Treeview',
            background=[('selected', 'bleu')]
        )

https://www.pythontutorial.net/tkinter/tkinter-event-binding/
https://www.pythontutorial.net/tkinter/tkinter-notebook/
https://www.pythontutorial.net/tkinter/tkinter-askyesno/
window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
'''

import tkinter as tk
from tkinter import *
from tkinter import Menu, filedialog as fd
def donothing():
   pass

def file_save():
    f = fd.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close() # `()` was missing.

root = Tk()
root.geometry("500x500")
menubar=Menu(root)
text=Text(root)
text.pack()
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Help",command=donothing)
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar)
root.mainloop() 