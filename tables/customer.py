from tkinter import *
from tk_objects import DropDown, Table
import server


class CustomerApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Customers)')
        self.root.geometry('1080x720')
        self.root.configure(padx=20, pady=20)

        self.title = Label(
            self.root,
            text='Customer Management System',
            font=('Arial', 24, 'bold', 'underline'),
            pady=10
        )
        self.title.pack()

        self.customers_attr = ('customerID', 'fname', 'lname', 'email', 'phoneNo', 'sex', 'DOB', 'ppNo')
        customer_data = server.selectTable('customer')
        self.customers_table = Table(self.root, self.customers_attr, customer_data)
        self.customers_table.frame.pack(side='top', pady=10)
        self.current_customers = len(customer_data)

        self.separator = Frame(self.root, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, pady=10)

        self.control_panel = Frame(self.root, pady=10)
        self.control_panel.pack()

        self.update_panel = LabelFrame(
            self.control_panel,
            text='Update Customer Details',
            font=('Arial', 14, 'bold'),
            padx=10,
            pady=10
        )
        self.update_panel.pack(pady=10, fill='x')

        self.options = [val[0] for val in customer_data if customer_data]  
        dropdown_enabled = bool(self.options)
        if not dropdown_enabled:
            self.options = ["No customer available"]

        Label(self.update_panel, text='Select Customer:', font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.dd = DropDown(self.update_panel, self.options)
        self.dd.grid(row=0, column=1, padx=5, pady=5)

        Label(self.update_panel, text='New Email:', font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.email_input = Entry(self.update_panel, width=30, font=('Arial', 12))
        self.email_input.grid(row=1, column=1, padx=5, pady=5)

        Label(self.update_panel, text='New Phone No.:', font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.phone_input = Entry(self.update_panel, width=20, font=('Arial', 12))
        self.phone_input.grid(row=2, column=1, padx=5, pady=5)

        self.update_button = Button(
            self.update_panel,
            text='Update Customer Details',
            command=self.updateCustomer,
            state='normal' if dropdown_enabled else 'disabled',
            bg='#4CAF50', fg='white', font=('Arial', 12), padx=10
        )
        self.update_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.delete_button = Button(
            self.update_panel,
            text='Delete Customer',
            command=self.deleteCustomer,
            state='normal' if dropdown_enabled else 'disabled',
            bg='#F44336', fg='white', font=('Arial', 12), padx=10
        )
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.separator2 = Frame(self.root, height=2, bd=1, relief=SUNKEN)
        self.separator2.pack(fill=X, pady=10)

        self.add_customer_panel = LabelFrame(
            self.control_panel,
            text='Add New Customer',
            font=('Arial', 14, 'bold'),
            padx=10,
            pady=10
        )
        self.add_customer_panel.pack(pady=10, fill='x')

        Label(self.add_customer_panel, text='First Name:', font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.fname_input = Entry(self.add_customer_panel, width=20, font=('Arial', 12))
        self.fname_input.grid(row=0, column=1, padx=5, pady=5)

        Label(self.add_customer_panel, text='Last Name:', font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.lname_input = Entry(self.add_customer_panel, width=20, font=('Arial', 12))
        self.lname_input.grid(row=1, column=1, padx=5, pady=5)

        Label(self.add_customer_panel, text='Email:', font=('Arial', 12)).grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.email_input_add = Entry(self.add_customer_panel, width=30, font=('Arial', 12))
        self.email_input_add.grid(row=0, column=3, padx=5, pady=5)

        Label(self.add_customer_panel, text='Phone No.:', font=('Arial', 12)).grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self.phone_input_add = Entry(self.add_customer_panel, width=20, font=('Arial', 12))
        self.phone_input_add.grid(row=1, column=3, padx=5, pady=5)

        Label(self.add_customer_panel, text='Address:', font=('Arial', 12)).grid(row=2, column=2, padx=5, pady=5, sticky='w')
        self.address_input_add = Entry(self.add_customer_panel, width=30, font=('Arial', 12))
        self.address_input_add.grid(row=2, column=3, padx=5, pady=5)

        self.add_button = Button(
            self.add_customer_panel,
            text='Add Customer',
            command=self.addCustomer,
            bg='#2196F3', fg='white', font=('Arial', 12), padx=10
        )
        self.add_button.grid(row=3, column=0, columnspan=4, pady=10)

    def updateTable(self):
        self.customers_table.frame.destroy()  
        customer_data = server.selectTable('customer')  
        self.customers_table = Table(self.root, self.customers_attr, customer_data) 
        self.customers_table.frame.pack(side='top', pady=10)  
        self.current_customers = len(customer_data)

        self.options = [val[0] for val in customer_data if customer_data]  
        dropdown_enabled = bool(self.options)
        if not dropdown_enabled:
            self.options = ["No customer available"]

        self.dd.destroy()
        self.dd = DropDown(self.update_panel, self.options)
        self.dd.grid(row=0, column=1, padx=5, pady=5)
        self.update_button.config(state='normal' if dropdown_enabled else 'disabled')
        self.delete_button.config(state='normal' if dropdown_enabled else 'disabled')

    def addCustomer(self):
        customerID = f'CUST0000{self.current_customers + 1}'
        fname, lname = self.fname_input.get(), self.lname_input.get()
        email, phoneNo = self.email_input_add.get(), self.phone_input_add.get()
        address = self.address_input_add.get()

        if fname and lname and email and phoneNo and address:  
            server.addCustomer(customerID, fname, lname, email, phoneNo, 'M', '2000-01-01', '123456789')
            self.updateTable()  
        else:
            print("All fields are required.")

    def updateCustomer(self):
        customerID = self.dd.getSelected()
        email = self.email_input.get()
        phoneNo = self.phone_input.get()
        if customerID != "No customer available" and email and phoneNo:
            server.updateCustomer(customerID, email=email, phoneNo=phoneNo)
            self.updateTable()


    def deleteCustomer(self):
        customerID = self.dd.getSelected()
        if customerID != "No customer available":
            server.deleteCustomer(customerID)
            self.updateTable()
            
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = CustomerApp()
    app.run()
