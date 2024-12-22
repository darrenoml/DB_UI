from tkinter import *
from tk_objects import DropDown, Table
import server
from tables.customer import CustomerApp
from tables.tour import TourApp
from tables.destination import DestinationApp
from tables.tourdest import TourDestApp
from tables.flight import FlightApp
from tables.booking import BookingApp
from tables.staff import StaffApp
from tables.flightbooking import FlightBookingApp

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara Admin Control Panel')
        self.root.geometry('800x400')
        self.frame = Frame(self.root)
        
        self.title = Label(self.frame, text='Binusantara - Admin Control Panel', font=('Arial', 20, 'bold', 'underline'))
        self.title.pack()
        
        self.buttons = Frame(self.frame)
        self._generateButtons()
        self.buttons.pack(pady=20, anchor=CENTER)  
        
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
    def _generateButtons(self):
        functions = [
            self.openCustomerApp, self.openStaffApp, self.openTourApp, self.openDestApp,
            self.openTourDestApp, self.openBookingApp, self.openFlightApp, self.openFlightBookingApp
        ]
        col = 0
        for i in range(len(server.getTableNames())):
            button = Button(self.buttons, width=10, height=2, text=server.getTableNames()[i].capitalize(), command = functions[i])
            button.grid(row=0, column=col)
            col += 1
            
    def openCustomerApp(self):
        customer_app = CustomerApp() 
        customer_app.run()
        
    def openStaffApp(self):
        staff_app = StaffApp() 
        staff_app.run()
        
    def openTourApp(self):
        tour_app = TourApp() 
        tour_app.run()
        
    def openDestApp(self):
        dest_app = DestinationApp()
        dest_app.run() 
    
    def openTourDestApp(self):
        tour_dest_app = TourDestApp()
        tour_dest_app.run()
        
    def openFlightApp(self):
        flight_app = FlightApp()
        flight_app.run()
        
    def openBookingApp(self):
        booking_app = BookingApp()
        booking_app.run()
        
    def openFlightBookingApp(self):
        flight_booking_app = FlightBookingApp()
        flight_booking_app.run()

    def run(self):
        self.root.mainloop()
        
if __name__ == "__main__": 
    App().run()
