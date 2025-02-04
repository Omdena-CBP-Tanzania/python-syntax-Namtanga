def format_string(name, age):
    """
    Create a formatted string using f-strings.
    """
    return f"My name is {name} and I am {age} years old."

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    """
    return sum(numbers), max(numbers), min(numbers)

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    """
    return [name for name, score in students_dict.items() if score > 80]

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    """
    return set(list1) & set(list2)

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    """
    return {
        "Addition": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": a / b if b != 0 else "Undefined",
        "Modulus": a % b if b != 0 else "Undefined",
        "Exponentiation": a ** b
    }

def logical_ops(x, y):
    """
    Perform logical operations.
    """
    return {
        "AND": x and y,
        "OR": x or y,
        "NOT x": not x,
        "NOT y": not y
    }

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    """
    return {
        "AND": a & b,
        "OR": a | b,
        "XOR": a ^ b,
        "Left Shift a": a << 1,
        "Right Shift a": a >> 1,
        "Left Shift b": b << 1,
        "Right Shift b": b >> 1
    }

