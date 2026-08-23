print("Simple Calculator")
print("-----------------")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("\nChoose an Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

operation=int(input("Enter the Operation(1-4):"))

if operation==1:
    Result=num1+num2
elif operation==2:
    Result=num1-num2
elif operation==3:
    Result=num1*num2
elif operation==4:
    Result=num1/num2
if operation>=1 and operation<=4:
    print("Result is:", Result)
else:
    print("Invalid Operation")
    
        
         