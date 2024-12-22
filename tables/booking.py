from tkinter import *
from tk_objects import DropDown, Table
import server


class BookingApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Bookings)')
        self.root.geometry('1080x720')
        self.root.configure(padx=20, pady=20)

        # Title
        self.title = Label(
            self.root,
            text='Booking Management System',
            font=('Arial', 24, 'bold', 'underline'),
            pady=10
        )
        self.title.pack()

        # Booking Table Section
        self.booking_attr = ('bookingID', 'customerID', 'booking_date', 'status', 'tourID', 'staffID')
        booking_data = server.selectTable('booking')
        self.booking_table = Table(self.root, self.booking_attr, booking_data)
        self.booking_table.frame.pack(side='top', pady=10)
        self.current_bookings = len(booking_data)

        # Control Panel
        self.control_panel = Frame(self.root, pady=10)
        self.control_panel.pack()

        # Add New Booking Panel
        self.add_booking_panel = LabelFrame(
            self.control_panel,
            text='Add New Booking',
            font=('Arial', 14, 'bold'),
            padx=10,
            pady=10
        )
        self.add_booking_panel.pack(pady=10, fill='x')

        Label(self.add_booking_panel, text='Customer ID:', font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.customer_id_input = Entry(self.add_booking_panel, width=20, font=('Arial', 12))
        self.customer_id_input.grid(row=0, column=1, padx=5, pady=5)

        Label(self.add_booking_panel, text='Tour ID:', font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.tour_id_input = Entry(self.add_booking_panel, width=20, font=('Arial', 12))
        self.tour_id_input.grid(row=1, column=1, padx=5, pady=5)

        Label(self.add_booking_panel, text='Booking Date:', font=('Arial', 12)).grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.booking_date_input = Entry(self.add_booking_panel, width=20, font=('Arial', 12))
        self.booking_date_input.grid(row=0, column=3, padx=5, pady=5)

        Label(self.add_booking_panel, text='Staff ID (Optional):', font=('Arial', 12)).grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self.staff_id_input = Entry(self.add_booking_panel, width=20, font=('Arial', 12))
        self.staff_id_input.grid(row=1, column=3, padx=5, pady=5)

        self.add_button = Button(
            self.add_booking_panel,
            text='Add Booking',
            command=self.addBooking,
            bg='#2196F3', fg='white', font=('Arial', 12), padx=10
        )
        self.add_button.grid(row=2, column=0, columnspan=4, pady=10)

        # Delete Booking Panel
        self.delete_booking_panel = LabelFrame(
            self.control_panel,
            text='Delete Booking',
            font=('Arial', 14, 'bold'),
            padx=10,
            pady=10
        )
        self.delete_booking_panel.pack(pady=10, fill='x')

        Label(self.delete_booking_panel, text='Booking ID:', font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.booking_id_input = Entry(self.delete_booking_panel, width=20, font=('Arial', 12))
        self.booking_id_input.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = Button(
            self.delete_booking_panel,
            text='Delete Booking',
            command=self.deleteBooking,
            bg='#F44336', fg='white', font=('Arial', 12), padx=10
        )
        self.delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Add Booking
    def addBooking(self):
        bookingID = f'BOOK0000{self.current_bookings + 1}'
        customerID = self.customer_id_input.get()
        tourID = self.tour_id_input.get()
        booking_date = self.booking_date_input.get()
        staffID = self.staff_id_input.get()

        if customerID and tourID and booking_date:
            server.addBooking(bookingID, customerID, tourID, booking_date, staffID or None)
            self.updateTable()
        else:
            print("All fields (except Staff ID) are required to add a booking.")

    # Delete Booking
    def deleteBooking(self):
        bookingID = self.booking_id_input.get()
        if bookingID:
            server.deleteBooking(bookingID)
            self.updateTable()
        else:
            print("Booking ID is required to delete a booking.")

    # Update Table
    def updateTable(self):
        self.booking_table.frame.destroy()  # Destroy the old table
        booking_data = server.selectTable('booking')  # Fetch updated booking data
        self.booking_table = Table(self.root, self.booking_attr, booking_data)  # Create a new table with updated data
        self.booking_table.frame.pack(side='top', pady=10)  # Repack the table
        self.current_bookings = len(booking_data)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = BookingApp()
    app.run()
