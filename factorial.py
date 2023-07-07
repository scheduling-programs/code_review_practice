def factorial(n):
    # Calculates the factorial of n
    if n < 0:
        return "Sorry, factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # This should print 120
