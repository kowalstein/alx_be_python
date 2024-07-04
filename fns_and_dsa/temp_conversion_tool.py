""" This script define functions to convert temperatures between
    Celsius and Fahrenheit, demonstrating the use of global variables
    to store conversion factors that are accessible within functions."""

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    return fahrenheit

temp = input ("Enter the temperature to convert: ")
choice = input ("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    
if temp.isnumeric() and choice == 'F':
        print (f"{int(temp)}°F is {convert_to_celsius(int(temp))}°C")
elif temp.isnumeric() and choice == 'C':
        print (f"{int(temp)}°C is {convert_to_fahrenheit(int(temp))}°F")
else:
        print ("Invalid temperature. Please enter a numeric value.")
