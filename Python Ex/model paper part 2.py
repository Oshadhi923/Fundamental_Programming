def calculateAverage(marks):
    total=sum(marks)
    average=total/5
    return average
#create an array to store marks
marks=[]

#input marks for five students
for i in range(5):
    mark=int(input("Enter mark for student"+ str(i+1)+":"))
    marks.append(mark)

#calculate average
average=calculateAverage(marks)

#find highest mark
highest=max(marks)

#display results
print("Average mark:",average)
print("Highest mark:",highest)