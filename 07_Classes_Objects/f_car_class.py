# Program 7f: Car class with show_details() method

class Car:
    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Price: ₹{self.price:,.2f}")
        print()


# Creating objects
car1 = Car("Toyota", "Fortuner", 2024, "White", 4500000)
car2 = Car("Hyundai", "Creta", 2025, "Black", 1500000)

print("Car 1 Details:")
car1.show_details()

print("Car 2 Details:")
car2.show_details()
