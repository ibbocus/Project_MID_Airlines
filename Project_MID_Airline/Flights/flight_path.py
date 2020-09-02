import pandas as pd
from Project_MID_Airline.Planes.Plane_A381 import A380
from Project_MID_Airline.Planes.Plane_747 import B747
from Project_MID_Airline.Planes.Plane_787 import B787
from Project_MID_Airline.Databases.database_connection import *
from Project_MID_Airline.Databases.flights_db import *

# This file will create class called FlightInfo, which will contain the attributes needed to describe a flight
# It will also contain methods that will allow staff to determine other outputs such as fuel consumption, flight capacity (based on plane model) etc


class FlightInfo:
    def __init__(self, flight_name=None, destination=None, timeslot=None, plane_model=None, origin=None, distance=None,
                 flight_duration=None, flights_info=[]):  # plane_model will be exported to plane
        self.flight_name = flight_name
        self.origin = origin
        self.destination = destination
        self.timeslot = timeslot
        self.plane_model = plane_model
        self.distance = distance
        self.flight_duration = flight_duration
        self.flights_info = flights_info

    # If method is specific to 1 flight then it will be kept here
    # We need to print out a list of available destinations

    def create_flight(self):
        distances = {"Brussels": 300, "Paris": 340, "Amsterdam": 360, "Dublin": 470, "Berlin": 940, "Copenhagen": 994,
                     "Madrid": 1260, "Rome": 1380, "Stockholm": 1530, "Lisbon": 1550}
        self.flight_name = input("What would you like to name this route?: ")
        self.destination = input("Where is the destination?: ")
        self.origin = "London"
        self.timeslot = input("What time is the slot?: ")
        self.plane_model = input("Which model plane is being used?: ")
        self.store_info()

    def store_info(self):
        db = Database_OOP()
        db.connect_sql()
        cursor = db.connect_sql()
        query = f'''
        INSERT INTO flights(flight_name, plane_model, destination, timeslot)
        VALUES
        ('{self.flight_name}', '{self.plane_model}', '{self.destination}', '{self.timeslot}')
        '''
        cursor.execute(query)
        cursor.commit()
        return

    def assign_plane(self):
        password = True
        while password:
            try:
                password = input("Please enter your password:")
                if password != "midairlines":
                    raise ValueError  # this will send it to the print message and back to the input option
                password = False
            except ValueError:
                print("Invalid password. Please try again!")
        self.plane_model = input("Enter Plane model to change type of plane used: ")
        db = Database_OOP()
        db.connect_sql()
        cursor = db.connect_sql()
        query = f"""
            UPDATE flights
            SET plane_model = '{self.plane_model}'
            WHERE flight_number = '{self.flight_number}'
            """
        cursor.execute(query)
        cursor.commit()
        return

    def assign_plane_app(self, plane_model, flight_number):
        db = Database_OOP()
        db.connect_sql()
        cursor = db.connect_sql()
        query = f"""
            UPDATE flights
            SET plane_model = '{plane_model}'
            WHERE flight_number = '{flight_number}'
            """
        cursor.execute(query)
        cursor.commit()

    def select_flights(self):
        db = Database_OOP()
        db.connect_sql()
        cursor = db.connect_sql()
        query = "SELECT * FROM flights"
        rows = cursor.execute(query)  # execute query using connection/ cursor
        passengerid = []
        flight_name = []  # Initialise an empty list for each column
        plane_model = []
        destination = []
        timeslot = []

        for passengerID, flightname, planemodel, dstn, time in rows:
            passengerid.append(passengerID)# a slightly different name goes here
            flight_name.append(flightname)  # list goes first, slightly different name goes in brackets
            plane_model.append(planemodel)
            destination.append(dstn)
            timeslot.append(time)

        df_flights = pd.DataFrame()
        df_flights['PassengerID'] = passengerid
        df_flights['Flight Name'] = flight_name  # name a column 'First Name' then make it equal to the list you initialised
        df_flights['Plane Model'] = plane_model
        df_flights['Destination'] = destination
        df_flights['Time Slot'] = timeslot

        # Naming the column 'Date' and filling it with the data from the list previously created
        return df_flights

    def time_taken(self):
        plane = ""
        if self.plane_model == "747":
            plane = B747()
        elif self.plane_model == "787":
            plane = B787()
        elif self.plane_model == "A380":
            plane = A380()
        self.flight_duration = self.distance / plane.avg_speed
        print(str(self.flight_duration) + " " + "hours")

    def gather_info(self, flights_info, gui_output):

        flights_info.append(gui_output)
        print(flights_info)

