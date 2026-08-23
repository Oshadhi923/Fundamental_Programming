print("Adventure Resort")
print("----------------")
print("\nAvailabe Package:")
print("1.Horse Ride")
print("2.Scuba Diving")
print("3.Water Rafting")

package=int(input("Enter the package type(1-3):"))
people=int(input("Enter the number of people:"))

if package==1:
    total=people*2000
elif package==2:
    total=people*5000
elif package==3:
    total=people*7000
else:
    total=0
    print("Invalid package")
if total>0:
    print("Total cost is:",total)