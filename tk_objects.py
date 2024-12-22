from tkinter import *

class DropDown(OptionMenu):
    def __init__(self, root, choices: list):
        self.root = root
        self.clicked = StringVar()
        if choices:  # Check if choices is not empty
            self.clicked.set(choices[0])
        else:
            self.clicked.set("No options available")
            choices = ["No options available"]
        super().__init__(self.root, self.clicked, *choices)
    
    def getSelected(self):
        return self.clicked.get()
    
    def updateChoices(self, choices: list):
        if choices:
            self.clicked.set(choices[0])
        else:
            self.clicked.set("No options available")
            choices = ["No options available"]
        menu = self["menu"]
        menu.delete(0, "end")
        for choice in choices:
            menu.add_command(label=choice, command=lambda value=choice: self.clicked.set(value))

    
class Table:
    def __init__(self, root, attributes: tuple, values: list = None):
        self.root = root
        self.attributes = attributes
        self.values = values if values else []  # Use empty list if no values are provided
        self.combined = [self.attributes] + self.values  # Combine attributes and values

        self.frame = Frame(self.root)
        self.__loadTable()
        
    def __loadTable(self):
        for i, row_values in enumerate(self.combined):
            for j, value in enumerate(row_values):
                cell = Label(
                    self.frame,
                    text=value,
                    width=12,
                    height=1,
                    borderwidth=3,
                    relief="ridge",
                )
                cell.grid(row=i, column=j, sticky="news")
