angle1=int(input("Enter first angle value"))
angle2=int(input("Enter second angle value"))
angle3=int(input("Enter third angle value"))

if angle1>0 and angle2>0 and angle3>0 and (angle1+angle2+angle3==180):
    print("Traingle can be formed")
else:
    print("Traingle cannot be formed")