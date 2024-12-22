from tkinter import *
from tk_objects import DropDown, Table
import server


class FlightBookingApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Flight Bookings)')
        self.root.geometry('1080x720')
        
        self.flight_booking_attr = ('bookingID', 'flightID', 'seats', 'class')
        self.flight_booking_table = Table(self.root, self.flight_booking_attr, server.selectTable('flightbooking'))
        self.flight_booking_table.frame.pack(side='top')
        self.current_flight_booking =  len(server.selectTable('flightbooking'))

    def run(self):
        self.root.mainloop()
        