# Day 13 — Linux Networking Commands 🌐

# Aaj hum Linux terminal se network ko inspect aur test karna seekhenge. Cybersecurity me ye commands bahut important hain, especially network troubleshooting aur authorized reconnaissance ke liye.



#  Today's Goal

# Aaj ke end tak ye 5 commands basic level par use karni aani chahiye:

# Command	Kaam
# ip	Network interfaces aur IP address dekhna
# ping	Connectivity check karna
# ss	Network connections/ports dekhna
# curl	Website/server se data request karna
# dig	DNS information check karna




# 1. ip — Apna IP Address Dekhna

# Sabse pehle:

# ip a

# Ya:

# ip addr

# Tumhe kuch aisa output milega:

# 1: lo: <LOOPBACK,UP,LOWER_UP>
#     inet 127.0.0.1/8

# 2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
#     inet 172.20.10.5/20



# Important

# 127.0.0.1 ko localhost/loopback address kehte hain.

# Tumhe generally eth0 ke neeche:

# inet 172.x.x.x/...

# jaisa address milega.

# WSL me IP address Windows/WSL configuration ki wajah se alag ho sakta hai, isliye jo tumhare terminal me aaye wahi note karna.

# Practice
# ip a

# Phir identify karo:

# Interface:
# IP Address:



# 2. ping — Internet Connectivity Check

# Ab:

# ping google.com

# Tumhe kuch aisa mil sakta hai:

# PING google.com (...) ...
# 64 bytes from ...: icmp_seq=1 ttl=... time=...
# 64 bytes from ...: icmp_seq=2 ttl=... time=...

# ping check karta hai ki destination tak network communication ho pa rahi hai ya nahi.

# Ping ko stop karna

# Linux me:

# Ctrl + C

# press karo.

# Better practice

# Pehle:

# ping google.com

# Stop:

# Ctrl + C

# Phir second website:

# ping cloudflare.com

# Again:

# Ctrl + C



# 3. ss — Network Connections Dekhna

# Ab:

# ss

# Aur detailed information ke liye:

# ss -tuln

# Iska basic meaning


# -t

# TCP

# -u

# UDP

# -l

# Listening sockets

# -n

# Numeric addresses/ports

# Example:

# Netid  State   Local Address:Port
# tcp    LISTEN  0.0.0.0:22

# Yahan 22 ek port number hai.


# Cybersecurity me listening ports important hote hain because they indicate which network services may be accepting connections.

#  Aaj sirf inspect karna hai. Kisi unknown service ko disable/kill nahi karna.




# 4. curl — Website ka HTML Terminal Me Dekhna

# Ab:

# curl https://example.com

# Tumhe webpage ka raw HTML terminal me milega.

# Example:

# <!doctype html>
# <html>
# <head>
# ...
# </head>
# <body>
# ...
# </body>
# </html>

# Browser ki tarah formatted webpage nahi dikhega.

# HTML ko file me save karna

# Ye tumhare Day 13 task ka important part hai:

# curl https://example.com -o webpage.html

# Check karo:

# ls

# Tumhe:

# webpage.html

# dikhega.

# Phir:

# cat webpage.html

# Ya:

# less webpage.html




# 5. dig — DNS Information

# Ab:

# dig google.com

# Output me tumhe DNS information milegi.

# Sirf answer section dekhne ke liye:

# dig google.com +short

# Example:

# 142.250.x.x

# DNS ka basic kaam:

# Domain name
#      ↓
# DNS
#      ↓
# IP address

# For example:

# google.com → IP address



# Cybersecurity Connection

# Ye commands cybersecurity me foundation hain:

# ip
#  ↓
# Apne network ko samjho

# ping
#  ↓
# Connectivity test karo

# ss
#  ↓
# Connections / listening ports inspect karo

# dig
#  ↓
# DNS information dekho

# curl
#  ↓
# Server se directly HTTP/HTTPS response dekho

# Later authorized security testing me in concepts ka use reconnaissance, troubleshooting aur service identification me hota hai.



#  Day 13 Practice

# Ab exactly ye commands run karo:

# Step 1 — IP
# ip a

# Step 2 — Website #1
# ping google.com

# Ctrl + C

# Step 3 — Website #2
# ping cloudflare.com

# Ctrl + C

# Step 4 — Listening/network sockets
# ss -tuln

# Step 5 — Website HTML
# curl https://example.com

# Step 6 — Save HTML
# curl https://example.com -o webpage.html

# Step 7 — Verify file
# ls -l webpage.html

# Step 8 — Read it
# head webpage.html

# Step 9 — DNS
# dig google.com +short




#  Day 13 Final Task

# Apne /home/vishwajeet/linux-practice folder me task complete karo:

# cd /home/vishwajeet/linux-practice

# Create a notes file:

# touch day13-networking.txt

# Open/edit karne ke liye beginner-friendly option:

# nano day13-networking.txt

# Isme ye information likho:

# DAY 13 — Linux Networking

# 1. My IP Address:
# [apna IP]

# 2. Ping Test 1:
# google.com
# Result: Successful / Failed

# 3. Ping Test 2:
# cloudflare.com
# Result: Successful / Failed

# 4. Listening Ports:
# [ss -tuln se jo important ports dikhe]

# 5. curl:
# Website: https://example.com
# Output file: webpage.html

# 6. DNS:
# Domain: google.com
# IP returned:
# [dig google.com +short ka result]

# 7. What I Learned:
# - ip
# - ping
# - ss
# - curl
# - dig

# Save in nano:

# Ctrl + O
# Enter
# Ctrl + X



#  Final Folder

# Tumhare folder me roughly ye hona chahiye:

# linux-practice/
# ├── day10.txt
# ├── security.log
# ├── day13-networking.txt
# ├── webpage.html
# └── ...

# Check:

# ls -lah





# Day 13 Revision

# Khud se answer try karo:

# Q1. ip a ka kya use hai?

# Q2. 127.0.0.1 kya represent karta hai?

# Q3. ping kya check karta hai?

# Q4. ss -tuln ka kya use hai?

# Q5. curl aur browser me basic difference kya hai?

# Q6. curl https://example.com -o webpage.html kya karega?

# Q7. DNS ka basic purpose kya hai?

# Q8. dig google.com +short kya information deta hai?

# Q9. TCP aur UDP kya hain?

# Q10. Cybersecurity me network commands kyun important hain?




#  Day 13 Completion Checklist

# ☐ ip a successfully run
# ☐ Apna IP identify kiya
# ☐ ping google.com run kiya
# ☐ ping cloudflare.com run kiya
# ☐ ss -tuln run kiya
# ☐ curl se webpage fetch kiya
# ☐ HTML ko webpage.html me save kiya
# ☐ dig use kiya
# ☐ day13-networking.txt notes banaye
# ☐ Revision questions complete kiye



#  Move Forward If...

# Tum bina help ke roughly explain kar sako:

# ip   → IP/network information
# ping → connectivity
# ss   → connections/ports
# curl → HTTP/HTTPS request
# dig  → DNS information