# Q1: Write a program that takes two numbers from the user, and outputs their sum.

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

# Call the function and print the result
result = add_numbers(num1, num2)
print("The sum is:", result)