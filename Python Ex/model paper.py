# Input the number of tickets
adult=int(input("Enter number of adult tickets:"))
child=int(input("Enter number of child tickets:"))
senior=int(input("Enter number of senior citizen tickets:"))

# calculate total number of tickets
total_tickets= adult+child+senior

#calculate total ticket cost
total_cost=(adult*1500)+(child*800)+(senior*1000)

#apply 10% discount if there are 5 or more tickets
if total_tickets>=5:
    discount=total_cost*0.10
else:
    discount=0
finalamount=total_cost-discount

#Display results
print("Total ticket cost:Rs.",total_cost)
print("Discount:Rs.",discount)
print("Final amount payable:Rs.",finalamount)
    
