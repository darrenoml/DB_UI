import mysql.connector
import os

mydb = mysql.connector.connect(
    host        = "localhost",
    user        = "root",
    password    = "Berkat123",
    database    = "Binusantara"
 )
cursor = mydb.cursor()

def getTableNames():
    return  ['customer', 'staff', 'tour', 'destination', 'tourdest', 'booking', 'flight', 'flightbooking']

def selectTable(name:str):
    table_name = name.lower().capitalize()
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

def setStaffSalary(id, salary):
    if int(salary) > 100000000:
        cursor.execute("UPDATE Staff SET staff_salary = %s WHERE staffID = %s", (salary, id))
        mydb.commit()
        print(f"set {id} salary to {str(salary)}")
    print(selectTable('staff'))

def hireStaff(id, fname, lname, email, phoneNo, sex, salary):
    val = (id, fname, lname, email, phoneNo, sex, salary)
    cursor.execute("INSERT INTO Staff VALUES (%s, %s, %s, %s, %s, %s, %s)", val)
    mydb.commit()
    print(f'Hired {fname} {lname} as new Staff!')
    print(selectTable('staff'))
    
def fireStaff(id):
    cursor.execute("DELETE FROM Staff WHERE staffID = %s", [id])
    mydb.commit()
    print(f'Fired a staff')
    print(selectTable('staff'))
####################################################
def addCustomer(id, fname, lname, email, phoneNo, sex, dob, ppNo):
    val = (id, fname, lname, email, phoneNo, sex, dob, ppNo)
    cursor.execute("INSERT INTO Customer (customerID, customer_fname, customer_lname, customer_email, customer_phoneNo, customer_sex, customer_DOB, customer_ppNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", val)
    mydb.commit()
    print(f"Added customer {fname} {lname}!")

def updateCustomer(id, email=None, phoneNo=None):
    if email:
        cursor.execute("UPDATE Customer SET customer_email = %s WHERE customerID = %s", (email, id))
    if phoneNo:
        cursor.execute("UPDATE Customer SET customer_phoneNo = %s WHERE customerID = %s", (phoneNo, id))
    mydb.commit()
    print(f'Updated Customer {id}.')
    print(selectTable('customer'))

def deleteCustomer(id):
    cursor.execute("DELETE FROM Customer WHERE customerID = %s", [id])
    mydb.commit()
    print(f'Deleted Customer {id}.')
    print(selectTable('customer'))
##############################################################


def selectTable(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    return result

def addBooking(id, customerID, tourID, bookingDate, status, staffID=None):
    val = (id, customerID, tourID, bookingDate, status, staffID)
    query = """
        INSERT INTO Booking (bookingID, customerID, tourID, booking_date, status, staffID)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, val)
    mydb.commit()
    print(f'Added Booking {id}.')
    print(selectTable('booking'))



def deleteBooking(id):
    cursor.execute("DELETE FROM Booking WHERE bookingID = %s", [id])
    mydb.commit()
    print(f'Deleted Booking {id}.')
    print(selectTable('Booking'))  


def getBookings():
    cursor.execute("SELECT * FROM Booking")
    return cursor.fetchall()


def getBookingById(bookingID):
    cursor.execute("SELECT * FROM Booking WHERE bookingID = %s", [bookingID])
    return cursor.fetchone()

####################################################################
def getFlightById(flightID):
    cursor.execute("SELECT * FROM Flight WHERE flightID = %s", [flightID])
    return cursor.fetchone()

def addFlight(flightID, airlineName, depAirport, depTime, arrAirport, arrTime):
    val = (flightID, airlineName, depAirport, depTime, arrAirport, arrTime)
    cursor.execute("INSERT INTO Flight (flightID, airline_name, dep_airport, dep_time, arr_airport, arr_time) VALUES (%s, %s, %s, %s, %s, %s)", val)
    mydb.commit()
    print(f'Added Flight {flightID}.')
    return selectTable('flight')

def updateFlight(flightID, airlineName=None, depAirport=None, depTime=None, arrAirport=None, arrTime=None):
    updates = []
    values = []

    if airlineName:
        updates.append("airline_name = %s")
        values.append(airlineName)
    if depAirport:
        updates.append("dep_airport = %s")
        values.append(depAirport)
    if depTime:
        updates.append("dep_time = %s")
        values.append(depTime)
    if arrAirport:
        updates.append("arr_airport = %s")
        values.append(arrAirport)
    if arrTime:
        updates.append("arr_time = %s")
        values.append(arrTime)

    if updates:
        values.append(flightID)
        sql = f"UPDATE Flight SET {', '.join(updates)} WHERE flightID = %s"
        cursor.execute(sql, values)
        mydb.commit()
        print(f'Updated Flight {flightID}.')
        return selectTable('flight')
    else:
        print("No fields to update.")
        return None

def deleteFlight(flightID):
    cursor.execute("DELETE FROM Flight WHERE flightID = %s", [flightID])
    mydb.commit()
    print(f'Deleted Flight {flightID}.')
    return selectTable('flight')

def selectTable(tableName):
    cursor.execute(f"SELECT * FROM {tableName}")
    return cursor.fetchall()
