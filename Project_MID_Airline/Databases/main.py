# This file is to be used to initialise both Passengers and Flights DB's
from Project_MID_Airline.Passengers.passengers import Passengers
from Project_MID_Airline.Databases.flights_db import Flights

#Initialising the classes
passengersdb = Passengers()
flightsdb = Flights()


# Setting up the Flights and Passengers Table
# passengersdb.table_init()
flightsdb.table_init()
# flightsdb.existing_flights()