def addTourDest(tourID, destID):
    cursor.execute(f"INSERT INTO TourDest VALUES {tourID, destID}")
    mydb.commit()
    print(f"Added Tour {tourID} the Destination {destID}")
    print(selectTable('TourDest'))

def addDestination(destID, name, country, address, desc):
    cursor.execute(f"INSERT INTO Destination VALUES {(destID, name, country, address, desc)}")
    mydb.commit()
    print(f"Added {destID} which is {name} located in {country} specifically on {address}. {desc}")
    print(selectTable('Destination'))
