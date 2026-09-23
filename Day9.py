# Today's Goal

# Aaj ke end tak tum:

# Linux filesystem ka basic structure samjhoge
# /, /home, /etc samjhoge
# Absolute aur relative paths ka difference samjhoge
# pwd, ls, cd use kar paoge
# folders create kar paoge
# files create/copy/move/delete kar paoge






# 1. Linux Filesystem kya hai?

# Windows me tum drives dekhte ho:

# C:\
# D:\
# E:\

# Linux me filesystem generally ek single root se start hota hai:

# /

# Is / ko root directory kehte hain.

# Basic structure:

# /
# ├── home
# ├── etc
# ├── var
# ├── tmp
# ├── usr
# ├── bin
# └── root

# Abhi tumhe har directory yaad karne ki zarurat nahi hai. Aaj mainly:

# /
# ├── home
# └── etc

# samajhna important hai.




# 2. / — Root Directory
# /

# Linux filesystem ka starting point hai.

# Example:

# /
# ├── home
# ├── etc
# ├── var
# └── usr

# Ye Windows ke C:\ se conceptually compare kiya ja sakta hai, although Linux ka filesystem structure exactly Windows drives jaisa nahi hota.







# 3. /home

# Normal users ki personal directories usually /home ke andar hoti hain.

# Example:

# /home/vishwajeet

# Tum check kar sakte ho:

# pwd

# Aur:

# ls /home





# 4. /etc

# /etc me system-wide configuration files hoti hain.

# Example:

# ls /etc

# Bahut saari files/directories dikhengi.

# ⚠️ Abhi /etc ke files ko modify/delete mat karna.

# Cybersecurity me baad me configuration aur security-related files ko samajhne me /etc important hoga.






# 5. pwd

# Day 8 me tumne ye already dekha tha.

# pwd

# Meaning:

# Print Working Directory

# Ye batata hai ki tum currently filesystem me kahan ho.

# Example:

# /home/vishwajeet

# Socho:

# Tum currently kis folder me ho?
#         ↓
#        pwd






# 6. ls

# Current directory ke contents dekhne ke liye:

# ls

# Example:

# Documents
# Downloads
# projects
# linux-practice

# Detailed information ke liye:

# ls -l

# Hidden files dekhne ke liye:

# ls -a

# Dono combine:

# ls -la

# Abhi basic ls par focus karo.






# 7. cd

# cd ka meaning hai:

# Change Directory

# Example:

# cd projects

# Ab tum projects directory ke andar ho.

# Check:

# pwd
# Ek level back
# cd ..

# .. ka meaning hai parent directory.

# Example:

# /home/vishwajeet/projects
#                      ↑
#                   cd ..

# ke baad:

# /home/vishwajeet
# Home directory par jaana
# cd ~

# ~ generally current user's home directory ko represent karta hai.






# 8. Absolute vs Relative Path

# Ye bahut important cybersecurity concept hai.

# Absolute Path

# Complete path / se start hota hai.

# Example:

# /home/vishwajeet/projects/day9

# Isme complete location specified hai.

# Relative Path

# Current location ke according path.

# Suppose tum yahan ho:

# /home/vishwajeet

# Aur projects ke andar jaana hai:

# cd projects

# Ye relative path hai.

# Simple comparison:
# Absolute:
#  /home/vishwajeet/projects/day9

# Relative:
#  projects/day9




# 9. mkdir

# New directory/folder create karne ke liye:

# mkdir projects

# Example:

# mkdir day9



# 10. touch

# New empty file create karne ke liye:

# touch notes.txt

# Multiple files:

# touch notes.txt commands.txt

# Check:

# ls





# 11. cp

# File copy karne ke liye:

# cp notes.txt notes-copy.txt

# Meaning:

# notes.txt
#    ↓
# copy
#    ↓
# notes-copy.txt





# 12. mv

# mv ka use move aur rename dono ke liye hota hai.

# Rename:

# mv notes.txt linux-notes.txt

# Ab:

# notes.txt

# ki jagah:

# linux-notes.txt

# ho jayegi.







# 13. rm

# File delete karne ke liye:

# rm notes-copy.txt

# Check first:

# ls

# Then delete:

# rm notes-copy.txt




# ⚠️ Important

# Linux terminal me rm use karte waqt carefully filename check karo.

# rm filename

# ko casually run mat karo.

# Aaj folders delete karne ke liye rm -r practice mat karo. Pehle normal file deletion properly samjho.






# Day 9 Practice

# Ab actual practice karte hain.

# Step 1 — Home directory
# cd ~

# Check:

# pwd



# Step 2 — projects folder
# mkdir projects

# Enter:

# cd projects



# Step 3 — day9 folder
# mkdir day9
# cd day9

# Check:

# pwd

# Expected structure:

# /home/yourusername/projects/day9



# Step 4 — notes folder
# mkdir notes
# cd notes

# Now:

# pwd

# Tum notes directory ke andar hone chahiye.

# 📁 Current Structure

# Ab tumne create kiya:

# projects/
# └── day9/
#     └── notes/


# Step 5 — Two Files

# notes ke andar:

# touch linux.txt commands.txt

# Check:

# ls

# Output approximately:

# commands.txt
# linux.txt


#  Step 6 — Copy

# linux.txt ki copy banao:

# cp linux.txt linux-copy.txt

# Check:

# ls

# Now:

# commands.txt
# linux-copy.txt
# linux.txt


#  Step 7 — Rename

# Ab copied file ko rename karo:

# mv linux-copy.txt day9-notes.txt

# Check:

# ls

# Now:

# commands.txt
# day9-notes.txt
# linux.txt



#  Step 8 — Safely Delete

# Pehle check:

# ls

# Ab commands.txt delete karo:

# rm commands.txt

# Again:

# ls

# Final:

# day9-notes.txt
# linux.txt


#  Day 9 Main Task

# Ab ek separate folder create karo.

# Home directory me jao:

# cd ~

# Create:

# mkdir linux-practice

# Enter:

# cd linux-practice

# Ab 3 subfolders create karo:

# mkdir commands files security

# Check:

# ls

# Expected:

# commands
# files
# security

# Ab isi linux-practice directory ke andar 2 files create karo:

# touch linux-notes.txt commands.txt

# Check:

# ls

# Expected:

# commands
# commands.txt
# files
# linux-notes.txt
# security




# Important condition

# Tumhara complete task sirf terminal commands se hona chahiye.

#  File Explorer/File Manager use nahi karna.

#  Cybersecurity Connection

# Imagine tumhe kisi Linux machine par investigation karni hai.

# Tumhe manually folders click karke search karne ke bajay quickly karna hoga:

# pwd
# ls
# cd

# Phir files:

# cp
# mv
# rm

# Aur later:

# logs
#  ↓
# configuration
#  ↓
# processes
#  ↓
# network information
#  ↓
# suspicious files

# Isliye filesystem navigation cybersecurity ke practical work ka fundamental skill hai.




