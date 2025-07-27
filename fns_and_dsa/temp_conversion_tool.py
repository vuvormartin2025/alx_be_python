# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factor"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factor"""
    fahrenheit = celsius * (CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


user_input = int(input("Enter the temperature to convert:"))
temp = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if temp.lower() == "c":
    calc = convert_to_fahrenheit(user_input)
    print(calc)

elif temp.lower() == "f":
    calc = convert_to_celsius(user_input)
    print(calc)

else:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
