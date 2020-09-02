# In this file, we will initialise the Plane class and determine the attributes each plane model has
# no methods yet


class Plane:
    def __init__(self, first_class_tickets=None, business_class_tickets=None, economy_class_tickets=None, fuel_capacity=None, avg_speed=None,
                 total_capacity=None, plane_model=None):
        self.first_class_tickets = first_class_tickets
        self.business_class_tickets = business_class_tickets
        self.economy_class_tickets = economy_class_tickets
        self.fuel_capacity = fuel_capacity
        self.avg_speed = avg_speed
        self.total_capacity = total_capacity
        self.plane_model = plane_model

    def flight_capacity(self):
        t_c = self.total_capacity = self.first_class_tickets + self.business_class_tickets + self.economy_class_tickets
        output = "Flight Capacity:" + str(t_c)
        return output

    def print_info(self):
        t_c = self.total_capacity = self.first_class_tickets + self.business_class_tickets + self.economy_class_tickets
        output = "Flight Capacity:" + str(t_c)
        fuel = "Fuel:" + str(self.fuel_capacity) + "litres"
        speed = "Speed:" + str(self.avg_speed) + "km"
        return str(output + '\n' +  fuel + '\n' + speed)


# This will go in a seperate file
class A380(Plane):
    def __init__(self, first_class_tickets = 10, business_class_tickets = 25, economy_class_tickets = 100, fuel_capacity = 5000, avg_speed = 500, total_capacity = 135, plane_model = "A380"):

        self.first_class_tickets = first_class_tickets
        self.business_class_tickets = business_class_tickets
        self.economy_class_tickets = economy_class_tickets
        self.fuel_capacity = fuel_capacity
        self.avg_speed = avg_speed
        self.total_capacity = total_capacity
        self.plane_model = plane_model

# Repeat this plane_model = "A380" for each parameter with what we want for each plane model


        # super().__init__(self, first_class_tickets, business_class_tickets, economy_class_tickets, fuel_capacity, avg_speed, total_capacity, plane_model):
# Task - to create subclasses in separate files that will contain information for each plane model
# - so that when we initialise the model, it inherits the methods of the parent class whilst keeping the attributes we have stated within the child class
