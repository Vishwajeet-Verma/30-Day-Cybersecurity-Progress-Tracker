# Day 10 — Reading & Manipulating Files

# Welcome to Day 10.
# Day 9 me files/folders create, move, copy aur delete karna seekha.

# Aaj hum next step karenge:

# Terminal ke andar file ke content ko read aur search karna.

# Ye cybersecurity ke liye particularly important hai because real systems me logs ko manually open karne ke bajay terminal commands se quickly search kiya jata hai.






# Today's Goal

# Aaj ke end tak tum confidently use kar paoge:

# cat
# less
# head
# tail
# grep

# Aur specifically:

# File
#  ↓
# Read
#  ↓
# Search
#  ↓
# Filter
#  ↓
# Important information identify




# 1. cat — File ka Content Dekhna

# Sabse basic command:

# cat filename.txt

# Example:

# cat linux-notes.txt

# Agar file me:

# Linux is an operating system.
# Ubuntu is a Linux distribution.
# Terminal is important.
# Linux is used on servers.

# hai, to cat poora content terminal me display karega.

# Simple meaning
# cat = complete file content display







# 2. less — Large File Read Karna

# Agar file bahut badi ho, cat inconvenient ho sakta hai.

# Use:

# less filename.txt

# Example:

# less linux-notes.txt

# Ab tum file ko terminal ke andar scroll karke read kar sakte ho.

# Important keys

# Inside less:

# ↓ / ↑     Move
# Space     Next page
# b         Previous page
# q         Quit

# Sabse important:

# q

# press karke less se bahar aa jao.

# Difference
# cat  → entire file ek saath display
# less → file ko page-by-page read








# 3. head — Starting Lines

# File ki beginning ki lines dekhne ke liye:

# head filename.txt

# Default generally first 10 lines show karta hai.

# Lekin hume exactly 5 lines chahiye:

# head -5 filename.txt

# Meaning:

# head -5
#    ↓
# first 5 lines



# 4. tail — Last Lines

# File ke end ki lines dekhne ke liye:

# tail filename.txt

# First 10 lines ki tarah, default generally last 10 lines show karta hai.

# Exactly last 5:

# tail -5 filename.txt

# Meaning:

# tail -5
#    ↓
# last 5 lines






# 5. grep — Search 

# Ab aaj ka most important command:

# grep

# grep ka use file ke andar specific text/pattern search karne ke liye hota hai.

# Example:

# grep "Linux" linux-notes.txt

# Ye sirf woh lines display karega jisme Linux match hota hai.

# Example

# Suppose:

# Linux is open source.
# Windows is also an operating system.
# Linux is common on servers.
# Ubuntu is based on Linux.
# Python is useful for cybersecurity.

# Command:

# grep "Linux" notes.txt

# Output:

# Linux is open source.
# Linux is common on servers.
# Ubuntu is based on Linux.

# Notice:

# grep ne poori file nahi dikhayi.

# Sirf matching lines dikhayi.




# Practice 1 — 20-Line File

# Ab khud ek file create karo:

# cd ~/linux-practice

# Check:

# pwd

# Ab file:

# touch day10.txt

# Ab hum usme 20 lines add karenge.

# Beginner-friendly way:

# echo "Line 1 - Linux" > day10.txt
# echo "Line 2 - Ubuntu" >> day10.txt
# echo "Line 3 - Terminal" >> day10.txt
# echo "Line 4 - Cybersecurity" >> day10.txt
# echo "Line 5 - Networking" >> day10.txt
# echo "Line 6 - Linux" >> day10.txt
# echo "Line 7 - Python" >> day10.txt
# echo "Line 8 - Security" >> day10.txt
# echo "Line 9 - Linux" >> day10.txt
# echo "Line 10 - Server" >> day10.txt
# echo "Line 11 - Ubuntu" >> day10.txt
# echo "Line 12 - Logs" >> day10.txt
# echo "Line 13 - Linux" >> day10.txt
# echo "Line 14 - Terminal" >> day10.txt
# echo "Line 15 - Firewall" >> day10.txt
# echo "Line 16 - Linux" >> day10.txt
# echo "Line 17 - Network" >> day10.txt
# echo "Line 18 - Security" >> day10.txt
# echo "Line 19 - Ubuntu" >> day10.txt
# echo "Line 20 - Linux" >> day10.txt
# Important

# First line:

# >

# file create/overwrite karta hai.

# Remaining:

# >>

# existing file ke end me content append karta hai.





# 6. File Check Karo
# cat day10.txt

# Tumhe 20 lines dikhni chahiye.




# 7. less Practice
# less day10.txt

# Scroll karo.

# Phir:

# q

# press karo.





# 8. head -5
# head -5 day10.txt

# Sirf:

# Line 1
# Line 2
# Line 3
# Line 4
# Line 5

# wali lines aayengi.






# 9. tail -5
# tail -5 day10.txt

# Sirf last 5 lines.







#  10. grep Practice

# Ab search karo:

# grep "Linux" day10.txt

# Sirf Linux wali lines display hongi.

# Try:

# grep "Ubuntu" day10.txt

# Aur:

# grep "Security" day10.txt







#  Important Cybersecurity Concept

# Suppose kisi server ka log file hai:

# User admin logged in
# User vashu logged in
# Failed login from 192.168.1.50
# User admin logged in
# Failed login from 10.0.0.25
# Connection established

# Security analyst ko sirf failed logins dekhne hain.

# Instead of manually reading everything:

# grep "Failed" server.log

# Output:

# Failed login from 192.168.1.50
# Failed login from 10.0.0.25

# Yahi reason hai ki grep cybersecurity me extremely useful command hai.






#  Day 10 Main Task — Fake Security Log

# Ab actual cybersecurity-style task karte hain.

# Home practice directory me:

# cd ~/linux-practice

# Create:

# touch security.log

# Ab 15-line fake log create karo:

# echo "INFO User Vishwajeet logged in" > security.log
# echo "INFO Server started successfully" >> security.log
# echo "ERROR Failed login attempt from 192.168.1.10" >> security.log
# echo "INFO User admin logged in" >> security.log
# echo "WARNING High memory usage detected" >> security.log
# echo "ERROR Database connection failed" >> security.log
# echo "INFO Backup completed" >> security.log
# echo "INFO User Rahul logged in" >> security.log
# echo "ERROR Permission denied for user guest" >> security.log
# echo "INFO Network connection established" >> security.log
# echo "WARNING Disk usage is high" >> security.log
# echo "ERROR Failed authentication attempt" >> security.log
# echo "INFO Security scan completed" >> security.log
# echo "ERROR File access failed" >> security.log
# echo "INFO System running normally" >> security.log




#  Sirf ERROR Lines Display Karo

# Run:

# grep "ERROR" security.log

# Output me sirf ERROR wali lines aani chahiye.

#  ERROR Count Karo




# Ab task ka second part:

# grep -c "ERROR" security.log

# -c ka meaning:

# matching lines ki count do.

# Tumhare current log me:

# ERROR = 5

# hona chahiye.

# So output:

# 5





#  Very Important Difference
# grep "ERROR" security.log

# → ERROR wali lines

# grep -c "ERROR" security.log

# → ERROR wali lines ki count




#  Bonus Practice

# Ab try karo:

# WARNING lines

# grep "WARNING" security.log

# INFO lines
# grep "INFO" security.log

# Specific IP
# grep "192.168.1.10" security.log

# Case-insensitive search

# Try:

# grep -i "error" security.log

# -i uppercase/lowercase difference ignore karta hai.

# For example:

# ERROR
# error
# Error

# sab match ho sakte hain.




# Real Cybersecurity Connection

# Imagine ek server par thousands of log lines hain:

# server.log
#     ↓
# 100 lines
#     ↓
# 1,000 lines
#     ↓
# 100,000 lines

# Manually read karna inefficient hai.

# Security analyst commands use kar sakta hai:

# grep "ERROR" server.log

# Ya:

# grep "Failed" server.log

# Ya:

# grep "192.168.1.50" server.log

# Concept:

# Huge Log
#    ↓
# grep
#    ↓
# Matching Lines
#    ↓
# Investigate

# Ye basic skill later log analysis, incident response aur Blue Team work me useful hogi.




#  Day 10 Quick Revision

# Khud answer karo:

# Q1. cat ka purpose kya hai?

# Q2. less aur cat me basic difference kya hai?

# Q3. head -5 kya karta hai?

# Q4. tail -5 kya karta hai?

# Q5. grep ka primary purpose kya hai?

# Q6. grep "ERROR" security.log kya output karega?

# Q7. grep -c "ERROR" security.log kya output karega?

# Q8. grep -i me -i kya karta hai?

# Q9. Cybersecurity me logs ke saath grep useful kyun hai?

# Q10. > aur >> me kya difference hai?




#  Mini Challenge

# Without looking above, try to solve:

# Situation:

# security.log me hundreds of lines hain.

# Tumhe:

# Sirf ERROR lines dekhni hain.
# Total ERROR lines count karni hain.
# 192.168.1.10 IP wali lines find karni hain.

# Commands khud likho.

# <details> <summary>Answer check karne ke baad dekho</summary>
# grep "ERROR" security.log
# grep -c "ERROR" security.log
# grep "192.168.1.10" security.log
# </details>



# Day 10 ka key takeaway:
# cat = read, less = browse, head = beginning, tail = ending, grep = search/filter.