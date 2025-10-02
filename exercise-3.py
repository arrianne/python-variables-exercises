# Q3: Write a program that takes a distance in kilometers from the user, and output the distance in meters and centimeters.

def distance_converter(km):
    """Converts kilometers to meters and centimeters."""
    meters = km * 1000
    centimeters = km * 100000
    return meters, centimeters

# Get input from the user
km = float(input("Enter distance in kilometers: "))

# Call the function
meters, centimeters = distance_converter(km)

# Output the results
print(f"{km} Kilometers = {meters} meters")
print(f"{km} Kilometers = {centimeters} centimeters")
