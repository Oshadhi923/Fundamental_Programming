def area_of_rectangle():
    width = float(input("Enter width:"))
    length = float(input("Enter length:"))
    area_r = width * length
    return area_r

def area_of_circle():
    radius = float(input("Enter radius:"))
    pi = 22/7
    area_c = pi * radius *radius
    return area_c

def area_of_green(area_y,area_b,area_p):
    area_g = area_y - (area_b + area_p)
    print("Area need to plant grass is:", area_g)
    
def perimeter_of_yard():
    print("\nTo find perimeter of yard enter width & length")
    width = float(input("Enter width:"))
    length = float(input("Enter length:"))
    perimeter = 2 * (width + length)
    print("Perimeter of yard:", perimeter)

#Main program
print("Enter width and length of yard")
area_y = area_of_rectangle()

print("Enter width and width of Building")
area_b = area_of_rectangle()

print("Enter radius of pond")
area_p = area_of_circle()

if (area_b + area_p) > area_y:
    print ("Invalid value")
else:
    area_of_green(area_y,area_b,area_p)
    
perimeter_of_yard()



