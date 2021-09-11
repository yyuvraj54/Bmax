
import tkinter as tk
from tkinter import *
from tkinter.constants import *

class Entry1(tk.Entry,Widget, XView):
    """Entry widget which allows displaying simple text."""
    def __init__(self, master=None, placeholder="", color='grey',cnf={}, **kw):
        super().__init__(master)
        Widget.__init__(self, master, 'entry', cnf, kw)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

if __name__ == "__main__": 
    root = tk.Tk() 
    name=Entry(root,relief=FLAT).pack()
    username = Entry1(root, "username","red",relief=FLAT)
    password = Entry1(root, "password", 'blue')
    username.pack()
    password.pack()  
    root.mainloop()
