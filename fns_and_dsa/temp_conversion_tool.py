
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = float(input("Enter the temperature to convert: "))
sign = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
def convert_to_celsius(fahrenheit):
    cel = (temp * CELSIUS_TO_FAHRENHEIT_FACTOR )+ 32
    return cel
def convert_to_fahrenheit(celsius):
    fah = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return fah
if sign == "c":
    converted_temp = convert_to_celsius(temp)
    print (f"{temp}C is = {converted_temp}F")
elif sign == "f":
    converted_temp = convert_to_fahrenheit(temp)
    print(f"{temp}F is {converted_temp}C")
else:
    print("Invalid input.")