def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        return "TypeError: unsupported operand type(s) for /: 'str' and 'int'"
except ZeroDivisionError:
        return "ZeroDivisionError: division by zero"
except Exception as e:
        return f"An unexpected error occurred: {e}"

#Example
result1 = function_with_uncommon_error(10, 2)  # Output: 5.0
result2 = function_with_uncommon_error(10, 0)  # Output: ZeroDivisionError: division by zero
result3 = function_with_uncommon_error(10, "hello") # Output: TypeError: unsupported operand type(s) for /: 'int' and 'str'