temp = float(input("Enter the temperature to conver: "))
sign = float(input("Is this temperature in Celsius or Fahrenheit? (C/F): ").isupper)

F = 5/9
C = 9/5
def convert_to_celsius(fahrenheit):
    cel = (F * 9/5)+ 32
def convert_to_fahrenheit(celsius):
    fah = (C * 9/5)+32 

print (f"{cel} is {fah}")