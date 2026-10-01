# Day 17 — IP Addresses


# Aaj ka topic cybersecurity ke liye bahut important hai, kyunki logs, firewalls, scanners, alerts aur network tools me IP addresses constantly milenge.

#  Today's Goal

# Aaj tum samjhoge:

# IPv4 kya hota hai
# Private IP kya hota hai
# Public IP kya hota hai
# 127.0.0.1 kya hai
# Basic subnet ka idea
# Private aur public IP me difference


# 1. IP Address Kya Hai?

# IP = Internet Protocol

# IP address ek numerical address hai jo network par kisi interface/device ko identify/address karne ke liye use hota hai.

# Example IPv4:

# 192.168.1.10

# IPv4 address generally 4 numbers/parts me hota hai:

# 192 . 168 . 1 . 10

# Har part ko octet kaha jata hai.

# IPv4 ka conceptual range:

# 0.0.0.0
#       ↓
# 255.255.255.255



# 2.  Private IP

# Private IP address normally local/private networks ke andar use hota hai.

# Common private IPv4 ranges:

# 10.0.0.0 – 10.255.255.255

# 172.16.0.0 – 172.31.255.255

# 192.168.0.0 – 192.168.255.255

# Examples:

# 192.168.1.10
# 192.168.1.20
# 10.0.0.5
# 172.16.1.10

# Tumhare home Wi-Fi me laptop ka IP, for example:

# 192.168.1.10

# ho sakta hai.

#  Example — Home Network
#                  Internet
#                     │
#                  Router
#               192.168.1.1
#               /          \
#              /            \
#         Laptop            Phone
#      192.168.1.10      192.168.1.11

# Yahan:

# 192.168.1.1
# 192.168.1.10
# 192.168.1.11

# private network addresses ke examples hain.






# 3.  Public IP

# Public IP internet-facing address hota hai jo internet par network/device/service ko address karne ke context me use hota hai.

# Home network me normally:

# Laptop
#    ↓
# Router
#    ↓
# ISP
#    ↓
# Public IP
#    ↓
# Internet

# Example:

# 203.x.x.x

#  Ye sirf example hai. Tumhara actual public IP different hoga.




#  Private vs Public IP

# Private IP	                                        Public IP

# Local/private network me use	                        Internet-facing communication ke context me
# Usually router ke behind devices ko assign hota hai	ISP/network se associated ho sakta hai
# Internet par globally unique hona required nahi	    Internet routing ke liye globally meaningful address
# Example 192.168.1.10	                                Example 203.x.x.x




# Easy memory:

# PRIVATE
# ↓
# Inside network

# PUBLIC
# ↓
# Internet-facing






# 4.  NAT — Private IP Internet Tak Kaise Jaata Hai?

# Ye concept tumhare liye important hai.

# Suppose:0

# Laptop
# 192.168.1.10

# website access karta hai.

# Request roughly:

# Laptop
# 192.168.1.10
#       ↓
#    Router
#       ↓
# NAT / Address Translation
#       ↓
# Public IP
#       ↓
# Internet
#       ↓
# Website

# Home router commonly NAT (Network Address Translation) use karta hai.

# Is wajah se ghar ke multiple private-IP devices internet access share kar sakte hain using the network's public address.




# 5. Loopback — 127.0.0.1

# Ye bahut important hai.

# 127.0.0.1

# ko commonly localhost kehte hain.

# Meaning:

# Apni hi machine.

# For example:

# ping 127.0.0.1

# Try karo.

# Tumhe kuch aisa mil sakta hai:

# 64 bytes from 127.0.0.1

# Yahan network ke bahar kisi machine ko contact nahi kar rahe.

# Conceptually:

# Your Computer
#      ↓
# 127.0.0.1
#      ↓
# Your Computer



#  127.0.0.1 "This Machine" Kyun?

# Because 127.0.0.0/8 IPv4 loopback range ke liye reserved hai.

# Isliye:

# 127.0.0.1

# ka traffic local machine par hi loop back karta hai.

# Simple example:

# curl http://127.0.0.1:8000

# Agar tumhari machine par port 8000 par koi local web server chal raha hai, request usi machine ke server ko jayegi.

# Cybersecurity me ye important hai because security tools ke output me:

# 127.0.0.1
# localhost

# dikhe to tumhe pata hona chahiye ki communication local machine se related hai.



# 6. Basic Subnet Idea

# Aaj subnetting ki deep mathematics nahi karni.

# Bas basic concept samjho.

# Suppose:

# 192.168.1.10/24

# Yahan:

# 192.168.1.10
#        +
#       /24

# /24 network ke address structure ke baare me information deta hai.

# Basic level par tum ise aise imagine kar sakte ho:

# Network part       Host part

# 192.168.1          .10

# To:

# 192.168.1.10
# 192.168.1.11
# 192.168.1.20

# same local network ke possible addresses ho sakte hain, depending on the actual subnet configuration.

# Abhi /24 ki mathematical calculation memorize mat karo.

# Bas yaad rakho:

# Subnet/prefix batata hai ki IP address ka kaunsa portion network ko identify karta hai aur kaunsa portion hosts ko.





# Practice 1 — Apna Private IP Find Karo

# Tum WSL/Ubuntu use kar rahe ho, so:

# ip a

# Ya:

# ip addr

# Output me:

# inet ...

# search karo.

# Example:

# 2: eth0:
#     inet 172.20.10.5/20

# Yahan:

# IP = 172.20.10.5
# Prefix = /20

# Tumhara WSL IP example se different hoga.




# Practice 2 — Public IP

# Browser me search karo:

# what is my IP

# Search engine tumhe tumhare internet connection ka public-facing IP dikha sakta hai.

# Tumhe kuch aisa mil sakta hai:

# Public IPv4: xxx.xxx.xxx.xxx
# Important Privacy Point 


# Learning ke liye bas ye record karo:

# Private IP: __________
# Public IP: __________





#  Practice 3 — Loopback

# Run:

# ping 127.0.0.1

# Stop:

# Ctrl + C

# Phir:

# ip a

# me 127.0.0.1 bhi identify karne ki koshish karo.





# Practice 4 — Apne IP Types Identify Karo

# Suppose output:

# inet 127.0.0.1/8
# inet 192.168.1.20/24

# Then:

# 127.0.0.1
# → Loopback

# 192.168.1.20
# → Private IP

# Agar:

# inet 10.0.0.5/24

# dikhe:

# 10.0.0.5
# → Private IP




#  Cybersecurity Connection

# Security logs me tumhe aise entries mil sakti hain:

# 2026-10-01 10:20:01
# Source: 192.168.1.25
# Destination: 192.168.1.10

# Ab tum samajh paoge ki ye private network addresses hain.

# Ya:

# Source: 203.x.x.x
# Destination: 192.168.1.10

# To broadly:

# 203.x.x.x
# → public/internet-facing address

# 192.168.1.10
# → private address

# Security analyst ko IP addresses ko correctly interpret karna aana chahiye.




#  Day 17 Main Task

# Apne notes me ye table banao:

# Item	Your Information
# Private IP	__________
# Public IP	__________
# Loopback	127.0.0.1

# Aur neeche one-sentence explanation:

# A private IP is used within a private/local network, while a public IP is used as an internet-facing address for communication beyond that private network.

# Apne words me likhna better hai.




# Notes File
# cd ~/networking-practice
# touch day17-ip-addresses.txt
# nano day17-ip-addresses.txt

# Use these headings:

# DAY 17 — IP ADDRESSES

# 1. What is an IP Address?

# 2. IPv4

# 3. Private IP

# 4. Public IP

# 5. Loopback Address

# 6. Basic Subnet Concept

# 7. NAT

# 8. My Private IP

# 9. My Public IP

# 10. Cybersecurity Connection

# 11. What I Learned


#  Revision Questions

# Notes band karke answer karo:

# Q1.

# IP ka full form kya hai?

# Q2.

# IPv4 address me kitne octets hote hain?

# Q3.

# 192.168.1.10 kis type ka address hai?

# Q4.

# Private IPv4 ki ek range batao.

# Q5.

# Public IP aur private IP me basic difference kya hai?

# Q6.

# 127.0.0.1 kya represent karta hai?

# Q7.

# localhost ka kya meaning hai?

# Q8.

# NAT ka basic purpose kya hai?

# Q9.

# Subnet ka basic purpose kya hai?

# Q10.

# Security logs me IP address important kyun hai?





#  Quick Challenge

# In addresses ko classify karo:

# 1. 127.0.0.1
# 2. 192.168.1.50
# 3. 10.0.0.25
# 4. 172.20.5.10
# 5. 8.8.8.8

# Format:

# 1. __________
# 2. __________
# 3. __________
# 4. __________
# 5. __________

# Hint: Private ranges:

# 10.0.0.0/8
# 172.16.0.0/12
# 192.168.0.0/16


#  Day 17 Checklist

# ☐ IPv4 structure understood
# ☐ Private IP understood
# ☐ Public IP understood
# ☐ Private IP found with ip a
# ☐ Public IP checked
# ☐ 127.0.0.1 understood
# ☐ ping 127.0.0.1 tested
# ☐ Basic subnet concept understood
# ☐ NAT basic concept understood
# ☐ Notes written
# ☐ Revision completed
# ☐ IP classification challenge completed