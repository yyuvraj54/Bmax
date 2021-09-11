from tkinter import *

class StringVar1(Variable):
    _default = "root"
    def __init__(self, master=None, value=None, name=None):
        
        Variable.__init__(self, master, value, name)

    def get(self):
        value = self._tk.globalgetvar(self._name)
        if isinstance(value, str):
            return value
        return str(value)

class StringVar2(Variable):
    _default = "localhost"
    def __init__(self, master=None, value=None, name=None):
        Variable.__init__(self, master, value, name)

    def get(self):
        value = self._tk.globalgetvar(self._name)
        if isinstance(value, str):
            return value
        return str(value)


class IntVar_for_height_and_weight(Variable):
    __default = ""
    def __init__(self, master=None, value=None, name=None):
        Variable.__init__(self, master, value, name)
    def get(self):
        value = self._tk.globalgetvar(self._name)
        if isinstance(value, str):
            return value
        return str(value)

class StringVar_for_pass(Variable):
    _default = ""
    def __init__(self, master=None, value=None, name=None):
        Variable.__init__(self, master, value, name)
    def get(self):
        value = self._tk.globalgetvar(self._name)
        if isinstance(value, str):
            return value
        return str(value)

