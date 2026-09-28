# Day 14 — Linux Mini-Project + Weekly Revision

# Aaj Week 2 ka final day hai. Aaj hum Day 8–13 me jo Linux commands seekhe hain unko combine karke ek real Linux System Information Script banayenge.

# Hum Bash ki jagah Python use karenge, kyunki tum Python already Week 1 me kar chuke ho. Isme subprocess ka light introduction hoga.



#  Today's Goal

# Ek Python script banana jo automatically ye 6 information print kare:

# Hostname
# Current user
# IP information
# Disk usage
# Memory information
# Running processes

# Final output kuch is type ka hoga:

# ========================================
#      LINUX SYSTEM INFORMATION
# ========================================

# [1] HOSTNAME
# MCAL532

# [2] CURRENT USER
# vishwajeet

# [3] IP INFORMATION
# ...

# [4] DISK USAGE
# ...

# [5] MEMORY INFORMATION
# ...

# [6] TOP RUNNING PROCESSES
# ...

# ========================================


# Step 1 — subprocess Kya Hai?

# Python normally Linux commands ko directly nahi samajhta.

# For example Linux terminal me:

# whoami

# lekin Python ke andar hum Linux command ko execute karne ke liye:

# import subprocess

# use kar sakte hain.

# Example:

# import subprocess

# result = subprocess.run(["whoami"], capture_output=True, text=True)

# print(result.stdout)

# Yahan:

# subprocess.run()

# → Linux command execute karta hai.

# capture_output=True

# → command ka output Python ke paas capture karta hai.

# text=True

# → output ko readable string banata hai.

# result.stdout

# → command ka actual output.




#  Step 2 — Project Folder

# Apne Linux terminal me:

# cd /home/vishwajeet/linux-practice

# Check:

# pwd

# Expected:

# /home/vishwajeet/linux-practice

# Ab project file banao:

# touch system_info.py

# Check:

# ls -l

# Tumhe:

# system_info.py

# dikhna chahiye.





#  Step 3 — Complete Mini Project

# system_info.py ko edit karo:

# nano system_info.py

# Aur ye code paste karo:

# import subprocess


# def run_command(command):
#     result = subprocess.run(
#         command,
#         capture_output=True,
#         text=True
#     )
#     return result.stdout.strip()


# print("=" * 50)
# print("       LINUX SYSTEM INFORMATION")
# print("=" * 50)


# # 1. Hostname
# print("\n[1] HOSTNAME")
# print(run_command(["hostname"]))


# # 2. Current User
# print("\n[2] CURRENT USER")
# print(run_command(["whoami"]))


# # 3. IP Information
# print("\n[3] IP INFORMATION")
# print(run_command(["ip", "a"])) 


# # 4. Disk Usage
# print("\n[4] DISK USAGE")
# print(run_command(["df", "-h"]))


# # 5. Memory Information
# print("\n[5] MEMORY INFORMATION")
# print(run_command(["free", "-h"]))


# # 6. Running Processes
# print("\n[6] TOP RUNNING PROCESSES")
# processes = run_command(["ps", "aux"])
# print("\n".join(processes.splitlines()[:6]))


# print("\n" + "=" * 50)
# print("          INFORMATION COMPLETE")
# print("=" * 50)

# Save:

# Ctrl + O
# Enter
# Ctrl + X



# ▶Step 4 — Run Your Script

# Run:

# python3 system_info.py

# Agar Python properly installed hai, tumhe actual machine information milegi.

# Code Ko Samjho
# Function
# def run_command(command):

# Humne ek function banaya jo Linux command execute karega.

# Isliye baar-baar ye code likhne ki zarurat nahi:

# subprocess.run(...)
# Hostname
# run_command(["hostname"])

# Ye internally:

# hostname

# run karega.

# Current User
# run_command(["whoami"])

# Equivalent:

# whoami
# IP
# run_command(["ip", "a"])

# Equivalent:

# ip a

# Notice:

# ["ip", "a"]

# instead of:

# ["ip a"]
# Disk
# run_command(["df", "-h"])

# Equivalent:

# df -h

# -h = human-readable format.

# Memory
# run_command(["free", "-h"])

# Equivalent:

# free -h
# Processes
# processes = run_command(["ps", "aux"])

# Equivalent:

# ps aux

# Then:

# processes.splitlines()[:6]

# ka matlab hai output ki first 6 lines lena.

# Isme normally header + 5 processes aa jayenge.




#  Step 5 — Test

# Ab ye commands run karo:

# python3 system_info.py

# Phir:

# python3 system_info.py > system_info_output.txt

# Ab:

# ls -lh

# Aur:

# head -30 system_info_output.txt

# Isse tumhare script ka output file me bhi save ho jayega.




#  Cybersecurity Connection

# Ye simple script actually ek important cybersecurity concept demonstrate karta hai:

# Know your system before you secure your system.

# For example, security investigation me useful information ho sakti hai:

# Hostname
#    ↓
# Which machine?

# Current user
#    ↓
# Who is logged in?

# IP information
#    ↓
# What network interfaces exist?

# Disk
#    ↓
# Is storage almost full?

# Memory
#    ↓
# How much RAM is being used?

# Processes
#    ↓
# What is currently running?

# Ye authorized system administration/security assessment me basic information gathering ka foundation hai.




#  Practical Challenge

# Ab project ko thoda cybersecurity-oriented banate hain.

# Hume detect karna hai:

# 1. Disk usage > 80%
# 2. Ek selected process running hai ya nahi

# For example testing ke liye hum sleep choose kar sakte hain.

# Terminal me pehle:

# sleep 120 &

# Phir:

# ps aux | grep sleep

# Agar sleep running hai to script usko detect kar sakti hai.





# Challenge Code

# Apne existing script ke end me ye add karo:

# print("\n[7] SECURITY CHECKS")

# # Check disk usage
# disk_usage = run_command(["df", "-h", "/"])
# print("\nDisk Usage:")
# print(disk_usage)

# # Check for unexpected process
# process_list = run_command(["ps", "aux"])

# if "sleep" in process_list:
#     print("\nWARNING: 'sleep' process is running!")
# else:
#     print("\nNo 'sleep' process detected.")


# Important

# Ye abhi basic detection hai. Production security tool nahi hai.

# "sleep" in process_list simple text matching karta hai, isliye false positives possible hain.

# Aaj ka purpose integration + understanding hai.




#  Day 14 Notes

# Ab notes file banao:

# touch day14-mini-project.txt

# Edit:

# nano day14-mini-project.txt

# Ye likh sakte ho:

# DAY 14 — Linux Mini Project

# Project:
# Linux System Information Script

# Language:
# Python

# Purpose:
# To collect basic information about a Linux system.

# Information collected:
# 1. Hostname
# 2. Current user
# 3. IP information
# 4. Disk usage
# 5. Memory information
# 6. Running processes

# Commands used:
# hostname
# whoami
# ip a
# df -h
# free -h
# ps aux

# Python module:
# subprocess

# What I learned:
# - How to execute Linux commands from Python
# - How to capture command output
# - How Linux system information can be collected automatically
# - Basic system information gathering

# Cybersecurity connection:
# System information gathering is useful for authorized
# system administration and security assessment.

# Mini project status:
# Completed / Tested





#  Week 2 Quick Test

# Ab bina notes dekhe answer try karo.

# Q1

# Absolute path aur relative path me difference?

# Q2

# chmod 700 ka roughly kya meaning hai?

# Q3

# File ke andar FAILED search karne ke liye command?

# Q4

# ps aur top me difference?

# Q5

# ping kya tell karta hai?

# Q6

# Security testing me curl useful kyun ho sakta hai?

# Q7

# Overly permissive file permissions ka ek risk?



#  Week 2 — Tumne Kya Seekha

# DAY 8
# Linux Basics
# ↓
# DAY 9
# Filesystem & Navigation
# ↓
# DAY 10
# Files & Searching
# ↓
# DAY 11
# Users, Groups & Permissions
# ↓
# DAY 12
# Processes & Monitoring
# ↓
# DAY 13
# Networking Commands
# ↓
# DAY 14
# Mini Project



# Tumhari main commands:

# whoami
# pwd
# ls
# cd
# mkdir
# touch
# cp
# mv
# rm

# cat
# less
# head
# tail
# grep

# chmod
# chown

# ps
# top
# kill

# ip
# ping
# ss
# curl
# dig

# Aur ab:

# Python
#    +
# Linux commands
#    ↓
# System Information Script


#  Final Day 14 Folder

# Check karo:

# ls -lah

# Ideally tumhare folder me ye important files honi chahiye:

# linux-practice/
# │
# ├── day10.txt
# ├── security.log
# ├── day13-networking.txt
# ├── webpage.html
# ├── system_info.py
# ├── system_info_output.txt
# └── day14-mini-project.txt




#  Day 14 Completion Checklist

# ☐ Week 2 notes revise kiye
# ☐ system_info.py banaya
# ☐ Script successfully run hua
# ☐ Hostname print hua
# ☐ Current user print hua
# ☐ IP information print hui
# ☐ Disk usage print hua
# ☐ Memory information print hui
# ☐ Processes print hue
# ☐ Security challenge try kiya
# ☐ Notes complete kiye
# ☐ GitHub par push kiya


#  Move Forward If

# Tum ye 3 cheezein independently kar pao:

# cd /home/vishwajeet/linux-practice
# python3 system_info.py

# aur explain kar sako ki script ke andar:

# subprocess.run(...)

# kyun use hua.