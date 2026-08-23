total=0
count=0

#Get first input from the user
grade=int(input("Enter mark,-1 to end:"))

while grade !=-1:
    total=total+grade
    count=count+1
    
    #Get next input
    grade=int(input("Enter mark,-1 to end:"))
    
if count !=0:
    average=total/count
    print("Class average is:",average)
else:
    print("No grades were entered.")