def calculate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
print(calculate_numbers(x=1, y=3))
print(calculate_numbers(1, 3, "subtract"))
print(calculate_numbers(y=1, x=3, operation="subtract"))