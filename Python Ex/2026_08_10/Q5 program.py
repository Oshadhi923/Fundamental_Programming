correct_password="password123"
password=""
attempt=0

while password != correct_password and attempt<3:
    password = input("Enter password:")
    
    if password != correct_password:
      attempt=attempt+1
      print("Incorrect password.Please try a gain.")
    
if password == correct_password:
    print("Access granted.Welcome!")
else:
    print("Access denied.You have entered the password 3 times.")