# Day 2 Learning Goals

# Aaj ye concepts seekhna Hai :

# if
# elif
# else
# Comparison operators
# and
# or
# not
# Multiple conditions
# Basic access-control logic
# Cybersecurity me conditional logic ka use



# if

# age = int(input("Enter Your Age: "))

# if age >= 18:             # yadi age 18 ya is se zyada hoga toh Adult Print hoga.
#     print("You are Adult.")
# else:                     # yadi age 18 se kam hoga toh Minor Print Hoga.
#     print("You are Minor.")




# Questions Practice on Day 2 Topics : 


# if

# mark = int(input("Enter Your Number: "))
# if mark >= 30:
#     print(" Pass")
    
# else:
#     print(" Fail")




# Q2. if-else
# 18 or above → Adult
# below 18   → Minor

# age = int(input("Enter Your Age: "))
# if age >= 18:
#     print("You are Adult.")
# else:
#     print("You are Minor.")



# if-elif-else
# User se number input lo aur check karo:

# Positive
# Negative
# Zero


# num = int(input("Enter Your Number: "))

# if num > 0:
#     print("Positive Number")
# elif num < 0:
#     print("Negitive")
# else :
#     print("Zero")


# Q4. ==

# User se password input lo.

# Agar password exactly: python123
 
# hai to: Correct Password

# warna:  Wrong Password


# passwrd = input("Enter Your Password: ")
# if passwrd == "python123" :
#     print("Correct Password.")
# else:
#     print("Incorrect Password.")



# Q5. !=

# User se username input lo.

# Agar username "admin" nahi hai:

# Normal User

# warna:

# Admin User



# username = input("Enter Your Username: ")
# if username == "admin":
#     print("Admin User")
# else:
#     print("Normal User")





# Q6. > and <

# User se do numbers lo aur check karo:

# First number greater
# First number smaller
# Both are equal


# num1 = int(input("Enter Your First Number: "))
# num2 = int(input("Enter Your Second Number: "))

# if num1 > num2 :
#     print(f"First Number {num1} is Grater Than, Second Number {num2}")
# elif num1 < num2:
#     print(f"First Number {num1} is Less Than, Second Number {num2}")
# else:
#     print("Both are Equal")





# Q7. >= and <=

# User se age lo.

# Check karo ki age 18 se 60 ke beech hai ya nahi.

# Output:      # Eligible

# ya

# Not Eligible

# age = int(input("Enter Your age: "))
# if age >= 18 and age <= 60:
#     print("You are Eligible.")
# else: 
#     print("You are not Eligible.")






# Logical Operators

# Q8. and

# User se:  age, marks

# lo.

# Student tab eligible hai jab:

# age >= 18 AND marks >= 40

# Output:  Eligible
# otherwise: Not Eligible


# age = int(input("Enter Your age: "))
# marks = int(input("Enter Your marks: "))

# if age >= 18 and marks >= 40 : 
#     print("You are Eligible.")
# else:
#     print("You are Not Eligible.")



# Q9. or

# User se poochho:

# Are you admin? (yes/no)
# Are you manager? (yes/no)

# Agar admin OR manager hai: # Access Allowed

# otherwise: # Access Denied


# admin = input("Are you admin? (yes/no): ")
# manager = input("Are you manager? (yes/no): ")

# if admin == "yes" or manager == "yes":
#     print("Access Allowed")
# else:
#     print("Access Denied")




# Q10. not

# Variable:  is_logged_in = False

# not ka use karke print karo: Please Login

# jab user logged in nahi hai.




# is_logged_in = False
# if not is_logged_in :
#     print("Please Login")
# else:
#     print("Already Logged In")



# Q11. Multiple Conditions

# User se: username password lo.

# Access tab allowed ho jab: username == "admin" AND password == "python123"

# Output: Login Successful 
# otherwise: Login Failed


# username = input("Enter Your Username: ")
# password = input("Enter Your Password: ")

# if username == "admin" and password == "python123":
#     print("Login Successful")
# else:
#     print("Login Failed")




# Q12. Cybersecurity Challenge

# Ek basic security checker banao.

# User se: username password lo.

# Rules:
# Username empty nahi hona chahiye
# AND
# Password length >= 8

# Agar dono conditions true hain: Access Granted

# otherwise: Access Denied



# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username != "" and len(password) >= 8:           # len(password) yaha par iska mtlb yeh hai ki password ki length kitni hai
#     print("Access Granted")
# else:
#     print("Access Denied")






# Bonus Challenge

# Ek program banao jo user se: username password is_admin le.

# Access Granted tab ho jab:  username non-empty AND password length >= 8 AND is_admin == "yes"

# Otherwise: Access Denied


# username = input("Enter your username: ")
# password = input("Enter your Password: ")
# is_admin = input("Are You admin? (yes/no): ")

# if username != "" and len(password) >= 8 and is_admin == "yes":
#     print("Access Granted")
# else:
#     print("Access Denied")





# Revision Complete 
# Lets Move on Third Day of Python Coding =>
# Thankyou !








