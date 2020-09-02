from Project_MID_Airline.Planes.plane_info import Plane


class A380(Plane):
    def __init__(self, first_class_tickets=10, business_class_tickets=25, economy_class_tickets=100, fuel_capacity=5000,
                 avg_speed=500, total_capacity=135, plane_model="A380"):
        self.first_class_tickets = first_class_tickets
        self.business_class_tickets = business_class_tickets
        self.economy_class_tickets = economy_class_tickets
        self.fuel_capacity = fuel_capacity
        self.avg_speed = avg_speed
        self.total_capacity = total_capacity
        self.plane_model = plane_model




