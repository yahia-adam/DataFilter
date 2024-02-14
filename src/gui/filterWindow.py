import tkinter as tk
from tkinter import ttk, TclError


def create_Button(app):
    frame = ttk.Frame(app)
        
    frame.grid()

    findNext = tk.Button(
        frame,        
        text="Find Next"
    )
    replace = tk.Button(
        frame,        
        text="Replace"
    )
    replaceAll = tk.Button(
        frame,        
        text="Replace All"
    )

    cancel = tk.Button(
        frame,        
        text="Cancel"
    )

    findNext.grid(row=0,column=0)
    replace.grid(row=1,column=0)
    replaceAll.grid(row=2,column=0)
    cancel.grid(row=3,column=0)
    
    return frame


def create_input_fram(app):
    frame = ttk.Frame()
    frame.grid()

    findWhat = ttk.Label(frame, text="Find What")
    replaceWith = ttk.Label(frame, text="Replace With")
    matchCase = ttk.Checkbutton(frame, textvariable="Math Case")
    wrapAround = ttk.Checkbutton(frame, textvariable="Wrap Around")

    findWhatInput = ttk.Entry()
    replaceWithInput = ttk.Entry()

    findWhat.grid(row=0, column=0)
    replaceWith.grid(row=1,column=0)
    matchCase.grid(row=2, column=0)
    wrapAround.grid(row=3,column=0)

    findWhatInput.grid(row=0, column=1)
    replaceWithInput.grid(column=1,row=1)

    return frame

if __name__ == "__main__":
    app = tk.Tk()
    inputframe = create_input_fram(app)
    # frame = create_Button(app)
    app.mainloop()