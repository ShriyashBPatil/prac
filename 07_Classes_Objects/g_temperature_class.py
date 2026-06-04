# Program 7g: Temperature class to convert Celsius to Fahrenheit

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def display(self):
        fahrenheit = self.to_fahrenheit()
        print(f"{self.celsius}°C = {fahrenheit}°F")


# Creating objects and converting
temp1 = Temperature(0)
temp2 = Temperature(100)
temp3 = Temperature(37)

print("Temperature Conversions:")
print("-" * 25)
temp1.display()
temp2.display()
temp3.display()
