from tkinter import *
from functools import partial



class FilterWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        window_width = 300
        window_height = 200
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.title('Filter')

        # Username label and text entry box
        usernameLabel = Label(self, text="User Name").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(self, textvariable=username).grid(row=0, column=1)  
        
        # Password label and password entry box
        passwordLabel = Label(self,text="Password").grid(row=1, column=0)  
        password = StringVar()
        passwordEntry = Entry(self, textvariable=password, show='*').grid(row=1, column=1)  
        
        validateLogin = partial(self.validateLogin, username, password)
        
        # Login button
        loginButton = Button(self, text="Login", command=validateLogin).grid(row=4, column=0)

    def validateLogin(self, username, password):
        print("username entered :", username.get())
        print("password entered :", password.get())
        self.destroy()