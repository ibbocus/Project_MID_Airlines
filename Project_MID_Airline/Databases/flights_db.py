from Project_MID_Airline.Passengers.passengers import *


# from Project_MID_Airline.Flights.flight_path import brussels1
# Here we will initiate the Flights class:


class Flights:

    def create_table(self):
        db = Database_OOP() #fix naming convetions
        db.connect_sql()
        cursor = db.connect_sql()
        table_name = "flights"
        sql_command = f"""

CREATE TABLE {table_name}
(
FlightID int IDENTITY (1,1) NOT NULL,
flight_number VARCHAR(300),
plane_model VARCHAR(300),
destination VARCHAR(300),
timeslot VARCHAR(300)
)
"""
        cursor.execute(sql_command)
        cursor.commit()

    def existing_flights(self):
        db = Database_OOP()
        db.connect_sql()
        cursor = db.connect_sql()
        query = '''
            INSERT
            INTO
            flights(flight_number, plane_model, destination, timeslot)
            VALUES
            ('1321', 'A380', 'Madrid', '11:00' ),
            ('8762', '787', 'Rome', '17:00' ),
            ('4321', '747', 'Paris', '16:00'),
            ('0129', '747', 'Berlin', '19:00'),
            ('2221', 'A380', 'Amsterdam', '16:20'),
            ('3987', '787', 'Stockholm', '14:00'),
            ('9984', '747', 'Lisbon', '13:00')

            '''
        cursor.execute(query)
        cursor.commit()

    def table_init(self):
        self.create_table()
        self.existing_flights()
# a = Flights()
# # a.create_table()
# # a.insert_passenger_info()
# # a.table_init()
# a.select_flights()
