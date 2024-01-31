# Python code to calculate the area of a circle

import math  # Import the math module for using pi

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * radius**2

# Display the result
print(f"The area of the circle with radius {radius} is: {area}")