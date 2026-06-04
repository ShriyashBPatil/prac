# Program 8h: Hybrid/Overriding: Vehicle start() in Car and Bike

class Vehicle:
    def __init__(self, name, fuel_type):
        self.name = name
        self.fuel_type = fuel_type

    def start(self):
        print(f"{self.name} is starting...")

    def display(self):
        print(f"Vehicle: {self.name}, Fuel: {self.fuel_type}")


class Car(Vehicle):
    def __init__(self, name, fuel_type, num_doors):
        super().__init__(name, fuel_type)
        self.num_doors = num_doors

    def start(self):
        print(f"{self.name} (Car) starts with key ignition. Vroom!")


class Bike(Vehicle):
    def __init__(self, name, fuel_type, bike_type):
        super().__init__(name, fuel_type)
        self.bike_type = bike_type

    def start(self):
        print(f"{self.name} (Bike) starts with a kick/self-start. Brrr!")


# Creating objects
print("Hybrid/Method Overriding Example:")
print("-" * 45)

v = Vehicle("Generic Vehicle", "Petrol")
v.start()

car = Car("Toyota Fortuner", "Diesel", 4)
car.start()

bike = Bike("Royal Enfield", "Petrol", "Cruiser")
bike.start()
