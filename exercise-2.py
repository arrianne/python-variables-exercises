# Q2: Write a program that takes two numbers from the user, and outputs the equation representing the multiplication of the two numbers.



# keep prompting the user until a valid integer is entered

def get_number(prompt):
    """Prompts the user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 5, 42, -3).")



def equation_output(num1, num2):

    num1 = int(num1)
    num2 = int(num2)
    return f"{num1} * {num2} = {num1 * num2}"


    """Returns a string representing the multiplication equation of two numbers."""
    print (f"{num1} * {num2} = {num1 * num2}")

num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")   

# Call the function and print its result
print(equation_output(num1, num2))






