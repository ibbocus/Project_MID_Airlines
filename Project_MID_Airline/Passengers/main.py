from Project_MID_Airline.Passengers.passengers import Passengers

# # Create a user interface that allows you to select options where the options are: Insert passenger info/create a manifest for a flight
def passenger_functions():
    passenger = Passengers()
    passengers = True
    print("Please choose from the options given below:")
    print("I - Insert passenger info - I ")
    print("S - Select passengers - S")
    print("C - Create manifest - C")
    print("Q - To exit this function")
    user_input = input("Please choose the function you would like to run: ")
    if user_input == "I":
        print(user_input)
        passenger.insert_passenger_info()
    elif user_input == "S":
        print(user_input)
        passenger.select_passengers()
    elif user_input == "C":
        print(user_input)
        passenger.create_manifest()

passenger = Passengers()
# # passenger.insert_passenger_info()
# passenger.select_passengers()
# passenger.create_table()
# passenger.existing_customers()
# passenger.create_manifest()
# print(passenger.select_passengers())
# passenger.table_init()

passenger.id_checker()

