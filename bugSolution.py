def function_with_uncommon_error(a, b):
    try:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            result = a / b
            return result
        else:
            raise TypeError("Unsupported operand type(s) for /: must be int or float")
    except TypeError as e:
        return f"TypeError: {e}"
    except ZeroDivisionError as e:
        return f"ZeroDivisionError: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

#Example
result1 = function_with_uncommon_error(10, 2)  # Output: 5.0
result2 = function_with_uncommon_error(10, 0)  # Output: ZeroDivisionError: Division by zero
result3 = function_with_uncommon_error(10, "hello") # Output: TypeError: Unsupported operand type(s) for /: must be int or float
result4 = function_with_uncommon_error("hello",10) # Output: TypeError: Unsupported operand type(s) for /: must be int or float