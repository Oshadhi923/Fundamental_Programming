number=int(input("Enter a positive integer number:"))
sum_of_numbers=0
count=1

while True:
    sum_of_numbers=sum_of_numbers+count
    count=count+1
    
    if count>number:
        break
    
print(f"The sum of numbers from 1 to {number} is: {sum_of_numbers}")
