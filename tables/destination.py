from tkinter import *
from tk_objects import DropDown, Table
import server


class DestinationApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Destinations)')
        self.root.geometry('1080x720')
        
        self.title = Label(self.root, text='Destinations Table', font=('Arial', 20, 'bold', 'underline'))
        self.title.pack()
        
        self.dest_attr = ('destID', 'name', 'country', 'address', 'dest_desc')
        self.dest_table = Table(self.root, self.dest_attr, server.selectTable('destination'))
        self.dest_table.frame.pack(side='top')
        self.current_dest=  len(server.selectTable('destination'))

    def run(self):
        self.root.mainloop()
        