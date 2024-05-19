def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get input from the user
number = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(number)

# Print the result
print(f"The factorial of {number} is {result}")