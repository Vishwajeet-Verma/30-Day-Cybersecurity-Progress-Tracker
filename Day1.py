# Python: Variables & Data Types


# Aaj ka Target

# Day 1 ke end tak ye cheezein aani chahiye:

# 1 Python environment verify karna
# 2 Variables kya hain
# 3 Variable naming rules
# 4 int, float, str, bool
# 5 type() ka use
# 6 Type conversion — especially int()
# 7 f-string se formatted output
# 8 In concepts ko cybersecurity se connect karna





# 1 — Python Environment


# to check Python installed or not 

# in Terminal type : python --version 


# print("Hello, CyberSecurity!")



# 2 — Variable kya hota hai?
#  Variable ek naam hai jisme hum koi value store karte hain.

# name = "Vishwajeet"
# age = 25

# print("My Name is", name)
# print("I'm", age, "Years Old")




# 3 — Variables ke different Data Types

# core data types hain: int, float, str, aur bool


# int  # whole Number 

# age = 16
# mark = 49

# print(age)
# print(mark)

# print(type(age))    # type() function variable ka type batata hai.
# print(type(mark))



# float     # Decimal Number

# height = 5.8
# price = 99.99

# print(height)
# print(type(height))

# print(price)
# print(type(price))



# Str   # Text 

# name = "vashu"
# course = "BCA"

# print(name)
# print(type(name))

# print(course)
# print(type(course))


# bool  # Boolean it means 'True' or 'False'

# is_student = True
# is_absent = False

# print(is_student)
# print(type(is_student))

# print(is_absent)
# print(type(is_absent))




# Part 4 — type()
# type() batata hai ki kisi value ka data type kya hai.


# a = "Apple"
# b = 5
# c = 9.9
# d = True

# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# print(d)
# print(type(d))



# Sabse Important Difference


# a = 5
# b = "5"             # a and b both are different  # a is integer and b is String


# print (a + a)       # Output will be = 10
# print(b + b)           # Output will be = 55 because it's type string '5' + '5' = 55


# print(10 + 10)      # Result = 20 
# print("10" + "10")      # Result = 1010  # It is Just conjunction




# 6 — Type Conversion

# num1 = 10               # Integer 
# num2 = "20"             # String
# num3 = int("40")            # int is converting String to Integer 


# print(num1)
# print(type(num1))

# print(num2)
# print(type(num2))

# print(num3)
# print(type(num3))






# 7 — f-string

# name = "Vashu"
# age = 30
# course = "BCA"

# # Normal Way to Print Within Sentences

# print("My Name is", name)
# print("I am", age, "years old")
# print("My course is", course)


# print()         # Here Using extra print() function of line spacing

# # using f-string 

# print(f"My name is {name}")
# print(f"I am {age} years Old")
# print(f"My Course is {course}")






# Cybersecurity Connection


# ip_address = "192.168.1.10"
# port = 155
# is_open = True


# print(f"Your IP Address is {ip_address}")
# print(f"Open Port is {port}")
# print(f"It's {is_open}")




#  Overall Practice 


# name = "Vashu"
# age = 25
# height = 5.9
# is_student = True

# print()             # Space for top 
# print(" About Me  ")
# print(f"My name is {name}")
# print(f"and I am {age} years old")
# print(f"and my Height is {height}")
# print(f"and It's {is_student}")

























