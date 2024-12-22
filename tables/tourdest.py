from tkinter import *
from tk_objects import DropDown, Table
import server


class TourDestApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Destinations)')
        self.root.geometry('1080x720')
        
        self.tour_dest_attr = ('tourID','destID')
        self.tour_dest_table = Table(self.root, self.tour_dest_attr, server.selectTable('tourdest'))
        self.tour_dest_table.frame.pack(side='top')
        self.current_tour_dest =  len(server.selectTable('tourdest'))

    def run(self):
        self.root.mainloop()
        