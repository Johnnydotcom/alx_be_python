def safe_divide(numerator, denominator):
    try:
                numerator = float(numerator)
                denominator = float(denominator)
                if denominator == 0:
                    raise ZeroDivisionError("Cannot dicide by zero.")
                return f"The result of the division is {numerator / denominator}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError as e:
        return f"Error: {e}"