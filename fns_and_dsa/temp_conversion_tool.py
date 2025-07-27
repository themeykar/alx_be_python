FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    fahrenheit_value = (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return fahrenheit_value


def convert_to_fahrenheit(celsius):
    celsius_value = (float(celsius)  * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return celsius_value

temperature = float(input("Enter the temperature to convert: "))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if temperature_type == "F":
    cel_number = convert_to_celsius(temperature)
    print(f"{temperature} {temperature_type} is {cel_number} C")

elif temperature_type == "C":
    fah_number = convert_to_fahrenheit(temperature)
    print(f"{temperature} {temperature_type} is {fah_number} F")