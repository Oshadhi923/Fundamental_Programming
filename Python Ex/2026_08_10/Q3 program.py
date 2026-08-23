number=int(input("Enter a number:"))
range_value=int(input("Enter the range:"))

multiplier=1

while multiplier<=range_value:
    result=number*multiplier
    print(number,"X",multiplier,"=",result)
    multiplier +=1