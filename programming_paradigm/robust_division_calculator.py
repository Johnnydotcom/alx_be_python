def safe_divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError(y)
        else:
            try:
                numerator = float(x)
                denominator = float(y)
                return f"The result of the division is {numerator / denominator}"
                #raise ValueError("Enter a numeric value.")
            except ValueError:
                print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")   