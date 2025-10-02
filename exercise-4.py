# Q4: Write a program that takes the user's name and height (in centimeters), and outputs a summary sentence.

name = input("What is your name?: ")
height = input("How tall are you in cm ")

def get_name(name, height):
    """Returns a summary sentence with the user's name and height."""
    return name, height

print(f"{name} is {height} cm tall.")