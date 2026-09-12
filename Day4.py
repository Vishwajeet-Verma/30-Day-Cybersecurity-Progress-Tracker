# Day 4 Started — Python Data Structures

# Aaj ka topic bahut important hai, kyunki Python me real projects aur cybersecurity scripts me data ko store/manage karne ke liye ye 4 structures bahut use hote hain:

# List → []
# Tuple → ()
# Set → {} / set()
# Dictionary → {key: value}




# List
# What is a List?
# List ek collection hai jisme hum multiple values store kar sakte hain.
# usernames = ["vashu", "rahul", "aman", "rohit"]
# Is list me 4 usernames hain.
# Important properties
# Ordered → jis order me items add kiye, wahi order maintain hota hai.
# Mutable → list banane ke baad uske items ko change/add/remove kar sakte ho.





# Tuple
# Tuple bhi multiple values store karta hai:
# colors = ("red", "green", "blue")
# Lekin tuple immutable hota hai.
# Matlab create karne ke baad normally uske elements ko change nahi kar sakte.
# colors = ("red", "green", "blue")
# print(colors[0])





# Set
# Set ka main feature hai:
# Unique values
# Example:
# numbers = {1, 2, 2, 3, 3, 4}
# print(numbers)
# Output approximately:
# {1, 2, 3, 4}





# Dictionary
# Ye aaj ka sabse important structure hai.
# Dictionary data ko key-value pair me store karta hai.
# user = {
#     "username": "vashu",
#     "password": "python123",
#     "age": 18
# }






# Easy trick:
# LIST       → Collection
# TUPLE      → Fixed Collection
# SET        → Unique Collection
# DICTIONARY → Key → Value






# Day 4 Practice

# Q — List
# 5 usernames ki list banao:

# Ek naya username add karo.
# Ek existing username remove karo.
# Final list print karo.

# username = ["vashu", "rahul", "govind", "vansh", "vedant"]
# print(username)
# username.append("Krishna")
# print(username)
# username.remove("vedant")
# print(username)
# username.insert(2, "Anirudh")
# print(username)



# Tuple

# username = ("Vashu", "Rahul", "Krishna", "Shubham")
# print(username)




# Set

# username = {0, 1, 2, 3, 3, 3, 2 , 5 ,3 ,4 ,5 , 6,6 ,4 }
# print(username)



# Dictionary 

# username = {"Vashu": "python123",
#             "rahul": "python1234",
#             "krishna": "python234",
#             "Shubham": "python456"}

# print(username)




# LEVEL 1 — Day 4 Basic Revision
# Q1 — List
# 5 usernames ki list banao aur:

# ek username add karo
# ek remove karo
# ek specific index par username insert karo
# final list print karo

# usernames = ["Vashu", "Rahul", "Krishna", "Shubham", "Vishwajeet"]
# print(usernames)
# usernames.append("VCSE")
# print(usernames)
# usernames.remove("Vishwajeet")
# print(usernames)
# usernames.insert(1, "Vishwajeet")
# print(usernames)



# Q2 — List Indexing
# users = ["vashu", "rahul", "aman", "rohit", "krishna"]

# Print:
# first username
# third username
# last username

# users = ["Vashu", "rahul", "aman", "rohit", "krishna"]
# print(users[1], users[3], users[-1])




# Q3 — List Update
# users = ["vashu", "rahul", "aman"]
# rahul ko "anirudh" se replace karo.


# users = ["vashu", "rahul", "aman"]
# print(users)
# users.remove("rahul")
# print(users)
# users.insert(1, "anirudh")
# print(users)


# best way to solve
# if index value malum ho toh

# users = ["vashu", "rahul", "aman"]
# print(users)
# users[1] = "anirudh"
# print(users)



# if index value malum nahi ho toh

# users = [ "vashu", "rahul", "aman"]
# print(users)

# index = users.index("rahul")
# users[index] = "anirudh"

# print(users)




# in a single line
# users = ["vashu", "rahul", "aman"]
# print(users)

# users[users.index("rahul")] = "anirudh"
# print(users)




# Q4 — Tuple

# 5 programming languages ka tuple banao:
# Python, Java, C, JavaScript, PHP
# First aur last language print karo.


# languages = ("python", "java", "c", "javascript", "PHP")
# print(languages[0], languages[-1])



# Q5 — Set
# numbers = [10, 20, 10, 30, 20, 40, 30]
# Isko set me convert karke duplicates remove karo.


# numbers = [10, 20, 10, 30, 20, 40, 30]

# sets = set(numbers)             # yaha prr set(number) se list ki value set me convert ho gyi hai
# print(sets)


# in_list = list(sets)            # abb yaha pr list(sets) se set ki value list me convert ho gyi hai
# print(in_list)










