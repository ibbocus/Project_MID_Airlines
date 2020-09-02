# This file will incorporate the information from flight info - Destination, origin and timeslot
# it will also take information from plane_info - potentaitally by creating an object of the required class here
# it will take information from the passengers database created in passengers.py

# outputs:
# generate a price for the ticket
# state the number of tickets available in each class
# updates the passengers database with a new value for their airmiles
# create an object of this class? maybe we do this in the flight_list_records file

class FlightTrip:
    def __init__(self): # As it imports data from other object, I am not sure if it needs to be passed arguments.
                        # maybe in the class files, we can make methods that will return each variable, we can use that to initialise this class
        pass
    def ticket_price(self):
        pass
    # apply discounts/up price the tickets based on quanitiy left, amount of airmiles, proximity to flight date

    def tickets_available(self):
        # this function will return the number of tickets available at each class, this will automatically update as more passengers are assigned to the flight
        pass

    def update_airmiles(self):
        pass
    # This function will update the airmiles of a passengers based on the distance of this flight

    def add_passengers_to_flight(self):
        # this function will add passengers to a list that will be used to create the manifest by reading the SQL database and adding based on a WHERE condition
        pass

    def assign_seat(self):
        # This function will asssign a unique seat number to each passenger
        pass
