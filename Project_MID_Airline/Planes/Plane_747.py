from Project_MID_Airline.Planes.plane_info import Plane


class B747(Plane):
    def __init__(self, first_class_tickets=20, business_class_tickets=45, economy_class_tickets=150, fuel_capacity=6000,
                 avg_speed=600, total_capacity=215, plane_model="747"):
        self.first_class_tickets = first_class_tickets
        self.business_class_tickets = business_class_tickets
        self.economy_class_tickets = economy_class_tickets
        self.fuel_capacity = fuel_capacity
        self.avg_speed = avg_speed
        self.total_capacity = total_capacity
        self.plane_model = plane_model


#
# plane = B747()
# print(plane.print_info())

