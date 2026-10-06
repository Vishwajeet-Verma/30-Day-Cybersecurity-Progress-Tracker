# Day 21 — Networking Practical Day

# Aaj se theory ko real cybersecurity tools ke saath practice karna start karenge. Tumhare Day 18 ke ports aur Day 20 ke HTTP/HTTPS concepts aaj directly use honge.

# Important ethical rule: Nmap sirf localhost, 127.0.0.1, apne systems, ya explicitly authorized labs par run karna. Random public IP/domain scan nahi karna.

#  Today's Goal

# Aaj hum 2 important tools use karenge:



#  Nmap

# Network Mapper

# Iska use network hosts/services ke baare mein information gather karne aur ports scan karne ke liye hota hai.

# Wireshark

# Network packets ko capture aur inspect karne ke liye use hota hai.

# Simple difference:

# Nmap
# ↓
# "Kaunse ports/services available hain?"

# Wireshark
# ↓
# "Network par actual packets mein kya communicate ho raha hai?"
# Part 1 — Nmap



# 1. Nmap Kya Karta Hai?

# Suppose tumhare computer par services chal rahi hain:

# 22   SSH
# 80   HTTP
# 443  HTTPS

# Nmap scan karke identify karne mein help kar sakta hai ki kaunse ports reachable/open hain.

# Conceptually:

# Your Computer
#      │
#      ├── Port 22   → ?
#      ├── Port 80   → ?
#      ├── Port 443  → ?
#      └── Port 8080 → ?
#               ↓
#             Nmap
#               ↓
#        Port information


# 2. Nmap Install Check Karo

# WSL/Ubuntu terminal mein:

# nmap --version

# Agar Nmap installed hai, version show hoga.

# Agar:

# Command 'nmap' not found

# aaye, install karo:

# sudo apt update
# sudo apt install nmap

# Phir:

# nmap --version




# 3. Ethical Boundary

# Aaj hum sirf apni machine scan karenge.

# Safe targets:

# 127.0.0.1

# aur:

# localhost

# Ye tumhari own local machine ko refer karte hain.

#  Aise random targets scan mat karna:

# google.com
# facebook.com
# random public IP
# college website
# someone else's server

# Even if a basic scan technically work kare, authorization ke bina scanning avoid karo.

#  4. First Nmap Scan

# Run:

# nmap localhost

# Ya:

# nmap 127.0.0.1

# Nmap output roughly aisa ho sakta hai:

# Starting Nmap ...

# PORT     STATE SERVICE
# 22/tcp   open  ssh
# 80/tcp   open  http

# Tumhare output mein ports different ho sakte hain.



# 5. Output Kaise Read Karna Hai?

# Main table:

# PORT     STATE     SERVICE
# 22/tcp   open      ssh

# Isko 3 parts mein samjho.

# 22/tcp

# Port:

# 22

# Protocol:

# TCP


# open

# Nmap ko us port par reachable/open service mili.

# ssh

# Nmap service ko identify/associate karne ki koshish kar raha hai.


# 6. Day 18 Connection 

# Day 18 mein humne padha tha:

# 22  → SSH
# 53  → DNS
# 80  → HTTP
# 443 → HTTPS
# 3389 → RDP

# Aaj Nmap mein agar:

# 22/tcp open ssh

# dikhta hai, to Day 18 ka knowledge directly apply hota hai.



# 7. open Ka Matlab Vulnerable Hai?    # Nahi.

# Ye bahut important cybersecurity concept hai.

# Open Port
#     ≠
# Vulnerability

# Open port ka matlab generally:

# Us port par koi service listening/reachable hai.

# Security analysis mein phir questions hote hain:

# Service kya hai?
# Expected hai?
# Correctly configured hai?
# Authentication secure hai?
# Software updated hai?
# Known vulnerabilities hain?



# 8. Nmap Scan + Your Day 18 Knowledge

# Pehle run karo:

# nmap localhost

# Output save karna ho to:

# nmap localhost -oN day21-nmap.txt

# Isse current directory mein:

# day21-nmap.txt

# banega.

# Check:

# cat day21-nmap.txt






# Part 2 — Wireshark 


# 9. Wireshark Kya Hai?

# Wireshark ek packet analyzer hai.

# Network communication ko packets mein capture karke inspect kar sakte ho.

# Conceptually:

# Browser
#    ↓
# Network packets
#    ↓
# Network Interface
#    ↓
# Wireshark
#    ↓
# Packet details


# 10. Packet Kya Hai?

# Network par data generally ek giant block ke form mein simply travel nahi karta.

# Communication network packets mein divided hoti hai.

# Example:

# Computer A
#     ↓
# [Packet 1]
# [Packet 2]
# [Packet 3]
# [Packet 4]
#     ↓
# Computer B

# Wireshark in packets ko capture aur display kar sakta hai.



# 11. Wireshark Open Karo

# Agar Windows par Wireshark installed hai:

# Start Menu → Wireshark

# Open karo.

# Tumhe network interfaces dikh sakte hain, such as:

# Wi-Fi
# Ethernet

# WSL ke context mein interfaces alag ho sakte hain, isliye Windows mein jo interface actually active network traffic carry kar raha hai, usse choose karna easiest rahega.

# Agar unsure ho, jis interface ke saamne traffic graph/activity clearly change ho rahi ho, woh likely active interface hai.



# 12. 60-Second Capture

# Wireshark mein active interface select karo.

# Then:

# Start Capture

# Ab browser open karo aur kuch normal browsing activity karo.

# For example:

# Open a website
# Reload page
# Search something

# Approximately 60 seconds capture karo.

# Phir:

# Stop Capture

# 13. Wireshark Mein Kya Dikhega?

# Tumhe table milegi:

# No.   Time   Source   Destination   Protocol   Length   Info

# Example:

# 1    0.000   ...      ...            DNS        72       Standard query
# 2    0.010   ...      ...            TCP        66       SYN
# 3    0.015   ...      ...            TCP        66       SYN, ACK
# 4    0.020   ...      ...            TCP        54       ACK

# Abhi har field memorize karne ki zarurat bilkul nahi hai.


# 14. Important Protocols Identify Karo

# Capture mein tumhe protocols mil sakte hain:

# DNS
# TCP
# UDP
# TLS
# QUIC
# HTTP
# ARP
# ICMP

# Tumhara goal aaj sirf:

# "Mujhe packets dekhna aur basic protocol names identify karna aata hai."

# Deep packet analysis later karenge.



# 15. Wireshark Filter — DNS

# Agar capture mein DNS traffic hai:

# dns

# display filter box mein enter karo.

# Isse primarily DNS-related packets filter honge.

# Conceptually:

# Browser/Application
#       ↓
# DNS query
#       ↓
# DNS response



# Day 19 ka DNS concept yahan real packets mein dikh sakta hai.


# 16. TCP Filter

# Try:

# tcp

# Isse TCP packets filter kar sakte ho.

# Day 18 mein humne TCP padha tha.

# TCP connection establish hone par tum potentially:

# SYN
# SYN, ACK
# ACK

# jaise packets dekh sakte ho.

# Ye wahi TCP 3-way handshake hai jo Day 18 mein padha tha.

# 17. HTTPS/TLS

# Modern websites generally HTTPS use karti hain.

# Wireshark mein tumhe:

# TLS

# ya modern traffic mein:

# QUIC

# jaise protocols bhi mil sakte hain.




# Important:

# HTTPS use hone par application data generally encrypted hota hai.

# Isliye Wireshark capture mein tum necessarily webpage ka plain text content nahi dekhoge.




# Security Reminder

# Wireshark mein capture kiya hua traffic sensitive ho sakta hai.

# Especially:

# Login information
# Session identifiers
# Private communications
# Internal network information

# Isliye apne system/network ya authorized lab traffic par hi packet capture practice karo.

# Aur captured files ko publicly upload/share mat karo.




#  Day 21 Practical Task

# Tumhara final task:

# Part A — Nmap

# Run:

# nmap localhost

# Record:

# Port:
# Protocol:
# State:
# Likely Service:

# Example format:

# 22/tcp
# State: open
# Service: SSH

# Har actual open port ke liye ek entry banao.


# Part B — Wireshark

# 60-second capture ke baad at least 5 packets observe karo.

# Notes mein:

# Packet 1:
# Protocol:
# What I noticed:

# Packet 2:
# Protocol:
# What I noticed:

# Packet 3:
# Protocol:
# What I noticed:

# Packet 4:
# Protocol:
# What I noticed:

# Packet 5:
# Protocol:
# What I noticed:

# Aaj detailed packet decoding ki requirement nahi hai.




#  Day 21 Notes File

# Folder:

# cd ~/networking-practice

# Create:

# touch day21-networking-practical.txt

# Open:

# nano day21-networking-practical.txt

# Structure:

# DAY 21 — NETWORKING PRACTICAL

# 1. NMAP
# What is Nmap?

# 2. Ethical Boundary
# Nmap should only be used against systems that I own or
# systems for which I have explicit authorization.

# 3. My Nmap Command


# nmap localhost

# 4. Nmap Results
# Port:
# Protocol:
# State:
# Service:

# 5. WIRESHARK
# What is Wireshark?

# 6. My Capture
# Duration: 60 seconds

# Packet 1:
# Protocol:
# Observation:

# Packet 2:
# Protocol:
# Observation:

# Packet 3:
# Protocol:
# Observation:

# Packet 4:
# Protocol:
# Observation:

# Packet 5:
# Protocol:
# Observation:





# 7. DAY 18 CONNECTION

# Nmap helped me identify ports/services that I previously
# learned about on Day 18.

# 8. DAY 19 CONNECTION
# Wireshark can show DNS-related network traffic.

# 9. DAY 20 CONNECTION
# Wireshark can show TCP/TLS/HTTP-related traffic depending
# on the website and network traffic.

# 10. WHAT I LEARNED




#  Day 21 Revision

# Answer these without looking back:

# Q1.

# Nmap kya hai?

# Q2.

# Nmap ka basic use kya hai?

# Q3.

# nmap localhost safe practice target kyun hai?

# Q4.

# 22/tcp open ssh ka kya meaning hai?

# Q5.

# Open port ka matlab automatically vulnerability hota hai?

# Q6.

# Wireshark kya karta hai?

# Q7.

# Packet kya hota hai?

# Q8.

# Wireshark mein dns filter ka purpose kya hai?

# Q9.

# TCP 3-way handshake mein kaunse three steps hote hain?

# Q10.

# Kisi doosre person's/public server ko bina permission scan karna kyun avoid karna chahiye?





#  Today's Most Important Connection

# Ab tak tumne jo padha hai, woh aaj connect hoga:

#              DAY 17
#           IP Address
#               ↓
#              Day 18
#         Port + TCP/UDP
#               ↓
#              Day 19
#              DNS
#               ↓
#              Day 20
#           HTTP/HTTPS
#               ↓
#              DAY 21
#         Nmap + Wireshark

# Example:

# google.com
#     ↓
# DNS → IP address
#     ↓
# IP + Port 443
#     ↓
# TCP/TLS/HTTPS communication
#     ↓
# Packets
#     ↓
# Wireshark can observe traffic

# Aur:

# Nmap
#  ↓
# "Is localhost par kaunse ports open hain?"






#  Day 21 Checklist

# ☐ Nmap installed
# ☐ nmap --version checked
# ☐ localhost scan completed
# ☐ Open ports identified
# ☐ Services identified
# ☐ Wireshark opened
# ☐ 60-second capture completed
# ☐ 5 packets observed
# ☐ DNS/TCP/TLS concepts connected
# ☐ Ethical boundary understood
# ☐ Notes written
# ☐ Revision completed




#  Move Forward If...

# Tum ye 3 statements confidently explain kar sako:

# Nmap → ports/services discover karne ke liye.

# Wireshark → network packets capture/inspect karne ke liye.

# Ethical rule → sirf apne ya explicitly authorized systems ko scan/capture karna.

# Ab practical start karo:

# Step 1:

# nmap localhost