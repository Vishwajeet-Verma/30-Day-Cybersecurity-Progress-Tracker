# Aaj ka topic Cyber Security ke liye kaafi important hai, kyunki logs read karna aur unexpected errors ko safely handle karna Blue Team / security automation ka basic part hai.

# Roadmap ke according aaj hum 3 main cheezein karenge:

# 1. File Open / Close
#        ↓
# 2. Read & Write Files
#        ↓
# 3. try / except / finally
#        ↓
# 4. Security Log Analysis







# 1. File Handling kya hai?

# Python se hum kisi .txt, .log etc. file ko:
# read kar sakte hain
# write kar sakte hain
# existing content modify/append kar sakte hain

# Example file:
# users.txt
# Uske andar:

# vashu
# rahul
# govind
# vansh

# Python se hum is file ko read kar sakte hain.



# 2. open() Function

# File open karne ka basic syntax:
# file = open("users.txt", "r")

# Yahan:
# open()       → file open karta hai
# users.txt    → file ka naam
# "r"          → read mode
# Common modes:
# Mode	Meaning
# "r"	Read
# "w"	Write
# "a"	Append
# ⚠️ Important

# "w" use karne par existing content overwrite ho sakta hai.
# "a" existing content ke end mein new content add karta hai.






# 3. File Read karna

# Suppose users.txt:
# vashu
# rahul
# govind
# vansh

# # Code:
# file = open("users.txt", "r")
# content = file.read()
# print(content)
# file.close()

# Output:

# vashu
# rahul
# govind
# vansh

# file.close() kyun?

# File ka kaam complete hone ke baad file ko close karna good practice hai.







# 4. with open() — Better Way 🔥

# Python mein recommended/simple approach:
# with open("users.txt", "r") as file:
#     content = file.read()
# print(content)

# Yahan manually:
# file.close()

# likhne ki zarurat nahi.
# with block complete hone ke baad Python file ko automatically close kar deta hai.
# Yaad rakho:
# open()        → file open
# read()        → content read
# write()       → content write
# with          → safely manage file





# 5. File mein Write karna

# Suppose hume usernames file mein save karne hain.

# with open("users.txt", "w") as file:
#     file.write("vashu\n")
#     file.write("rahul\n")
#     file.write("govind\n")

# File:
# vashu
# rahul
# govind
# \n kya hai?
# \n = new line
# Without \n:
# file.write("vashu")
# file.write("rahul")
# Output:
# vashurahul
# With \n:
# file.write("vashu\n")
# file.write("rahul\n")
# # Output:
# vashu
# rahul






# 6. List ko File mein Write karna

# Ye tumhare Day 4 Lists ka revision bhi hai.
# usernames = ["vashu", "rahul", "govind", "vansh"]
# with open("users.txt", "w") as file:
#     for username in usernames:
#         file.write(username + "\n")

# Ab users.txt:
# vashu
# rahul
# govind
# vansh
# Yahan:
# List
#  ↓
# for loop
#  ↓
# file.write()
#  ↓
# users.txt
# Ye Day 4 + Day 6 combination hai.






# 7. File ko Line-by-Line Read karna

# Security logs mein hume often har line separately process karni hoti hai.
# with open("users.txt", "r") as file:
#     for line in file:
#         print(line)
# Lekin output mein extra blank lines aa sakti hain because line ke end mein already \n hota hai.

# Better:
# with open("users.txt", "r") as file:
#     for line in file:
#         print(line.strip())
# .strip()
# Extra whitespace/newline remove karta hai.








# 8. try / except 

# Ab maan lo user ek file open karne ki koshish karta hai jo exist hi nahi karti.
# with open("abc.txt", "r") as file:
#     print(file.read())

# Agar abc.txt nahi hai, program error dega:
# FileNotFoundError
# Problem ye hai ki program crash ho sakta hai.
# Isliye:
# try:
#     with open("abc.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found.")
# Ab program crash nahi karega.
# Output:
# File not found.







# 9. try aur except ka logic

# Simple flow:
# try
#  ↓
# Risky code
#  ↓
# Error?
#  ├── No → Continue
#  │
#  └── Yes
#        ↓
#      except
#        ↓
#    Handle error

# Example:
# try:
#     num = int(input("Enter number: "))
#     print(100 / num)

# except ValueError:
#     print("Please enter a valid number.")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# Yahan do possible errors handle ho rahe hain.

# Agar user:
# 10
# Output:
# 10.0
# Agar:
# abc
# Output:
# Please enter a valid number.
# Agar:
# 0
# Output:
# Cannot divide by zero.






# 10. finally

# finally block normally execute hota hai chahe error aaye ya na aaye.

# try:
#     num = int(input("Enter number: "))
#     print(100 / num)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# finally:
#     print("Program finished.")

# Agar 0:

# Cannot divide by zero.
# Program finished.

# Agar 10:

# 10.0
# Program finished.

# Simple:

# try      → risky code
# except   → error handle
# finally  → cleanup/final code






# 10. finally

# finally block normally execute hota hai chahe error aaye ya na aaye.
# try:
#     num = int(input("Enter number: "))
#     print(100 / num)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# finally:
#     print("Program finished.")
# Agar 0:
# Cannot divide by zero.
# Program finished.
# Agar 10:
# 10.0
# Program finished.
# Simple:
# try      → risky code
# except   → error handle
# finally  → cleanup/final code






# Cybersecurity Connection

# Ab actual cybersecurity connection samjho.
# Server/application mein logs ho sakte hain:

# LOGIN SUCCESS username=vashu
# LOGIN FAILED username=rahul
# LOGIN SUCCESS username=govind
# LOGIN FAILED username=test

# Security analyst ko pata karna ho:
# Kitne failed login attempts hue?
# Python file ko read karke automatically count kar sakta hai.
# Ye basic log analysis hai.







# Day 6 Main Task

# Pehle ek file banao:
# login.log
# Usmein fake data:

# LOGIN SUCCESS username=vashu
# LOGIN FAILED username=rahul
# LOGIN SUCCESS username=govind
# LOGIN FAILED username=test
# LOGIN FAILED username=admin
# LOGIN SUCCESS username=vansh

# Ab Python:
# try:

#     with open("login.log", "r") as file:
#         failed_count = 0
#         for line in file:
#             if "FAILED" in line:
#                 failed_count += 1
#     print("Failed Login Attempts:", failed_count)
# except FileNotFoundError:
#     print("Log file not found.")
# Output:
# Failed Login Attempts: 3
# Is code ka flow:
# login.log
#     ↓
# open file
#     ↓
# read each line
#     ↓
# "FAILED" present?
#     ↓
#    YES
#     ↓
# failed_count += 1
#     ↓
# print total


# Important: failed_count += 1
# Ye tumhare previous loops ka revision hai.
# Starting:
# failed_count = 0
# First FAILED:
# 0 → 1
# Second:
# 1 → 2
# Third:
# 2 → 3
# Finally:
# 3







# Day 6 Practice


# Q1 — Write File
# Ek list banao:
# usernames = ["vashu", "rahul", "govind", "vansh"]
# Aur users.txt mein har username ko separate line par save karo.


# usernames = ["vashu", "rahul", "govind", "vansh"] 

# with open("users.txt", "w") as file:
#     for user in usernames:
#         file.write(user + "\n")
        
# print("File Save Successfully!")

# with open("users.txt", "r") as file:
#     content = file.read()
# print(content)







# Q2 — Read File

# users.txt ko read karo aur har username ko separately print karo.
# Expected:
# vashu
# rahul
# govind
# vansh


# with open("users.txt", "r") as file:
#     content = file.read()
# print(content)





# Q3 — Day 5 + Day 6 

# Ek function banao:
# def save_usernames(usernames):
# Jo list receive kare aur usernames ko users.txt mein save kare.
# Example:
# users = ["vashu", "rahul", "govind"]
# save_usernames(users)


# def save_usernames(usernames):
#     with open("users.txt", "w") as file: 
#         for user in usernames:
#             file.write(user + "\n")

# user1=input("Enter your username: ")
# user2=input("Enter your username: ")

# usernames = [user1, user2]

# save_usernames(usernames)


# with open("users.txt", "r") as file: 
#     content = file.read()
# print(content)




# Q4 — Exception

# User se number lo aur:
# 100 / number
# calculate karo.
# Handle:
# invalid input
# zero division


# try :
#     num = int(input("Enter your Number: "))
#     print(100 / num)

# except ValueError:
#     print("Please Enter Numbers.")

# except ZeroDivisionError:
#     print("Can't Divide By Zero.")






# Q5 — Log Analysis 

# security.log file banao:

# LOGIN SUCCESS user=vashu
# LOGIN FAILED user=rahul
# LOGIN FAILED user=admin
# LOGIN SUCCESS user=govind
# LOGIN FAILED user=test
# LOGIN SUCCESS user=vansh
# Python se count karo:
# FAILED
# kitni baar aaya.
# Expected:
# Failed Attempts: 3




# log_data = "FAILED"
# with open("security.log", "w") as file:
#     file.write(log_data)

# failed_count = 0
# with open("security.log", "r") as file:
#     for line in file:
#         if "FAILED" in line:
#             failed_count += 1


# print(failed_count)





# Step 1: security.log file banao aur sample logs write karo
# log_data = """LOGIN SUCCESS user=vashu
# LOGIN FAILED user=rahul
# LOGIN FAILED user=admin
# LOGIN SUCCESS user=govind
# LOGIN FAILED user=test
# LOGIN SUCCESS user=vansh"""

# with open("security.log", "w") as file:
#     file.write(log_data)

# # Step 2 & 3: File read karo aur FAILED count karo
# failed_count = 0

# with open("security.log", "r") as file:
#     for line in file:
#         if "FAILED" in line:
#             failed_count += 1



# # Output print karo
# print(f"Failed Attempts: {failed_count}")







# Q6 — Advanced Revision

# Ek function banao:
# def count_failed_logins(filename):
# Function:

# File open kare
# Har line read kare
# "FAILED" search kare
# Count return kare
# Agar file missing ho toh error handle kare

# Use:
# result = count_failed_logins("security.log")
# print("Failed Attempts:", result)


# def count_failed_logins(filename):
#     failed_count = 0
    
#     try:
#         # File open karke read karo
#         with open(filename, "r") as file:
#             for line in file:
#                 if "FAILED" in line:
#                     failed_count += 1
#         return failed_count

#     except FileNotFoundError:
#         print(f"Error: File '{filename}' nahi mili!")
#         return 0

# # Function call
# result = count_failed_logins("security.log")
# print("Failed Attempts:", result)






# Day 6 ke end tak ye confidently aana chahiye:
# open()
#    ↓
# with open()
#    ↓
# read()
#    ↓
# write()
#    ↓
# for line in file
#    ↓
# strip()
#    ↓
# try
#    ↓
# except
#    ↓
# finally
#    ↓
# Log File Analysis 














