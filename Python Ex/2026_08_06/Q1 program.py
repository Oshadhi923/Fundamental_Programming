import math

shape = input("Enter the first character of the shape(R-Rectangle,T-Triangle,C-Circle):")
area = 0.0

if shape == "R" or shape == "r":
    length = float(input("Enter the length of rectangle:"))
    width = float(input("Enter the width of rectangle:"))
    area = length * width
elif shape == "T" or shape == "r":
    base = float(input("Enter the base of the triangle:"))
    height = float(input("Enter the height of the triangle:"))
    area = 0.5 * base * height
elif shape == "C" or shape == "c":
    radius = float(input("Enter the radius of the circle:"))
    area = math.pi * radius * radius
else:
    print("Invalid shape entered")
    
print("Shape area is", area)

