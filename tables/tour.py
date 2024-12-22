from tkinter import *
from tk_objects import DropDown, Table
import server


class TourApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Tours)')
        self.root.geometry('1080x720')
        
        self.tour_attr = ('tourID', 'name', 'start_date', 'end_date', 'tour_price', 'tour_desc')
        self.tour_table = Table(self.root, self.tour_attr, server.selectTable('tour'))
        self.tour_table.frame.pack(side='top')
        self.current_tour=  len(server.selectTable('tour'))

    def run(self):
        self.root.mainloop()