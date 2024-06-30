num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sign = input("Choose the operation (+, -, *, /): ")

match sign:
    case "+":
        print("The result is", num1 + num2)

    case "-":
        print("The result is", num1 - num2)

    case "*":
        print("The result is", num1 * num2)

    case "/":
        print("The result is", num1 / num2)

    case_:
        print("Invalid operation")
