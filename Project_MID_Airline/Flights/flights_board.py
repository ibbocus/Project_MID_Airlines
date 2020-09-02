from Project_MID_Airline.Flights.flight_path import FlightInfo
from Project_MID_Airline.Databases.database_connection import Database_OOP
import pandas as pd



class FlightsBoard(FlightInfo):
    pass
    # def select_flights(self):
    #     db = Database_OOP()
    #     db.connect_sql()
    #     cursor = db.connect_sql()
    #     query = "SELECT * FROM flights"
    #     rows = cursor.execute(query)  # execute query using connection/ cursor
    #     flight_name = []  # Initialise an empty list for each column
    #     plane_model = []
    #     destination = []
    #
    #     for flightname, planemodel, dstn in rows:  # a slightly different name goes here
    #         flight_name.append(flightname)  # list goes first, slightly different name goes in brackets
    #         plane_model.append(planemodel)
    #         destination.append(dstn)
    #
    #     df_flights = pd.DataFrame()
    #     df_flights['Flight Name'] = flight_name  # name a column 'First Name' then make it equal to the list you initialised
    #     df_flights['Plane Model'] = plane_model
    #     df_flights['Destination'] = destination
    #
    #     print(df_flights)
    #     # Naming the column 'Date' and filling it with the data from the list previously created
    #     return