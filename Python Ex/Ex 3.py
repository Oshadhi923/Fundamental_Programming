print("Adventure Resort")
print("-----------------")
print("Available Packages")
print("1.Horse ride")
print("2.Scuba Diving")
print("3.Water Rafting")

while True:
    package_type=int(input("Enter package type(1,2,3):"))
    if package_type==1:
        cost_per_person=2000
    elif package_type==2:
        cost_per_person=5000
    elif package_type==3:
        cost_per_person=7000
    else:
        print("Invalid package type")
        continue
    
    no_of_people=int(input("Enter the number of people:"))
    total_cost=cost_per_person*no_of_people

    print(f"Total Amount to Pay:Rs. {total_cost}")
        
   
    
        

        
