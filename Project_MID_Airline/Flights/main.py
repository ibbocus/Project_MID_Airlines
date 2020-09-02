from Project_MID_Airline.Flights.flight_path import FlightInfo
# user input: are you ready to create a flight? if no set while to false, if yes first create flight, then store info
# after this is done, you give another user input with the following options: reassign plane - assign_plane, or display all flights - select_flights

display = FlightInfo()

# #
# display.create_flight() # This creates a flight
# display.store_info()
# display.assign_plane()
display.select_flights()