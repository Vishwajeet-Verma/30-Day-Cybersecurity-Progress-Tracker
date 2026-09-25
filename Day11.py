# Today's Goal

# Aaj seekhoge:

# Linux users kya hote hain
# Groups kya hote hain
# r, w, x ka meaning
# ls -l se permissions read karna
# chmod se permissions change karna
# chown ka basic purpose
# File ko executable banana
# Kisi file ko sirf apne user ke liye readable/writable banana






# 1. Linux me Users

# Linux system me multiple users ho sakte hain.

# Example:

# vishwajeet
# rahul
# admin
# root

# Har user ka apna account aur permissions ho sakta hai.

# Current user check karne ke liye:

# whoami

# Tumhare case me abhi tumhare terminal prompt me:

# root@MCAL532

# dikh raha tha.

# Iska matlab tum currently root user ke roop me terminal chala rahe ho.

# Aaj ke practice ke liye ye important hai, kyunki root Linux ka highly privileged account hai.





# 2. Groups kya hote hain?

# Users ko groups me organize kiya ja sakta hai.

# Example:

# Developers
# Security
# Admins
# Students

# Suppose:

# vishwajeet ─┐
# rahul       ├── developers
# govind      ┘

# Agar kisi folder ko developers group ke liye access diya gaya hai, to group ke members ko woh permissions mil sakti hain.

# Current user ke groups dekhne ke liye:

# groups

# Try karo:

# whoami
# groups







# 3. Linux Permissions

# Linux me basic permissions 3 hoti hain:

# Symbol	Meaning
# r	        Read
# w     	Write
# x	        Execute


# Read r

# File ka content read kar sakte ho.

# Write w

# File ko modify/change kar sakte ho.

# Execute x

# File ko executable ke roop me run kar sakte ho.




# 4. Permission String

# Ab run karo:

# ls -l

# Example output:

# -rwxr-xr--

# Isko parts me samjho:

# -rwxr-xr--
#  ↑ ↑   ↑   ↑
#  │ │   │   └── Others
#  │ │   └────── Group
#  │ └────────── Owner
#  └──────────── File type

# Actually permission part:

# rwx r-x r--

# Teen groups:

# Owner    Group    Others
# rwx      r-x      r--



# 5. rwx ko samjho

# Suppose:

# rwx

# iska meaning:

# r = read
# w = write
# x = execute

# So:

# rwx

# means:

# Read + Write + Execute



# Example
# r-x

# means:

# r = yes
# w = no
# x = yes

# So:

# Read + Execute, but no Write.

# Example
# r--

# means:

# Read only.





# 6. Full Example

# Suppose:

# -rwxr-xr--

# Break it:

# Owner:  rwx
# Group:  r-x
# Others: r--

# Meaning:

# Owner
# rwx

# Read ✅
# Write ✅
# Execute ✅

# Group
# r-x

# Read ✅
# Write ❌
# Execute ✅

# Others
# r--

# Read ✅
# Write ❌
# Execute ❌



# 7. chmod

# chmod = change mode

# Iska use file/directory ki permissions change karne ke liye hota hai.

# Example:

# chmod 600 secret.txt

# Ye bahut important command hai.

# 8. Linux Permission Numbers

# Permissions ko numbers se bhi represent kar sakte hain.

# Permission	Number
# r	            4
# w	            2
# x         	1

# Add karne par:

# rwx = 4 + 2 + 1 = 7
# rw- = 4 + 2 = 6
# r-x = 4 + 1 = 5
# r-- = 4
# -w- = 2
# --x = 1
# --- = 0



# 9. chmod 600 ka Meaning
# chmod 600 secret.txt

# 600 ko teen parts me divide karo:

# 6 0 0
# │ │ │
# │ │ └── Others
# │ └──── Group
# └────── Owner

# 6 = rw-

# 0 = ---

# 0 = ---

# So:

# Owner    Group    Others
# rw-      ---      ---

# Meaning:

# Owner read + write kar sakta hai. Group aur others ke paas koi permission nahi.

# Exactly tumhare Day 11 main task ke liye required permission.




#  Practice 1 — Permission Check

# Pehle:

# cd ~/linux-practice

# Check:

# pwd

# Phir:

# ls -l

# Kisi file ki permission dekho.

# Example:

# -rw-r--r-- 1 root root 123 Sep 25 day10.txt

# Yahan:

# -rw-r--r--

# permissions hain.


#  Practice 2 — File Create Karo

# Create:

# touch test-permission.txt

# Check:

# ls -l test-permission.txt

# Tumhe kuch similar dikh sakta hai:

# -rw-r--r-- ...

# Distribution/configuration ke according default permissions vary kar sakti hain.



# Practice 3 — Only Owner Access

# Ab:

# chmod 600 test-permission.txt

# Check:

# ls -l test-permission.txt

# Expected permission portion:

# -rw-------

# Break:

# Owner    Group    Others
# rw-      ---      ---

# So:

# Owner  → Read + Write
# Group  → No access
# Others → No access






#  Day 11 Main Task

# Ab ek dedicated file create karo:

# touch private-notes.txt

# Permissions check:

# ls -l private-notes.txt

# Ab permission set karo:

# chmod 600 private-notes.txt

# Again check:

# ls -l private-notes.txt

# Expected:

# -rw------- ...
# Verify

# Permission section:

# rw-------

# ka meaning:

# Owner  → rw- ✅
# Group  → --- ❌
# Others → --- ❌

# Task complete. ✅



# 10. chown — Ownership Change

# chown ka meaning:

# change owner

# Example:

# chown username filename

# Ye file ka owner change kar sakta hai.

# Check ownership:

# ls -l

# Example:

# -rw------- 1 root root 0 private-notes.txt

# Yahan:

# root root

# generally owner aur group ko represent karte hain.



#  Abhi chown ko sirf conceptually samjho

# Tumhare current WSL setup me tum root user ke roop me ho, isliye ownership commands ke saath experiment karna abhi zaroori nahi hai.



# Bonus — Executable File

# Ab ek script create karo:

# touch hello.sh

# Content add karo:

# echo '#!/bin/bash' > hello.sh
# echo 'echo "Hello from Linux"' >> hello.sh

# Check:

# cat hello.sh

# Initially execute permission nahi bhi ho sakti.

# Check:

# ls -l hello.sh

# Executable permission add karo:

# chmod +x hello.sh

# Check:

# ls -l hello.sh

# Ab permission string me x appear hona chahiye.

# Run:

# ./hello.sh

# Expected:

# Hello from Linux





#  Cybersecurity Connection

# Permissions security ke liye extremely important hain.

# Imagine:

# secret.txt

# me sensitive information hai.

# Agar:

# -rw-r--r--

# hai, to others bhi file read kar sakte hain.

# Agar:

# -rw-------

# hai:

# Owner → Read + Write
# Others → No access

# Isliye incorrectly configured permissions security problem create kar sakti hain.

# Concept:

# Sensitive File
#      ↓
# Permissions
#      ↓
# Who can Read?
# Who can Write?
# Who can Execute?



#  Day 11 Revision Questions

# Pehle khud answer karo:

# Q1. Linux user kya hota hai?

# Q2. Linux group kya hota hai?

# Q3. r, w, x ka meaning kya hai?

# Q4. ls -l kya information provide karta hai?

# Q5. rwxr-xr-- ko Owner, Group aur Others me divide karo.

# Q6. chmod kis kaam aata hai?

# Q7. chmod 600 file.txt ka exact meaning kya hai?

# Q8. chmod +x script.sh kya karta hai?

# Q9. chown kis kaam aata hai?

# Q10. File permissions cybersecurity ke liye important kyun hain?



#  Mini Challenge

# Bina upar dekhe ye task complete karne ki try karo:

# Create:

# cyber-secret.txt

# Then make it:

# Owner    → Read + Write
# Group    → No access
# Others   → No access

# Finally:

# ls -l cyber-secret.txt

# Expected permission:

# -rw-------