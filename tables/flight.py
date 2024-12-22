from tkinter import *
from tk_objects import DropDown, Table
import server


class FlightApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Flights)')
        self.root.geometry('1080x720')
        self.root.configure(padx=20, pady=20)

        self.title = Label(self.root, text='Flight Management System', font=('Arial', 24, 'bold', 'underline'))
        self.title.pack(pady=10)

        self.flight_attr = ('flightID', 'airline_name', 'dep_airport', 'dep_time', 'arr_airport', 'arr_time')
        self.flight_table = Table(self.root, self.flight_attr, server.selectTable('flight'))
        self.flight_table.frame.pack(side='top', pady=10)
        self.current_flight = len(server.selectTable('flight'))

        self.control_panel = Frame(self.root)
        self.control_panel.pack(pady=20)

        self.add_flight_panel = LabelFrame(
            self.control_panel, text='Add New Flight', font=('Arial', 14, 'bold'), padx=10, pady=10
        )
        self.add_flight_panel.grid(row=0, column=0, padx=10, pady=10, sticky='n')

        Label(self.add_flight_panel, text='Flight ID:', font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.flightID_input = Entry(self.add_flight_panel, width=20, font=('Arial', 12))
        self.flightID_input.grid(row=0, column=1, padx=5, pady=5)

        Label(self.add_flight_panel, text='Airline Name:', font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.airline_input = Entry(self.add_flight_panel, width=20, font=('Arial', 12))
        self.airline_input.grid(row=1, column=1, padx=5, pady=5)

        Label(self.add_flight_panel, text='Dep. Airport:', font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.dep_airport_input = Entry(self.add_flight_panel, width=20, font=('Arial', 12))
        self.dep_airport_input.grid(row=2, column=1, padx=5, pady=5)

        Label(self.add_flight_panel, text='Dep. Time:', font=('Arial', 12)).grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.dep_time_input = Entry(self.add_flight_panel, width=20, font=('Arial', 12))
        self.dep_time_input.grid(row=3, column=1, padx=5, pady=5)

        Label(self.add_flight_panel, text='Arr. Airport:', font=('Arial', 12)).grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.arr_airport_input = Entry(self.add_flight_panel, width=20, font=('Arial', 12))
        self.arr_airport_input.grid(row=4, column=1, padx=5, pady=5)

        Label(self.add_flight_panel, text='Arr. Time:', font=('Arial', 12)).grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.arr_time_input = Entry(self.add_flight_panel, width=20, font=('Arial', 12))
        self.arr_time_input.grid(row=5, column=1, padx=5, pady=5)

        self.add_button = Button(
            self.add_flight_panel, text='Add Flight', command=self.addFlight, bg='#4CAF50', fg='white', font=('Arial', 12)
        )
        self.add_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.delete_flight_panel = LabelFrame(
            self.control_panel, text='Delete Flight', font=('Arial', 14, 'bold'), padx=10, pady=10
        )
        self.delete_flight_panel.grid(row=0, column=1, padx=10, pady=10, sticky='n')

        self.flight_options = [row[0] for row in server.selectTable('flight')]
        self.dd = DropDown(self.delete_flight_panel, self.flight_options)
        self.dd.grid(row=0, column=0, padx=10, pady=10)

        self.delete_button = Button(
            self.delete_flight_panel, text='Delete Flight', command=self.deleteFlight, bg='#F44336', fg='white', font=('Arial', 12)
        )
        self.delete_button.grid(row=1, column=0, pady=10)

    def updateTable(self):
        self.flight_table.frame.destroy()
        self.flight_table = Table(self.root, self.flight_attr, server.selectTable('flight'))
        self.flight_table.frame.pack(side='top', pady=10)
        self.flight_options = [row[0] for row in server.selectTable('flight')]
        self.dd.destroy()
        self.dd = DropDown(self.delete_flight_panel, self.flight_options)
        self.dd.grid(row=0, column=0, padx=10, pady=10)

    def addFlight(self):
        flightID = self.flightID_input.get()
        airline_name = self.airline_input.get()
        dep_airport = self.dep_airport_input.get()
        dep_time = self.dep_time_input.get()
        arr_airport = self.arr_airport_input.get()
        arr_time = self.arr_time_input.get()

        if all([flightID, airline_name, dep_airport, dep_time, arr_airport, arr_time]):
            server.addFlight(flightID, airline_name, dep_airport, dep_time, arr_airport, arr_time)
            self.updateTable()
        else:
            print("All fields are required.")

    def deleteFlight(self):
        selected_flight = self.dd.getSelected()
        if selected_flight:
            server.deleteFlight(selected_flight)
            self.updateTable()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = FlightApp()
    app.run()

        