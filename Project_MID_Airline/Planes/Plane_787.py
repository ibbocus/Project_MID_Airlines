from Project_MID_Airline.Planes.plane_info import Plane

class B787(Plane):
    def __init__(self, first_class_tickets = 70, business_class_tickets = 90, economy_class_tickets = 250, fuel_capacity = 8000, avg_speed = 650, total_capacity = 410, plane_model = "787"):

        self.first_class_tickets = first_class_tickets
        self.business_class_tickets = business_class_tickets
        self.economy_class_tickets = economy_class_tickets
        self.fuel_capacity = fuel_capacity
        self.avg_speed = avg_speed
        self.total_capacity = total_capacity
        self.plane_model = plane_model

