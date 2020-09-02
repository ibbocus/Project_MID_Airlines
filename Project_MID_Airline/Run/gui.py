from PyQt5 import QtWidgets, uic
from Project_MID_Airline.Planes.Plane_747 import B747
from Project_MID_Airline.Planes.Plane_787 import B787
from Project_MID_Airline.Planes.Plane_A381 import A380
from Project_MID_Airline.Flights.flight_path import FlightInfo
from Project_MID_Airline.Databases.flights_db import Flights
from Project_MID_Airline.Databases.database_connection import Database_OOP
from Project_MID_Airline.Passengers.passengers import Passengers
import sys
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, Qt


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class Ui(QtWidgets.QTabWidget):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('Project_MID.ui', self)  # Load the .ui file

        # PLANE INFO FUNCTIONS
        self.b747 = self.findChild(QtWidgets.QPushButton, 'Qplanes_print_747')
        self.b747.clicked.connect(self.b747_info)

        self.b787 = self.findChild(QtWidgets.QPushButton, 'Qplanes_prints_787')
        self.b787.clicked.connect(self.b787_info)

        self.a380 = self.findChild(QtWidgets.QPushButton, 'Qplanes_print_A380')
        self.a380.clicked.connect(self.a380_info)

        # Flight Functions
        # Create flight
        self.display = self.findChild(QtWidgets.QLabel, 'Qcreate_flight_prompts')
        self.display.setText("Please click Create Flight to begin")

        self.create_flight = self.findChild(QtWidgets.QPushButton, 'Qflights_createflights')
        self.create_flight.clicked.connect(self.create_flight_input_prompt)

        # Name flight
        self.flight_name = self.findChild(QtWidgets.QPushButton, 'Qflight_input')
        self.flight_name.clicked.connect(self.flight_name_input_prompt)

        # set destination
        self.destination = self.findChild(QtWidgets.QPushButton, 'Qdestination_input')
        self.destination.clicked.connect(self.destination_input_prompt)

        # set timeslot
        self.timeslot = self.findChild(QtWidgets.QPushButton, 'Qtime_input')
        self.timeslot.clicked.connect(self.timeslot_input_prompt)

        # set plane_model
        self.timeslot = self.findChild(QtWidgets.QPushButton, 'Qplane_input')
        self.timeslot.clicked.connect(self.plamemodel_input)

        # Assign new plane to flight
        self.assign_plane = self.findChild(QtWidgets.QPushButton, 'Qflights_assignplane')
        self.assign_plane.clicked.connect(self.assign_plane_method)
        # Qflights_assignplane = button

        # Initialise database
        self.p_init = self.findChild(QtWidgets.QPushButton, 'Qinit_p')
        self.p_init.clicked.connect(self.passengers_init)

        self.p_init = self.findChild(QtWidgets.QPushButton, 'Qinit_f')
        self.p_init.clicked.connect(self.flight_init)

        self.show_all_p = self.findChild(QtWidgets.QPushButton, 'Qpassengers_show_all_passengers')
        self.show_all_p.clicked.connect(self.show_all_passengers)

        self.createmanifest = self.findChild(QtWidgets.QPushButton, 'Qcreate_manifest')
        self.createmanifest.clicked.connect(self.create_manifest)

        self.insert_passenger = self.findChild(QtWidgets.QPushButton, 'Qinsert_passenger_info_2')
        self.insert_passenger.clicked.connect(self.insert_passenger_info)

        self.show_all_f = self.findChild(QtWidgets.QPushButton, 'Qflights_display')
        self.show_all_f.clicked.connect(self.show_all_flights)

        self.show()

    # Plane Methods
    def b747_info(self):
        plane = B747()
        self.display = self.findChild(QtWidgets.QLabel, 'Qplane_info_label')
        self.display.setText(plane.print_info())

    def b787_info(self):
        plane = B787()
        self.display = self.findChild(QtWidgets.QLabel, 'Qplane_info_label')
        self.display.setText(plane.print_info())

    def a380_info(self):
        plane = A380()
        self.display = self.findChild(QtWidgets.QLabel, 'Qplane_info_label')
        self.display.setText(plane.print_info())

    # Flight Methods

    def create_flight_input_prompt(self):
        self.display = self.findChild(QtWidgets.QLabel, 'Qcreate_flight_prompts')
        self.display.setText("Please enter a flight name")

    def flight_name_input_prompt(self):
        self.input = self.findChild(QtWidgets.QLineEdit, 'Qcreate_flights_inputs')
        flight_name = self.input.text()
        self.display = self.findChild(QtWidgets.QLabel, 'Qcreate_flight_prompts')
        self.display.setText("Please enter a destination")
        global flight_info
        flight_info = []
        flight_info.append(flight_name)
        print(flight_name)
        self.input.clear()

    def destination_input_prompt(self):
        self.input = self.findChild(QtWidgets.QLineEdit, 'Qcreate_flights_inputs')
        self.display.setText("What time is the flight?")
        destination = self.input.text()
        print(destination)
        flight_info.append(destination)
        self.input.clear()

    def timeslot_input_prompt(self):
        self.display = self.findChild(QtWidgets.QLabel, 'Qcreate_flight_prompts')
        self.display.setText("What model is the plane?")
        timeslot = self.input.text()
        print(timeslot)
        flight_info.append(timeslot)
        self.input.clear()

    def plamemodel_input(self):
        self.display = self.findChild(QtWidgets.QLabel, 'Qcreate_flight_prompts')
        self.display.setText("information has been stored in database")
        plane_model = self.input.text()
        print(plane_model)
        flight_info.append(plane_model)
        print(flight_info)
        db = Database_OOP()
        db.connect_sql()
        cursor = db.connect_sql()
        query = f'''
        INSERT INTO flights(flight_number, plane_model, destination, timeslot)
        VALUES
        ('{flight_info[0]}', '{flight_info[3]}', '{flight_info[1]}', '{flight_info[2]}')
        '''
        cursor.execute(query)
        cursor.commit()
        return

    def assign_plane_method(self):
        self.fn_input = self.findChild(QtWidgets.QLineEdit, 'Qcreate_flights_inputs')
        self.pm_input = self.findChild(QtWidgets.QLineEdit, 'Qflight_assign_input')
        flight_number = self.fn_input.text()
        plane_model = self.pm_input.text()
        f = FlightInfo()
        f.assign_plane_app(plane_model, flight_number)

        # Qassign_confirmed = text label

    # DATABASE Methods

    def passengers_init(self):
        # db = Database_OOP()  # fix naming convetions
        # db.connect_sql()
        # cursor = db.connect_sql()
        # table_name = "passengers"
        # sql_command = f"""
        # CREATE TABLE {table_name}
        # (
        # passengerID int IDENTITY (1,1) NOT NULL,
        # first_name VARCHAR(300),
        # last_name VARCHAR(300),
        # passport_number VARCHAR(300),
        # dob VARCHAR(300),
        # upcoming_flight VARCHAR(300),
        # flight_number VARCHAR(300),
        # airmiles VARCHAR(300),
        # previous_flights VARCHAR(300),
        # )
        # """
        # cursor.execute(sql_command)
        # cursor.commit()
        # db.connect_sql()
        # cursor = db.connect_sql()
        # query = '''
        #     INSERT
        #     INTO
        #     passengers(first_name, last_name, passport_number, dob, upcoming_flight, flight_number, airmiles,
        #                previous_flights)
        #     VALUES
        #     ('Ibrahim', 'Bocus', '170994GLPR', '02/09/1996', 'True', '1321', '2500', 'london'),
        #     ('Daniel', 'Teegan', '150193FRHT', '17/08/1999', 'True', '4321', '0', 'london'),
        #     ('Mehdi', 'Shamaa', '020390AQWS', '22/02/2000', 'True', '1321', '3487', 'Dublin'),
        #     ('Tony', 'Hawk', '210799LQRV', '20/12/1991', 'True', '4321', '2087', 'Lisbon'),
        #     ('Jack', 'Bauer', '221290QPWR', '29/09/1987', 'False', '1321', '9023', 'N/A'),
        #     ('Jon', 'Jones', '150984LLPR', '02/09/1996', 'True', '4321', '2500', 'london'),
        #     ('Max', 'Holloway', '220198LPTT', '17/08/1999', 'True', '1321', '0', 'london'),
        #     ('Jorge', 'Masvidal', '020991LPWS', '22/02/2003', 'True', '1321', '3487', 'Dublin'),
        #     ('Tony', 'Ferguson', '110779MZAH', '20/12/1991', 'True', '4321', '2087', 'Lisbon'),
        #     ('Dustin', 'Poirer', '991290MJUT', '29/09/1987', 'False', '2221', '9023', 'N/A'),
        #     ('Rush', 'Holloway', '990779MZAH', '20/12/1991', 'True', '4321', '2087', 'Lisbon'),
        #     ('Dustin', 'Smith', '011290MLUT', '29/09/1987', 'False', '2221', '9023', 'N/A')
        #     '''
        # cursor.execute(query)
        # cursor.commit()

        f = Passengers()
        f.table_init()
        self.p_label = self.findChild(QtWidgets.QLabel, 'Qinit_p_prompt')
        self.p_label.setText("Passengers table has been initialised")

    def flight_init(self):
        f = Flights()
        f.table_init()
        self.f_label = self.findChild(QtWidgets.QLabel, 'Qinit_flights_prompt')
        self.f_label.setText("Flights table has been initialised")

    def show_all_flights(self):
        f = FlightInfo()
        df = f.select_flights()
        model = pandasModel(f.select_flights())
        with open('df_f.txt', 'w') as f:
            f.write(df.to_string(header=False, index=False))
        self.show_passengers = self.findChild(QtWidgets.QTableView, 'Qflights_display_2')
        self.show_passengers.setModel(model)

    # Passenger Methods

    def show_all_passengers(self):
        p = Passengers()
        df = p.select_passengers()
        model = pandasModel(p.select_passengers())
        with open('df.txt', 'w') as f:
            f.write(df.to_string(header=False, index=False))
        self.show_passengers = self.findChild(QtWidgets.QTableView, 'Qpassengers_display')
        self.show_passengers.setModel(model)

    def create_manifest(self):
        self.show_passengers = self.findChild(QtWidgets.QTableView, 'Qpassengers_display')
        p = Passengers()
        # lineinout Qflight_number = lineedit
        self.input = self.findChild(QtWidgets.QLineEdit, 'Qflight_number')
        flightnumber = self.input.text()
        df = p.create_manifest_app(flightnumber)
        model = pandasModel(p.create_manifest_app(flightnumber))
        with open('dfm.txt', 'w') as f:
            f.write(df.to_string(header=False, index=False))

        self.show_passengers.setModel(model)

    # Insert passenger Info

    def insert_passenger_info(self):
        print("hello")
        self.first_name1 = self.findChild(QtWidgets.QLineEdit, 'Q_first_name_input')
        self.last_name1 = self.findChild(QtWidgets.QLineEdit, 'Q_last_name_input')
        self.passport1 = self.findChild(QtWidgets.QLineEdit, 'Q_passport_input')
        self.datebirth1 = self.findChild(QtWidgets.QLineEdit, 'Q_dob_input')
        self.flightnumber1 = self.findChild(QtWidgets.QLineEdit, 'Q_flight_number_input')
        self.air_miles1 = self.findChild(QtWidgets.QLineEdit, 'Q_airmiles_input')
        self.prev_flight1 = self.findChild(QtWidgets.QLineEdit, 'Q_previous_input')
        firstname = self.first_name1.text()
        print(firstname)
        lastname = self.last_name1.text()
        passportno = self.passport1.text()
        dob = self.datebirth1.text()
        upcoming_flight = "True"
        flight_number = self.flightnumber1.text()
        airmiles = self.air_miles1.text()
        previous_flights = self.prev_flight1.text()
        p = Passengers()
        p.insert_passenger_info_app(firstname, lastname, passportno, dob, upcoming_flight, flight_number, airmiles,
                                    previous_flights)

        self.f_label = self.findChild(QtWidgets.QLabel, 'Qconfirm_passenger_info')
        self.f_label.setText("Passenger info has been stored")
