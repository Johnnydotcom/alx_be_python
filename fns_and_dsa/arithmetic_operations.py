def perform_operation(num1, num2, operation):
    if operation == "multiply":
        print({num1 * num2})
    elif operation == "add":
        print({num1 + num2})
    elif operation == "subtract":
        print({num1 - num2})
    elif operation == "divide":
        if num2 == 0:
            print("Not divisble by zero")
    else:
        print({num1 / num2})
    return(0)