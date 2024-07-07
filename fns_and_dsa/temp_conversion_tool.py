
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = float(input("Enter the temperature to conver: "))
sign = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").islower
def convert_to_celsius(fahrenheit):
    cel = ((temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR)
def convert_to_fahrenheit(celsius):
    fah = ((temp + 32) * CELSIUS_TO_FAHRENHEIT_FACTOR)

    if sign == "c":
         print (f"{cel} is = {fah}")
    else:
        print(f"{fah} is = {cel} ")