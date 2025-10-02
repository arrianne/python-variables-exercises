# Q1: Write a program that takes two numbers from the user, and outputs their sum.


def get_number(prompt):
    """Prompts the user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 5, 42, -3).")

def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

# Main program
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

result = add_numbers(num1, num2)
print("The sum is:", result)
