from tkinter import *
from tk_objects import DropDown, Table
import server


class StaffApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Binusantara (Staffs)')
        self.root.geometry('1080x720')
        self.root.configure(padx=20, pady=20)

        # Title Label
        self.title = Label(
            self.root,
            text='Staff Management System',
            font=('Arial', 24, 'bold', 'underline'),
            pady=10
        )
        self.title.pack()

        self.staffs_attr = ('staffID', 'fname', 'lname', 'email', 'phoneNo', 'sex', 'salary')
        staff_data = server.selectTable('staff')
        self.staffs_table = Table(self.root, self.staffs_attr, staff_data)
        self.staffs_table.frame.pack(side='top', pady=10)
        self.current_staffs = len(staff_data)

        self.separator = Frame(self.root, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, pady=10)

        self.control_panel = Frame(self.root, pady=10)
        self.control_panel.pack()

        self.update_panel = LabelFrame(
            self.control_panel,
            text='Update Staff Details',
            font=('Arial', 14, 'bold'),
            padx=10,
            pady=10
        )
        self.update_panel.pack(pady=10, fill='x')

        self.options = [val[0] for val in staff_data if staff_data] 
        dropdown_enabled = bool(self.options)
        if not dropdown_enabled:
            self.options = ["No staff available"]

        Label(self.update_panel, text='Select Staff:', font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.dd = DropDown(self.update_panel, self.options)
        self.dd.grid(row=0, column=1, padx=5, pady=5)

    
        Label(self.update_panel, text='New Salary:', font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.salary_input = Entry(self.update_panel, width=15, font=('Arial', 12))
        self.salary_input.grid(row=1, column=1, padx=5, pady=5)

        self.salary_button = Button(
            self.update_panel,
            text='Update Salary',
            command=self.updateSalary,
            state='normal' if dropdown_enabled else 'disabled',
            bg='#4CAF50', fg='white', font=('Arial', 12), padx=10
        )
        self.salary_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.fire_button = Button(
            self.update_panel,
            text='Fire Staff',
            command=self.fireStaff,
            state='normal' if dropdown_enabled else 'disabled',
            bg='#F44336', fg='white', font=('Arial', 12), padx=10
        )
        self.fire_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.separator2 = Frame(self.root, height=2, bd=1, relief=SUNKEN)
        self.separator2.pack(fill=X, pady=10)

       
        self.hire_staff_panel = LabelFrame(
            self.control_panel,
            text='Hire New Staff',
            font=('Arial', 14, 'bold'),
            padx=10,
            pady=10
        )
        self.hire_staff_panel.pack(pady=10, fill='x')

        Label(self.hire_staff_panel, text='First Name:', font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.fname_panel = Entry(self.hire_staff_panel, width=20, font=('Arial', 12))
        self.fname_panel.grid(row=0, column=1, padx=5, pady=5)

        Label(self.hire_staff_panel, text='Last Name:', font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.lname_panel = Entry(self.hire_staff_panel, width=20, font=('Arial', 12))
        self.lname_panel.grid(row=1, column=1, padx=5, pady=5)

        Label(self.hire_staff_panel, text='Email:', font=('Arial', 12)).grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.email_panel = Entry(self.hire_staff_panel, width=30, font=('Arial', 12))
        self.email_panel.grid(row=0, column=3, padx=5, pady=5)

        Label(self.hire_staff_panel, text='Phone No.:', font=('Arial', 12)).grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self.phoneNo_panel = Entry(self.hire_staff_panel, width=20, font=('Arial', 12))
        self.phoneNo_panel.grid(row=1, column=3, padx=5, pady=5)

        self.hire_button = Button(
            self.hire_staff_panel,
            text='Hire Staff',
            command=self.hireStaff,
            bg='#2196F3', fg='white', font=('Arial', 12), padx=10
        )
        self.hire_button.grid(row=2, column=0, columnspan=4, pady=10)


    def updateTable(self):
        self.staffs_table.frame.destroy()
        staff_data = server.selectTable('staff')
        self.staffs_table = Table(self.root, self.staffs_attr, staff_data)
        self.staffs_table.frame.pack(side='top', pady=10)
        self.current_staffs = len(staff_data)

        self.options = [val[0] for val in staff_data if staff_data]
        dropdown_enabled = bool(self.options)
        if not dropdown_enabled:
            self.options = ["No staff available"]

  
        self.dd.destroy()
        self.dd = DropDown(self.update_panel, self.options)
        self.dd.grid(row=0, column=1, padx=5, pady=5)
        self.salary_button.config(state='normal' if dropdown_enabled else 'disabled')
        self.fire_button.config(state='normal' if dropdown_enabled else 'disabled')

    def hireStaff(self):
        staffID = f'STAFF0000{self.current_staffs + 1}'
        fname, lname = self.fname_panel.get(), self.lname_panel.get()
        email, phoneNo = self.email_panel.get(), self.phoneNo_panel.get()
        if fname and lname and email and phoneNo:  # Validate input
            server.hireStaff(staffID, fname, lname, email, phoneNo, 'M', 100000000)
            self.updateTable()
        else:
            print("All fields are required to hire a staff.")

    def fireStaff(self):
        staffID = self.dd.getSelected()
        if staffID != "No staff available":
            server.fireStaff(staffID)
            self.updateTable()


    def updateSalary(self):
        staffID = self.dd.getSelected()
        salary = self.salary_input.get()
        if staffID != "No staff available" and salary.isdigit():
            server.setStaffSalary(staffID, salary)
            self.updateTable()
        else:
            print("Please enter a valid salary.")

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = StaffApp()
    app.run()
