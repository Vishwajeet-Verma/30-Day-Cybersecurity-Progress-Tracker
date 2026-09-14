# Day 5 — Python Functions
# 1. Function kya hota hai?

# Simple language mein:
# Function = ek reusable code block jo ek specific kaam karta hai.
# Maan lo tumhe 10 baar check karna hai ki number even hai ya odd.
# Function ke bina:


# num = 10

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Agar baar-baar karna ho toh same logic repeat karna padega.

# Function ke saath:

# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # Ab ise multiple times use kar sakte ho:

# print(check_even_odd(10))
# print(check_even_odd(7))
# print(check_even_odd(25))

# Output:
# Even
# Odd
# Odd





# 2. Function ka basic syntax
# def function_name():
    # code

# Example:

# def hello():
    # print("Hello Vishwajeet!")

# Function define karne se woh automatically execute nahi hota.
# Use call karna padega:

# hello()

# Output:
# Hello Vishwajeet!

# Yaad rakho:
# def hello():   #   → Function banana
# hello()        #   → Function chalana





# 3. Parameter kya hota hai?

# Function ko input dene ke liye parameter use karte hain.

# def greet(name):
    # print("Hello", name)

# Yahan name parameter hai.
# Call:
# greet("Vishwajeet")
# greet("Rahul")

# Output:
# Hello Vishwajeet
# Hello Rahul
# Flow:
# greet("Vishwajeet")
#         # ↓
#       name
#         ↓
# print("Hello", name)






# 4. Parameter vs Argument

# Ye important hai 👇
# def greet(name):
# name = parameter

# Aur:
# greet("Vishwajeet")
# "Vishwajeet" = argument

# Simple trick:
# Parameter = function banate time
# Argument = function call karte time






# 5. Multiple Parameters

# Ek function mein multiple parameters ho sakte hain.
# def add(a, b):
#     print(a + b)
# Call:
# add(10, 20)

# Output:
# 30
# Yahan:
# a = 10
# b = 20






# # 6. return — bahut important 

# Ab print() aur return ka difference samjho.

## print()
# def add(a, b):
#     print(a + b)

# add(10, 20)

# Ye result screen par print karega.

## return
# def add(a, b):
#     return a + b

# result = add(10, 20)
# print(result)

# Output:
# 30
# return function ka result bahar bhejta hai.
# Isliye hum result ko variable mein store kar sakte hain:
# result = add(10, 20)






# 7. return ke baad kya hota hai?
# def test():
#     return 10
#     print("Hello")

# "Hello" print nahi hoga.
# Kyunki:
# return
# function ko wahi stop kar deta hai.







# Cybersecurity Connection

# Functions cybersecurity mein bahut important hain.
# Example:
# Password checker mein alag-alag functions ho sakte hain:

# has_min_length()
#        ↓
# has_number()
#        ↓
# has_special()
#        ↓
# check_common_password()
#        ↓
# final_password_result()

# Matlab ek huge code likhne ke bajay small-purpose functions banate hain.
# Ye exactly Day 5 roadmap ka cybersecurity connection hai.




# 8. Default Parameter

# Function mein parameter ki default value bhi de sakte ho.

# def greet(name="User"):
#     print("Hello", name)

# Agar argument nahi diya:
# greet()
# Output:
# Hello User

# Argument diya:
# greet("Vishwajeet")
# Output:
# Hello Vishwajeet

# Matlab:
# def greet(name="User"):
# "User" default value hai.




# Ab ek proper example
# Number even/odd check
# def check_even_odd(num):

#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# result = check_even_odd(15)
# print(result)

# Flow:
# 15
#  ↓
# check_even_odd(15)
#  ↓
# 15 % 2
#  ↓
# remainder = 1
#  ↓
# Odd
#  ↓
# return "Odd"
#  ↓
# result
#  ↓
# print(result)
# Output:
# Odd



# Day 5 Practice

# Ab easy → medium → advanced order mein questions karne hain.


# Level 1 — Basics

# Q1. Ek function hello() banao jo print kare:

# Hello, Python!


# def hello():
#     print("Hello, Python!")
# hello()


# Q2. Ek function square(num) banao jo number ka square return kare.
# Example:
# square(5)
# Output:
# 25

# def square(num):
#     return num ** 2     # yah power ke liye jo number user se lenge uske itself multiplication se square nikal jayega, mtlb n * n    
          
# n = int(input("Enter Your Number: "))
# result = square(n)
# print(result)



# Q3. Ek function add(a, b) banao jo dono numbers ka sum return kare.

# def add(a , b):
#     return a + b

# a = int(input("Enter Your First Number: "))
# b = int(input("Enter Your Second Number: "))

# result = add(a, b)
# print(result)





# Level 2 — Parameters + Conditions

# Q4. Function check_age(age) banao:

# age >= 18 → "Adult"
# otherwise → "Minor"


# age = int(input("Enter Your Age: "))

# def check_age(age):
#     if age >= 18:
#         return "Adult"
#     else:
#         return "Minor"

# print(check_age(age))







# Q5. Function check_even(num) banao jo True return kare agar number even hai, otherwise False.

# Example:
# print(check_even(10))
# Output:
# True


# num = int(input("Enter your number: "))
# def check_even(num):
#     if num % 2 == 0:
#         return True
#     return False      #Python me jab function ke pehle block me return lag jata hai, toh function wahi par end ho jata hai. Isliye else lagaye bina bhi ise likha ja sakta hai:
# print(f"\t {num} is \n    == Even Number ==  ")  # yaha pr \n se new line pirnt hogi aur \t ek tab space add hoga
# print(check_even(num))








# Level 3 — Day 5 Roadmap Practice 

# Q6. Prime Number Function

# Function:
# is_prime(num)
# banao jo check kare number prime hai ya nahi.

# Example:
# is_prime(7) → True
# is_prime(10) → False

# Hint:
# for i in range(2, num):



# num = int(input("Enter your number: "))

# def is_prime(num):
#     if num <= 1:
#         return False
    
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#         return True

# print(f"\t {num}  \n   Is Prime Number")
# print(f" => {is_prime(num)}")






# Q7. Strong Password Function

# Function:

# is_strong_password(password)

# banao jo length ke basis par True/False return kare.

# Example rule:

# 8 or more characters → True
# less than 8 → False



# password = input("Enter Your Passowrd: ")

# def is_strong_password(password):
#     if len(password) >= 8:
#         return True
#     return False

# print(is_strong_password(password))




# Q8. Average Function

# Ek function:

# average(numbers)
# banao jo list ke numbers ka average return kare.

# Example:
# numbers = [10, 20, 30, 40, 50]

# Expected:
# 30.0
# Is question mein tumhari Day 4 Lists + Day 5 Functions dono ki revision hogi.


# num1 = float(input("Enter Your Number: "))
# num2 = float(input("Enter Your Number: "))
# num3 = float(input("Enter Your Number: "))
# num4 = float(input("Enter Your Number: "))

# numbers = [num1, num2, num3, num4]

# def average(numbers):
#     return sum(numbers) / len(numbers)

# print(f"Average of Your Given Number Is => {average(numbers)}")






# Day 5 Task — Security Functions

# Roadmap ka main task:

# has_min_length()
# has_number()
# has_special()

# In 3 separate functions ko banana hai.
# Pehle sirf functions individually banao.
# Function 1
# has_min_length(password)
# Check:
# password length >= 8
# Return:
# True / False
# Function 2
# has_number(password)
# Check kare password mein koi number hai ya nahi.
# Example:
# "hello123" → True
# "helloworld" → False
# Function 3
# has_special(password)
# Check kare password mein special character hai ya nahi.
# Example:
# "hello@123" → True
# "hello123" → False
# Abhi in teenon ko combine mat karo. Pehle individually clean functions likho. Day 7 project mein inhe combine karna hai.


# password = input("Enter Your Password: ")
# def has_min_length(password):
#     if len(password) >= 8:
#         return True
#     return False
# print(f"\t '{password}' is it more than 8 character?")
# print(f"\t {has_min_length(password)}")

# def has_number(password):
#     for num in password:
#         if num.isdigit():
#             return True
#     return False
# print(f"\n\t '{password}' has it number?")
# print(f"\t {has_number(password)}")

# def has_special(password):
#     for special_symbol in password:
#         if not special_symbol.isalnum() and not special_symbol.isspace():
#             return True
#     return False
# print(f"\n\t '{password}' has it Special Character?")
# print(f"\t {has_special(password)}")




# Aaj ka learning order
# 1. def
#    ↓
# 2. Function call
#    ↓
# 3. Parameters
#    ↓
# 4. Arguments
#    ↓
# 5. return
#    ↓
# 6. Default parameters
#    ↓
# 7. Conditions inside functions
#    ↓
# 8. Lists + Functions
#    ↓
# 9. Security functions




# Day 5 Complete 
# Lets Move on Sixth Day of Python Coding =>
# Thankyou !
