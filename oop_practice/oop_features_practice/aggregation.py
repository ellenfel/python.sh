class Vehicle:

    def __init__(self, color, lisence_plate, is_electric=False):
        self.color = color
        self.lisence_plate = lisence_plate
        self.is_electric = is_electric

    def show_lisence_plate(self):
        print(self.lisence_plate)

    def show_info(self):
        print("Vehicle: ")
        print(f"color: {self.color}")
        print(f"lisence plate: {self.lisence_plate}")
        print(f"electric: {self.is_electric}")

class Employee:
    
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    def show_vehicle_info(self):
        self.vehicle.show_info()


vehicle = Vehicle("Black", "BK201")
employee = Employee("Mori", vehicle)

print(employee.show_vehicle_info())