from Project_MID_Airline.Flights.flight_path import FlightInfo
from Project_MID_Airline.Planes.Plane_747 import *
from Project_MID_Airline.Planes.Plane_A381 import *
from Project_MID_Airline.Planes.Plane_787 import *

class FlightsFunctions(FlightInfo):


    def fuel_check(self):
        if self.plane_model == "747":
            plane = B747()
            if self.distance > plane.fuel_capacity:
                return "WARNING: This 747 needs refuelling!"
            else:
                return "This 747 is OK to fly!"
        elif self.plane_model == "787":
            plane = B787()
            if self.distance > plane.fuel_capacity:
                return "WARNING: This 787 needs refuelling!"
            else:
                return "This 787 is OK to fly!"
        elif self.plane_model == "A380":
            plane = A380()
            if self.distance > plane.fuel_capacity:
                return "WARNING: This A380 needs refuelling!"
            else:
                return "This A380 is OK to fly!"

