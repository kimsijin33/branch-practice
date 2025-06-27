
def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("Input cannot be a negative number.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(10))
