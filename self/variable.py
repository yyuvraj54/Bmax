from tkinter import *
class IntVar_for_height_and_weight(Variable):
    __default = ""
    def __init__(self, master=None, value=None, name=None):
        Variable.__init__(self, master, value, name)
    def get(self):
        value = self._tk.globalgetvar(self._name)
        if isinstance(value, str):
            return value
        return str(value)
