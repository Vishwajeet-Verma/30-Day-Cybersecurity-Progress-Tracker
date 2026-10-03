# Day 19 — DNS (Domain Name System)

# Aaj hum DNS samjhenge — internet ka ek bahut important concept. Day 17 mein humne IP addresses aur Day 18 mein ports padhe the. Ab samjhenge ki google.com jaise naam ko computer IP address mein kaise convert karta hai.



# Today's Goal

# Aaj ke end tak ye explain karna aana chahiye:

# DNS domain name ko corresponding IP address se resolve karne mein help karta hai, taaki computer correct server tak connect kar sake.

# Aaj hum seekhenge:

# DNS kya hai?
# DNS ki zarurat kyun hai?
# Domain → IP address kaise milta hai?
# DNS lookup ka basic process
# dig / nslookup ka use
# DNS aur cybersecurity ka connection


# 1. DNS Kya Hai?

# DNS = Domain Name System

# Simple language mein:

# DNS internet ka phonebook/address book hai.

# Hum humans ke liye:

# google.com
# youtube.com
# github.com

# yaad rakhna easy hai.

# Computer network communication ke liye IP addresses use karta hai, jaise:

# 142.250.x.x

# DNS domain name ko IP address se resolve karne mein help karta hai.

# Example

# Tum browser mein type karte ho:

# google.com

# DNS lookup ke through system ko Google ke relevant IP address mil sakte hain.

# Phir browser us IP address par connection establish karta hai.




# 2. DNS Ki Zarurat Kyun Hai?

# Imagine karo agar websites ke names nahi hote.

# Tumhe Google use karne ke liye yaad rakhna padta:

# 142.250.xxx.xxx

# YouTube:

# 142.250.xxx.xxx

# GitHub:

# 140.82.xxx.xxx

# Aur problem ye hai ki websites ke IP addresses change bhi ho sakte hain aur ek domain ke multiple IP addresses bhi ho sakte hain.

# Isliye:

# Human → Domain Name
# Computer/Network → IP Address
# DNS → In dono ke beech resolution



# 3. Domain Name → IP Address

# Basic flow:

# You type:

# google.com
#      ↓
# DNS Lookup
#      ↓
# IP Address
#      ↓
# Server se connection
#      ↓
# Website



# For example, conceptually:

# google.com
#     ↓
# DNS
#     ↓
# 142.250.x.x
#     ↓
# Google server

# Important: Google ka actual returned IP tumhare DNS resolver, location, time aur network ke according different ho sakta hai. Isliye exact IP ko fixed value mat samajhna.







# 4. DNS Lookup Kya Hota Hai?

# Jab tum kisi domain ka IP address discover karne ke liye DNS se query karte ho, use broadly DNS lookup kehte hain.

# Linux mein hum dig use kar sakte hain.

# Run:

# dig google.com

# Output kaafi detailed ho sakta hai.

# Tumhe kuch sections milenge:

# QUESTION SECTION
# ANSWER SECTION
# AUTHORITY SECTION
# ADDITIONAL SECTION

# Abhi sab memorize karne ki zarurat nahi hai.

# 5. dig Ka Simple Version

# Try:

# dig google.com +short

# Ye mostly directly returned address records dikhata hai.

# Example:

# 142.250.xx.xx
# 142.251.xx.xx

# Tumhare system par output different ho sakta hai.

# Iska meaning:

# google.com
#     ↓
# DNS
#     ↓
# 142.250.xx.xx




# 6. nslookup Bhi Use Kar Sakte Ho

# Alternative command:

# nslookup google.com

# Output mein kuch aisa information aa sakta hai:

# Server:     ...
# Address:    ...

# Name:       google.com
# Addresses:  ...

# Yahan:

# Server

# Tumhara DNS resolver/server.

# Name

# Jis domain ko tumne lookup kiya.

# Addresses

# DNS ne jo IP addresses return kiye.



# 7. DNS Lookup Process — Conceptually

# Thoda deeper samjho.

# Suppose tum browser mein enter karte ho:

# www.example.com

# High-level process:

# Browser
#    ↓
# Operating System
#    ↓
# DNS Resolver
#    ↓
# DNS hierarchy
#    ↓
# IP address
#    ↓
# Browser connects to server

# DNS infrastructure mein different types ke servers/resolvers involved ho sakte hain.

# Broadly tum ye names sunoge:

# DNS Resolver
# Root DNS Servers
# TLD DNS Servers
# Authoritative DNS Servers

# Example:

# www.example.com
#       ↓
#       .
#       ↓
#     .com
#       ↓
#  example.com
#       ↓
# Authoritative DNS
#       ↓
# IP address

# Ye conceptual flow hai; real DNS resolution mein caching ki wajah se har query ko complete hierarchy traverse karna zaroori nahi hota.



# 8. DNS Caching

# Ye important concept hai.

# Agar tumne recently google.com lookup kiya hai, tumhara system ya DNS resolver result temporarily cache kar sakta hai.

# Next time:

# google.com
#     ↓
# Cache check
#     ↓
# Result available?
#     ↓
# Yes → cached result use

# Isse DNS queries reduce hoti hain aur response faster ho sakta hai.

# DNS records ke saath TTL (Time To Live) associated ho sakta hai, jo batata hai ki result ko kitni der cache kiya ja sakta hai.



# 9. DNS Sirf IP Address Ke Liye Nahi Hai

# DNS mein different types ke records hote hain.



# A Record

# Domain → IPv4 address

# example.com → 93.184.xxx.xxx



# AAAA Record

# Domain → IPv6 address

# example.com → IPv6 address




# MX Record

# Mail servers identify karta hai.

# example.com → mail server



# CNAME

# Ek domain/hostname ko doosre hostname ke alias ke roop mein point kar sakta hai.

# Abhi tumhe mainly A record samajhna hai.




# Practice 1 — Google

# Run:

# dig google.com +short

# Phir:

# nslookup google.com

# Tumhe kya observe karna hai?
# Kaunsa DNS server use hua?
# Google ke kitne addresses return hue?
# Kya output mein IPv4 address hai?
# nslookup aur dig ka output exactly same hai ya different format mein hai?



#  Practice 2 — 2 Aur Websites

# Try:

# dig youtube.com +short
# dig github.com +short

# Agar dig installed nahi hai:

# nslookup youtube.com
# nslookup github.com


# Comparison table banao:

# Domain	        Command	               Returned IP(s)

# google.com	dig google.com +short	Your output
# youtube.com	dig youtube.com +short	Your output
# github.com	dig github.com +short	Your output

# Important: IP addresses tumhare output ke according fill karna. Internet par examples se IP copy mat karna.



#  10. DNS + Cybersecurity

# DNS cybersecurity mein bahut important hai.

# DNS Spoofing

# Attacker DNS response ko manipulate karke user ko incorrect destination par direct karne ki koshish kar sakta hai.

# Conceptually:

# User
#  ↓
# example.com
#  ↓
# Manipulated DNS response
#  ↓
# Wrong IP
#  ↓
# Fake/Malicious destination



# DNS Cache Poisoning

# DNS cache mein incorrect DNS information insert karne ki technique ko broadly DNS cache poisoning kaha jata hai.

# Goal ho sakta hai:

# Legitimate domain
#        ↓
# Incorrect cached IP
#        ↓
# Unexpected destination





#  11. DNS As A Security Tool

# DNS sirf attack target nahi hai.

# Security teams DNS ka use defense ke liye bhi karti hain.

# For example:

# User
#  ↓
# DNS request
#  ↓
# Security DNS filtering
#  ↓
# Known malicious domain?
#    ↙          ↘
#  YES          NO
#  ↓             ↓
# Block         Allow

# Isse malicious/phishing domains ko block karne mein help mil sakti hai.




#  12. Very Important Cybersecurity Point

# Agar tum Wireshark ya security logs analyze karoge, tumhe DNS traffic dikh sakta hai.

# Typical DNS query:

# Client → DNS Resolver
# "What is the IP address of example.com?"

# Response:

# DNS Resolver → Client
# "Here is the answer."

# Isliye cybersecurity mein normal DNS behavior samajhna important hai.



#  Day 19 Practical Task

# Pehle folder open karo:

# cd ~/networking-practice

# Notes file banao:

# touch day19-dns.txt

# Check:

# ls

# Ab:

# nano day19-dns.txt

# Is structure ko use karo:

# DAY 19 — DNS

# 1. What is DNS?
# DNS stands for Domain Name System. It helps resolve domain names to IP addresses.

# 2. Why is DNS Needed?
# DNS makes it easier for humans to use domain names instead of remembering IP addresses.

# 3. Domain → IP
# Example:
# google.com → DNS lookup → IP address

# 4. DNS Lookup Process
# Browser
# ↓
# Operating System
# ↓
# DNS Resolver
# ↓
# DNS infrastructure
# ↓
# IP address
# ↓
# Server connection

# 5. Commands Used

# Command 1:
# dig google.com +short

# Output:
# PASTE YOUR OUTPUT HERE

# Command 2:
# dig youtube.com +short

# Output:
# PASTE YOUR OUTPUT HERE

# Command 3:
# dig github.com +short

# Output:
# PASTE YOUR OUTPUT HERE

# 6. My DNS Server
# Write the DNS server shown by nslookup/dig.

# 7. A Record
# An A record maps a domain/hostname to an IPv4 address.

# 8. Cybersecurity Connection
# DNS can be targeted through attacks such as DNS spoofing and cache poisoning.
# DNS filtering can also help block malicious domains.

# 9. What Happens If DNS Stops Working?
# Write your one-sentence answer.

# 10. What I Learned
# Write 3-5 points about today's lesson.



#  Day 19 Quick Challenge

# Without looking above, answer these:

# Q1.

# DNS ka full form kya hai?

# Q2.

# DNS ka main kaam kya hai?

# Q3.

# google.com kya hai?

# Q4.

# 142.250.x.x kis type ki information represent kar sakta hai?

# Q5.

# dig google.com +short kya karta hai?

# Q6.

# A record kis cheez se related hai?

# Q7.

# DNS caching kya hoti hai?

# Q8.

# DNS spoofing kya hota hai?

# Q9.

# DNS filtering security mein kaise help kar sakti hai?

# Q10.

# Agar DNS completely stop ho jaye, existing internet connections aur new domain lookups par kya effect padega?



#  One-Sentence Challenge

# Ye sentence apne words mein complete karo:

# “DNS is like the internet's ______ because ______.”




#  Day 19 Checklist

# ☐ DNS concept understood
# ☐ Domain → IP understood
# ☐ dig/nslookup understood
# ☐ google.com lookup completed
# ☐ youtube.com lookup completed
# ☐ github.com lookup completed
# ☐ DNS caching understood
# ☐ DNS security connection understood
# ☐ day19-dns.txt written
# ☐ Revision questions completed



#  Move Forward If...

# Tum bina notes dekhe kisi beginner ko ye explain kar sako:

# “Jab main browser mein google.com type karta hoon, DNS us domain ko resolve karne mein help karta hai taaki system ko server se connect karne ke liye required IP information mil sake.”

# Ab terminal mein ye 3 commands run karo aur output yahan paste karo:

# dig google.com +short
# dig youtube.com +short
# dig github.com +short