import math
shape = input("Enter the first character of the shape(R for Rectangle, T for Traingle, C for Circle):")

area = 0.0
if shape == 'R' or shape == 'r':
    length = float (input("Enter length of the rectangle:"))
    width = float (input("Enter width of the rectangle:"))
    area = length * width
    
elif shape == 'T' or shape == 't':
    base = float (input("Enter the base length of the traingle:"))
    heigth = float (input("Enter the heigth of the traingle:"))
    area = 0.5 * base * heigth
    
elif shape == 'C' or shape == 'c':
    radius = float(input("Enter the radius of the traingle"))
    area = math.pi * radius * radius
else:
    print("Invalid shape entered.")
print("The area of the shape is:",area)