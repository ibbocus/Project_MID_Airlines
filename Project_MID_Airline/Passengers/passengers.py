from Project_MID_Airline.Databases.database_connection import Database_OOP
import pyodbc
import pandas as pd
# from Project_MID_Airline.Flights.flight_path import brussels1
# Here we will initiate the Passengers class:
from Project_MID_Airline.Flights.flight_manifest import FlightManifest


class Passengers:

    def create_table(self):
        db = Database_OOP()  # fix naming convetions
        db.connect_sql()
        cursor = db.connect_sql()
        table_name = "passengers"
        sql_command = f"""
    CREATE TABLE {table_name}
    (
    passengerID int IDENTITY (1,1) NOT NULL,
    first_name VARCHAR(300),
    last_name VARCHAR(300),
    passport_number VARCHAR(300),
    dob VARCHAR(300),
    upcoming_flight VARCHAR(300),
    flight_number VARCHAR(300),
    airmiles VARCHAR(300),
    previous_flights VARCHAR(300),
    )
    """
        cursor.execute(sql_command)
        cursor.commit()

    def existing_customers(self):
        a = Database_OOP()
        cursor = a.connect_sql()
        query = '''
            INSERT
            INTO
            passengers(first_name, last_name, passport_number, dob, upcoming_flight, flight_number, airmiles,
                       previous_flights)
            VALUES
        ('Ibrahim', 'Bocus', '170994GLPR', '02/09/1996', 'True', '1321', '2500', 'london'),
        ('Daniel', 'Teegan', '150193FRHT', '17/08/1999', 'True', '4321', '0', 'london'),
        ('Mehdi', 'Shamaa', '020390AQWS', '22/02/2000', 'True', '1321', '3487', 'Dublin'),
        ('Tony', 'Hawk', '210799LQRV', '20/12/1991', 'True', '4321', '2087', 'Lisbon'),
        ('Jack', 'Bauer', '221290QPWR', '29/09/1987', 'True', '1321', '9023', 'N/A'),
        ('Jon', 'Jones', '150984LLPR', '02/09/1996', 'True', '4321', '2500', 'london'),
        ('Max', 'Holloway', '220198LPTT', '17/08/1999', 'True', '1321', '0', 'london'),
        ('Sammy', 'Loqbeti', '340991MPWS', '22/02/2003', 'False', 'N/A', '3487', 'Dublin'),
        ('Jorge', 'Masvidal', '020991LPWS', '22/02/2003', 'True', '1321', '3487', 'Dublin'),
        ('Tony', 'Ferguson', '110779MZAH', '20/12/1991', 'True', '4321', '2087', 'Lisbon'),
        ('Jamie', 'Footy', '340661MPWS', '22/02/2000', 'False', 'N/A', '3187', 'Dublin'),
        ('Dustin', 'Poirer', '991290MJUT', '29/09/1987', 'True', '2221', '9023', 'N/A'),
        ('Rush', 'Holloway', '990779MZAH', '20/12/1991', 'True', '4321', '2087', 'Lisbon'),
        ('Dustin', 'Smith', '011290MLUT', '29/09/1987', 'True', '2221', '9023', 'N/A'),
        ('Kamaru', 'Usman', '300561NQWS', '22/02/1988', 'False', 'N/A', '3187', 'Dublin')

            '''
        cursor.execute(query)
        cursor.commit()

    def table_init(self):
        self.create_table()
        self.existing_customers()

    def insert_passenger_info(self):
        db = Database_OOP()
        cursor = db.connect_sql()
        p = Passengers()
        enter_info = True
        while enter_info:
            while True:
                try:
                    # First name user input
                    first_name = input("Please enter the customers First Name: ")
                    if len(first_name) <= 2 or len(first_name) > 20:
                        raise ValueError
                    break
                except ValueError:
                    print("ERROR: Please enter a valid first name")
            while True:
                try:
                    # Second name user input
                    last_name = input("Please enter the customers Last Name: ")
                    if len(last_name) <= 2 or len(last_name) > 20:
                        raise ValueError
                    break
                except ValueError:
                    print("ERROR: Please enter a valid last name")
            while True:
                try:
                    # Passport number user input
                    passport_number = input("Please enter the customers 10-character Passport Number: ")
                    if len(passport_number) < 10 or len(passport_number) > 10:
                        raise ValueError
                    break
                except ValueError:
                    print("ERROR: Please enter a valid passport number (10 characters) ")
            while True:
                try:
                    # Date of birth user input
                    dob = input("Please enter the customers Date of Birth in the following format (DD/MM/YYYY): ")
                    if len(str(dob)) < 10 or len(str(dob)) > 10:
                        raise ValueError
                    break
                except ValueError:
                    print("ERROR: Please enter a valid date of birth. In the following format (DD/MM/YYYY)")
            while True:
                try:
                    # Upcoming flight user input
                    upcoming_flight = input("Does the customer have an upcoming flight? (TRUE or FALSE): ")
                    if (upcoming_flight != "TRUE" and "FALSE") and (
                            len(upcoming_flight) < 2 or len(upcoming_flight)) > 6:
                        raise ValueError
                    break
                except ValueError:
                    print("ERROR: Please enter a valid choice TRUE or FALSE: ")
            while True:
                try:
                    # Upcoming flight number user input
                    flight_number = input("Please enter the customers Flight number: ")
                    if len(flight_number) < 2 or len(flight_number) > 30:
                        raise ValueError
                    break
                except ValueError:
                    print("ERROR: Please enter a valid destination")
            while True:
                try:
                    # Airmiles user input
                    airmiles = (input(
                        "How many Air Miles has the customer accumulated: "))
                    if len(airmiles) > 10:
                        raise ValueError
                    break
                except ValueError:
                    print("ERROR: please check and try again")
            while True:
                try:
                    # Last flight user input
                    previous_flights = input(
                        "Please enter the customers previous flight with MID Airlines. If its their first flight enter N/A: ")
                    if len(previous_flights) < 3 or len(previous_flights) > 30:
                        raise ValueError
                    break
                except ValueError:
                    print("ERROR: Please enter a valid destination")
            query1 = f"""
            INSERT INTO passengers
            (
                first_name, last_name, passport_number, dob,  upcoming_flight, flight_number, airmiles, previous_flights
            )
            VALUES
            (
                '{first_name}', '{last_name}', '{passport_number}', '{dob}', '{upcoming_flight}', '{flight_number}','{airmiles}', '{previous_flights}'
            )
            """
            cursor.execute(query1)
            cursor.commit()
            break_loop = input("Would you like to continue?: Y/N")
            if break_loop == "N":
                enter_info = False
            else:
                p.insert_passenger_info()

    def insert_passenger_info_app(self, first_name, last_name, passport_number, dob, upcoming_flight, flight_number,
                                  airmiles, previous_flights):
        db = Database_OOP()
        cursor = db.connect_sql()

        query1 = f"""
            INSERT INTO passengers
            (
                first_name, last_name, passport_number, dob,  upcoming_flight, flight_number, airmiles, previous_flights
            )
            VALUES
            (
                '{first_name}', '{last_name}', '{passport_number}', '{dob}', '{upcoming_flight}', '{flight_number}','{airmiles}', '{previous_flights}'
            )
            """
        cursor.execute(query1)
        cursor.commit()

    def select_passengers(self):
        db = Database_OOP()
        db.connect_sql()
        db.connect_sql()
        cursor2 = db.connect_sql()
        query = "SELECT * FROM passengers"
        rows = cursor2.execute(query)  # execute query using connection/ cursor
        passportid = []
        first_name = []  # Initialise an empty list for each column
        last_name = []
        passport_number = []
        date_of_birth = []
        upcoming_flight = []
        flight_number = []
        airmiles = []
        last_flight = []
        for pportid, firstname, lastname, passportno, dob, upcoming, flightnumber, air_miles, lastflight in rows:
            passportid.append(pportid)  # a slightly different name goes here
            first_name.append(firstname)  # list goes first, slightly different name goes in brackets
            last_name.append(lastname)
            passport_number.append(passportno)
            date_of_birth.append(dob)
            upcoming_flight.append(upcoming)
            flight_number.append(flightnumber)
            airmiles.append(air_miles)
            last_flight.append(lastflight)
        df_passengers = pd.DataFrame()
        df_passengers[
            'First Name'] = first_name  # name a column 'First Name' then make it equal to the list you initialised
        df_passengers['Last Name'] = last_name
        df_passengers['Passport Number'] = passport_number
        df_passengers['Date of Birth'] = date_of_birth
        df_passengers['Upcoming Flight'] = upcoming_flight
        df_passengers['Flight Number'] = flight_number
        df_passengers['Air Miles'] = airmiles
        df_passengers['Previous Flight Destination'] = last_flight

        # Naming the column 'Date' and filling it with the data from the list previously created
        return df_passengers

    def create_manifest(self):
        db = Database_OOP()
        db.connect_sql()
        cursor = db.connect_sql()
        manifest_input = input("Which flight number would you like to create a manifest for? ")
        if manifest_input == "1321":
            flightnumber = "1321"
        elif manifest_input == "4321":
            flightnumber = "4321"
        elif manifest_input == "2221":
            flightnumber = "2221"
        query = f"""SELECT p.passengerID, p.first_name, p.last_name, p.passport_number, p.dob, p.upcoming_flight, p.flight_number, f.destination, f.timeslot, f.plane_model, p.airmiles, p.previous_flights
FROM passengers p
INNER JOIN flights f ON p.flight_number = f.flight_number
WHERE p.flight_number = '{flightnumber}'"""
        rows = cursor.execute(query)
        passengerid = []
        first_name = []  # Initialise an empty list for each column
        last_name = []
        passport_number = []
        date_of_birth = []
        upcoming_flight = []
        flight_number = []
        destination = []
        time_slot = []
        plane_model = []
        airmiles = []
        previous_flight = []
        for passengerID, firstname, lastname, passportno, dob, upcoming, flightnumber, dest, timeslot, planemodel, air_miles, previousflight in rows:
            passengerid.append(passengerID)
            first_name.append(firstname)
            last_name.append(lastname)
            passport_number.append(passportno)
            date_of_birth.append(dob)
            upcoming_flight.append(upcoming)
            flight_number.append(flightnumber)
            destination.append(dest)
            time_slot.append(timeslot)
            plane_model.append(planemodel)
            airmiles.append(air_miles)
            previous_flight.append(previousflight)
        df_passengers = pd.DataFrame()
        df_passengers['First Name'] = first_name
        df_passengers['Last Name'] = last_name
        df_passengers['Passport Number'] = passport_number
        df_passengers['Date of Birth'] = date_of_birth
        df_passengers['Upcoming Flight'] = upcoming_flight
        df_passengers['Flight Number'] = flight_number
        df_passengers['Destination'] = destination
        df_passengers['Time slot'] = time_slot
        df_passengers['Plane model'] = plane_model
        df_passengers['Air Miles'] = airmiles
        df_passengers['Previous Flight'] = previous_flight
        return df_passengers

    def create_manifest_app(self, flightnumber):
        db = Database_OOP()
        db.connect_sql()
        cursor = db.connect_sql()
        query = f"""SELECT p.passengerID, p.first_name, p.last_name, p.passport_number, p.dob, p.upcoming_flight, 
p.flight_number, f.destination, f.timeslot, f.plane_model, p.airmiles, p.previous_flights 
FROM passengers p
INNER JOIN flights f ON p.flight_number = f.flight_number
WHERE p.flight_number = '{flightnumber}'"""
        rows = cursor.execute(query)
        passengerid = []
        first_name = []  # Initialise an empty list for each column
        last_name = []
        passport_number = []
        date_of_birth = []
        upcoming_flight = []
        flight_number = []
        destination = []
        time_slot = []
        plane_model = []
        airmiles = []
        previous_flight = []
        for passengerID, firstname, lastname, passportno, dob, upcoming, flightnumber, dest, timeslot, planemodel, air_miles, previousflight in rows:
            passengerid.append(passengerID)
            first_name.append(firstname)
            last_name.append(lastname)
            passport_number.append(passportno)
            date_of_birth.append(dob)
            upcoming_flight.append(upcoming)
            flight_number.append(flightnumber)
            destination.append(dest)
            time_slot.append(timeslot)
            plane_model.append(planemodel)
            airmiles.append(air_miles)
            previous_flight.append(previousflight)
        df_passengers = pd.DataFrame()
        df_passengers['First Name'] = first_name
        df_passengers['Last Name'] = last_name
        df_passengers['Passport Number'] = passport_number
        df_passengers['Date of Birth'] = date_of_birth
        df_passengers['Upcoming Flight'] = upcoming_flight
        df_passengers['Flight Number'] = flight_number
        df_passengers['Destination'] = destination
        df_passengers['Time slot'] = time_slot
        df_passengers['Plane model'] = plane_model
        df_passengers['Air Miles'] = airmiles
        df_passengers['Previous Flight'] = previous_flight
        return df_passengers

    def id_checker(self):
        db = Database_OOP()
        db.connect_sql()
        cursor = db.connect_sql()
        # flight_number = input("What flight number are you checking?") # THIS NEEDS TO BE UPDATED IN THE CREATE TABLE AND EXISTING CUSTOMERS INFO AND INSERT PASSENGER INFO
        # query = f"SELECT * FROM passengers WHERE  "
        flightnumber = input("What flight number are you checking")
        query = f"""SELECT p.passengerID, p.first_name, p.last_name, p.passport_number, p.dob, p.upcoming_flight, p.flight_number, f.destination, f.timeslot, f.plane_model, p.airmiles, p.previous_flights
FROM passengers p
INNER JOIN flights f ON p.flight_number = f.flight_number
WHERE p.flight_number = '{flightnumber}'"""
        first_name = str(input("What is the first name of the passenger? "))
        rows = cursor.execute(query)
        fname = []
        for pportid, firstname, lastname, passportno, dob, upcoming, flightnumber, air_miles, lastflight, fill1, fill2, fill3 in rows:
            fname.append(firstname)
        if first_name in fname:
            print("Success! ID matches with customer")
        else:
            manifest = FlightManifest()
            manifest.call_police()

# p = Passengers()
# # p.id_checker()
# # # WHERE flight_destination = '{destination}'
# # q = Passengers()
# # q.id_checker()
# # a = Passengers()
# # # a.create_table()
# # # a.insert_passenger_info()
# p.create_manifest_app(1321)
