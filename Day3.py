# DAY 3
#  Today's Goal

# Aaj ke end tak ye aana chahiye:

# for loop
# range()
# while loop
# break
# continue
# for vs while
# Loops ko cybersecurity examples se connect karna


# 1 — for Loop

# for loop ka use tab hota hai jab hume kisi sequence/range ke items par repeatedly kaam karna ho.


# for i in range(1, 6):           #range(start, stop)
#     print(i)



# 2 — range()

# for i in range(1, 11, 1):           # range(start, stop, step)
#     print(i)


# for i in range(1, 11, 2):         # step me 2 hai iska mtlb 1,2,3,.. nahi 1, 3, 5 , ..... hai.
#     print(i)




# 3 — while Loop

# while loop tab tak execute hota hai jab tak condition True hoti hai.

# Important

# while me condition ko eventually False banana zaroori hai, warna infinite loop ho sakta hai.

# i = 1
# while i <= 5:
#     print(i)
#     i += 1          # i = i + 1






# 4 — for vs while

# for = Kitni baar karna hai, generally pata hai.
# while = Kab tak karna hai, condition decide karti hai.

# Simple difference yaad rakho:

# for

# Jab repetitions/sequence ka idea known ho:

# for i in range(1, 11):
#     print(i)

# "10 times kaam karo."

# while

# Jab condition ke basis par loop continue karna ho:


# while password != "python123":
#     ...

# "Jab tak password correct nahi hota, poochte raho."


# password = ""
# while password != "python123":
#     password = input("Enter Password: ")
# print("Login Successfull")





# 5 — break

# break loop ko immediately stop kar deta hai.


# for i in range(1, 11):
#     if i == 5:
#         break         # here  loop will be stop
#     print(i)




# 6 — continue

# continue current iteration ko skip karta hai aur next iteration par chala jata hai

# for i in range(1, 11):
#     if i == 8:
#         continue            # here 8 will not be print
#     print(i)


# break    → poora loop stop
# continue → current iteration skip





# Practice 

# Q1 — Basic for

# for loop ka use karke:

# 1 2 3 4 5 6 7 8 9 10
# print karo.


# for i in range(1, 11):
#     print(i)



# Q2 — range() with Step

# range() ka use karke 2 se 20 tak even numbers print karo.

# Expected:

# 2 4 6 8 10 12 14 16 18 20


# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)



# Q3 — while

# while loop ka use karke:

# 10 9 8 7 6 5 4 3 2 1
# print karo.

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1


# Q4 — break

# 1 se 10 tak loop chalao, lekin 5 aate hi loop stop kar do.

# Expected: 1 2 3 4


# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)





# Q5 — continue

# 1 se 20 tak numbers print karo, lekin multiples of 3 skip karo.

# Expected: 1 2 4 5 7 8 10 ...



# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)




# Q6 — Password while Loop

# User se password repeatedly input lo. Correct password: python123

# Jab tak password incorrect hai: Wrong password 
# Correct hone par: Login successful
# Hint
# Is question me while particularly important hai.


# password = ""
# while password != "python123":
#     password = input("Enter Password: ")

#     if password == "python123":
#         print("Login Succesfully")
#     else:
#         print("Wrong Password")



# password = ""
# while password != "python123":
#     password = input("Enter Passowrd: ")
# print("Login Successfully")





# Q7 — Vowel Counter

# User se ek string lo: Enter text: cybersecurity

# for loop ka use karke count karo ki string me kitne vowels hain.

# Vowels: a e i o u

# Example:

# cybersecurity

# me vowels count karne hain.

# Hint

# Tum if + for combine karoge.




# string = input("Enter Text: ")

# count = 0

# for i in string:
#     if i in "aeiou":
#         count += 1

# print(f"Total Vowels = {count}")



# vowels = input("Enter Text: ")

# count = 0

# for i in vowels:
#     if i in "aeiou":
#         count += 1

# print(f"Total Vowels = {count}")






# Main Task — Login Simulator

# Ab roadmap ka main task.

# Tumhe ek login system banana hai jo user ko maximum 3 attempts de.

# Example:

# Enter password: hello
# Wrong password
# Attempts remaining: 2

# Enter password: test
# Wrong password
# Attempts remaining: 1

# Enter password: python123
# Login successful

# Agar 3 attempts fail:

# Account locked. Too many failed attempts.
# Required Concepts

# Is project me tumhe use karna hai:

# while
# if
# break

# Aur preferably:

# attempt counter


# password = ""
# count = 0

# while password != "python123":
    
#     password = input("Enter Password: ")
    
#     count += 1

#     if password == "python123":
#         print("Login Successful")
#         break

#     else:
#         print("Wrong Password")
    
#     if count >= 3:
#         print("Account Locked. Too many failed attempts.")
#         break






# Day 3 Complete 
# Lets Move on Fourth Day of Python Coding =>
# Thankyou !



















