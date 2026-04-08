def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(f"Factorial of 5 is {factorial_recursive(5)}")