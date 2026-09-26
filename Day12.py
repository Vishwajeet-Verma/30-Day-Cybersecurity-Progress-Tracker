# Day 12 — Processes & System Monitoring

# Great! Day 11 me Linux permissions complete kiya. 

# Aaj hum Linux ke running programs/processes ko samjhenge.

#  Main question: "Mere Linux system me abhi kya-kya chal raha hai?"

# Cybersecurity me kisi machine ki investigation start karte waqt running processes dekhna ek basic observation step hota hai.

# 1. Process kya hota hai?

# Jab tum koi program run karte ho, Linux us program ko ek process ke roop me manage karta hai.

# Example:

# Tum:
#     ./hello.sh
#          ↓
# Linux
#          ↓
# Process
#          ↓
# CPU + RAM use

# Examples of processes:

# bash
# system services
# Python
# SSH
# Chrome-related processes
# background services

# Har process ka generally ek PID hota hai.

# PID kya hai?

# PID = Process ID

# Example:

# PID
# 1234

# Ye process ki identification number hoti hai.

# 2. ps — Running Processes

# Basic command:

# ps

# Try:

# ps

# Ye current terminal/session se related processes ka snapshot dikhata hai.

# Lekin hume system ke zyada processes dekhne hain.

# 3. ps aux

# Aaj ka most important command:

# ps aux

# Ye running processes ki detailed list provide karta hai.

# Output kuch is type ka ho sakta hai:

# USER       PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
# root         1   0.0  0.1  ...    ... ?        ...  ...     ... /sbin/init
# root       100   0.0  0.2  ...    ... ?        ...  ...     ... ...
# vishwajeet 500   0.0  0.1  ...    ... pts/0    ...  ...     ... bash

# Tumhare system par output different hoga. That's completely normal.





# 4. ps aux ke Columns

# Important columns:

# USER
# PID
# %CPU
# %MEM
# COMMAND
# USER

# Process kis user ke under chal raha hai.

# PID

# Process ID.

# Example:

# 1234
# %CPU

# Process kitna CPU use kar raha hai.

# %MEM

# Process kitni memory/RAM use kar raha hai.

# COMMAND

# Kaunsa program/process run ho raha hai.



# Practice 1 — 3 Processes Identify Karo

# Run:

# ps aux

# Ab list me se 3 processes choose karo.

# Notes me:

# Process 1:
# Name:
# PID:
# What I think it does:

# Process 2:
# Name:
# PID:
# What I think it does:

# Process 3:
# Name:
# PID:
# What I think it does:

# Agar kisi process ka purpose nahi pata:

# I am not sure yet.

# likh sakte ho.

# Guess karna allowed hai — goal observation hai.





# 5. top

# Ab live system monitoring:

# top

# Tumhe continuously changing screen milegi.

# Example:

# top - ...
# Tasks: ...
# %Cpu...
# MiB Mem...

# Neeche processes ki list bhi hoti hai.

# Important information:

# CPU usage
# Memory usage
# PID
# Process
# top se bahar kaise nikle?

# Simply:

# q

# press karo.

#  Ctrl+C ki zarurat nahi.



#  ps vs top

# Important difference:

# ps aux
#    ↓
# Snapshot

# while:

# top
#    ↓
# Live/continuously updating monitoring

# Simple:

# Command	Purpose
# ps aux	Running processes ka snapshot
# top	Live process monitoring




# 6. Background Process

# Normally jab tum command run karte ho:

# sleep 60

# terminal wait karega jab tak command complete nahi hoti.

# Lekin:

# sleep 60 &

# me & ka meaning hai:

# Process ko background me run karo.

# Try:

# sleep 60 &

# Tumhe kuch similar output mil sakta hai:

# [1] 12345

# Yahan:

# [1]     → job number
# 12345   → PID

# Tumhare system par PID different hoga.




# 7. Background Process Check Karo

# Ab:

# ps

# run karo.

# Ya:

# ps aux | grep sleep

# Yahan | ko pipe kehte hain.

# Abhi pipe ko deeply learn karna zaroori nahi hai; bas observe karo.



# 8. Process Kill Karna

# Agar sleep ka PID maan lo:

# 12345

# to:

# kill 12345

# Run:

# kill 12345

# Apne actual PID ko use karna. 12345 ko blindly copy mat karna.

# Check:

# ps aux | grep sleep

# Agar process terminate ho gaya hai, actual sleep 60 process nahi milna chahiye.




# kill ka Important Concept

# kill ka naam thoda dangerous lag sakta hai, but iska basic purpose hai:

# Process ko signal bhejna.

# Normal:

# kill PID

# usually process ko gracefully terminate karne ka request bhejta hai.

# Forceful option:

# kill -9 PID

# bhi hota hai, lekin aaj iski practice mat karo.

# Abhi:

# kill PID

# hi use karo.




#  Day 12 Practice — Complete Flow

# Ab ye complete sequence khud run karo:

# Step 1
# ps aux

# 5 processes observe karo.

# Step 2
# top

# CPU/memory observe karo.

# Exit:

# q
# Step 3

# Background process:

# sleep 60 &
# Step 4

# Check:

# ps aux | grep sleep


# Step 5

# PID identify karo.

# Example:

# root    5432    ... sleep 60

# Yahan PID:

# 5432



# Step 6

# Kill:

# kill 5432

# Tumhare actual PID ko use karna.



# Step 7

# Verify:

# ps aux | grep sleep


#  Cybersecurity Connection

# Imagine tumhe ek Linux machine investigate karni hai aur user bolta hai:

# "Mujhe lagta hai system me kuch suspicious chal raha hai."

# Sabse basic questions me se ek hoga:

# What is running?

# Tum:

# ps aux

# run kar sakte ho.

# Then observe:

# Process
#    ↓
# PID
#    ↓
# CPU usage
#    ↓
# Memory usage
#    ↓
# Command

# Agar koi unfamiliar process dikhe, sirf naam dekhkar usse malicious assume nahi karna. Pehle investigate karna hota hai.

# Ye important cybersecurity mindset hai:

# Observe → Identify → Investigate → Act



#  Foreground vs Background

# Foreground
# sleep 60

# Terminal command ke complete hone ka wait karega.

# Background
# sleep 60 &

# Terminal available rahega aur process background me chalega.

# Foreground:

# Terminal → Process
#             ↓
#        Terminal waits


# Background:

# Terminal → Process
#    ↓
# Available      Process continues



#  Processes vs Services

# Aaj basic distinction samjho.

# Process

# Currently running program instance.

# Example:

# python
# bash
# sleep
# Service

# Background system/application functionality jo usually continuously available rehne ke liye configured hoti hai.

# Examples:

# SSH service
# Web server
# Database service

# Services ke saath hum later deeper practice karenge.



#  Day 12 Main Task

# Tumhare task ka exact requirement:

# ps aux use karo aur 5 running processes notes me likho aur batao tumhe lagta hai har process kya karta hai.

# Notes format:

# DAY 12 — PROCESS OBSERVATION

# 1. Process:
#    PID:
#    CPU:
#    Memory:
#    What I think it does:

# 2. Process:
#    PID:
#    CPU:
#    Memory:
#    What I think it does:

# 3. Process:
#    PID:
#    CPU:
#    Memory:
#    What I think it does:

# 4. Process:
#    PID:
#    CPU:
#    Memory:
#    What I think it does:

# 5. Process:
#    PID:
#    CPU:
#    Memory:
#    What I think it does:

# Tumhare actual ps aux output ke according values fill karna.



#  Useful Extra Command

# Agar ps aux ka output bahut long ho jaye:

# ps aux | less

# Phir:

# q

# se exit.

# Ye tumhare Day 10 ke less knowledge ko bhi reinforce karega.



# Day 12 Revision Questions

# Q1. Process kya hota hai?

# Q2. PID kya hota hai?

# Q3. ps kya karta hai?

# Q4. ps aux aur top me kya difference hai?

# Q5. top se bahar kaise aate hain?

# Q6. sleep 60 & me & ka kya purpose hai?

# Q7. Kisi process ko terminate karne ke liye basic command kya hai?

# Q8. kill PID me PID kya represent karta hai?

# Q9. Foreground aur background process me kya difference hai?

# Q10. Cybersecurity investigation me running processes dekhna important kyun hai?



# Mini Challenge

# Bina upar dekhe ye complete karo:

# sleep 120 &

# Phir:

# ps aux | grep sleep

# PID identify karo.

# Phir:

# kill <PID>

# Finally verify:

# ps aux | grep sleep

# Note: <PID> ko literally type nahi karna; apne actual sleep process ka number use karna.



#  Day 12 Completion Checklist
# ☐ Process concept understood
# ☐ PID understood
# ☐ ps practiced
# ☐ ps aux practiced
# ☐ 5 processes identified
# ☐ top practiced
# ☐ top exited with q
# ☐ Foreground process understood
# ☐ Background process understood
# ☐ sleep 60 & executed
# ☐ Process PID identified
# ☐ kill used on sleep process
# ☐ Process termination verified
# ☐ Services concept understood
# ☐ Notes written
# ☐ Revision questions attempted


# Move Forward If...

# Tum confidently:

# ps aux

# se processes dekh sakte ho,

# top

# se live activity observe kar sakte ho,

# aur:

# sleep 60 &
# kill <PID>

# se ek harmless process start aur terminate kar sakte ho.

# Day 12 ka core takeaway:

# ps   → processes ka snapshot
# top  → live monitoring
# PID  → process ki ID
# kill → process ko signal
# &    → background me run