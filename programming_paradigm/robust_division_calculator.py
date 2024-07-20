def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError(denominator)
        else:
            try:
                numerator = float(numerator)
                denominator = float(denominator)
                return f"The result of the division is {numerator / denominator}"
            except ValueError:
                print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")