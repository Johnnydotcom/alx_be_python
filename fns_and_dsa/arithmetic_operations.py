def perform_operation(num1, num2, operation):
    if operation == "*":
        print({num1} * {num2})
    elif operation == "+":
        print({num1} + {num2})
    elif operation == "-":
        print({num1} - {num2})
    elif operation == "/":
        if num2 == 0:
            print("Not divisble by zero")
    else: 
        print({num1} / {num2})