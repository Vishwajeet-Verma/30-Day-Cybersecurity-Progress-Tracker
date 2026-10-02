# Day 18 — Ports, TCP & UDP

# Aaj ka topic bahut important hai, kyunki ab tak tumne IP address samjha, aur aaj samjhoge ki IP address ke andar actual service/application ko kaise identify kiya jata hai — ports ke through.




#  Today's Goal

# Aaj samjhoge:

# Port kya hota hai
# Port range 0–65535
# TCP kya hai
# UDP kya hai
# TCP vs UDP
# Common ports
# ss -tuln se listening ports dekhna
# Open/listening ports ka cybersecurity me importance



# 1. Port Kya Hai?

# Simple example:

# Socho ek building ka address hai:

# IP Address
#    ↓
# Building ka address

# Aur building ke andar different doors hain:

# Port
#  ↓
# Specific service/application ka entry point

# Isliye:

# IP + Port

# milkar network destination ko more specifically identify karne me help karte hain.

# Example:

# 192.168.1.10:22

# Yahan:

# 192.168.1.10
#      ↓
# IP address

# 22
#      ↓
# Port


# 2. Port Range

# TCP aur UDP ports:

# 0 – 65535

# range me hote hain.

# Broad categories:

# 0–1023 → Well-known ports

# Common network services ke liye widely associated ports.

# Examples:

# 22
# 53
# 80
# 443



# 1024–49151 → Registered ports

# Various applications/services commonly use kar sakte hain.

# 49152–65535 → Dynamic/private ports

# Often temporary client-side connections ke liye use hote hain.


# Abhi categories ko conceptually samjho; exact allocation rules later detail me dekhenge.



# 3.  Common Ports

# Ye 5 yaad kar lo:

# Port	Common Service	    Protocol

# 22	SSH	                TCP
# 53	DNS	                TCP/UDP
# 80	HTTP	            TCP
# 443	HTTPS	            TCP
# 25	SMTP	            TCP

# Aur kuch useful ports:

# Port	Common Service
# 21	FTP
# 23	Telnet
# 110	POP3
# 143	IMAP
# 3389	RDP

#  Port number automatically guarantee nahi karta ki wahi service actually running hai. Configuration change ho sakti hai.




# 4.  IP + Port Together

# Suppose:

# 192.168.1.10:80

# Meaning conceptually:

# IP
#  ↓
# 192.168.1.10

# Port
#  ↓
# 80

# Agar machine par HTTP service port 80 par listening hai, client us service se communicate kar sakta hai.

# Similarly:

# 192.168.1.10:22

# SSH service ke context me ho sakta hai.




# 5.  TCP Kya Hai?

# TCP = Transmission Control Protocol

# TCP connection-oriented transport protocol hai.

# Simple idea:

# TCP data delivery ko reliable banane ke liye connection, acknowledgements aur retransmission mechanisms use karta hai.

# Example:

# Client                    Server

#   SYN  ─────────────────→
#        ←──────────────── SYN-ACK
#   ACK  ─────────────────→

#        Connection established

# Is process ko commonly TCP three-way handshake kehte hain.

# TCP Reliable Kaise Hai?

# Suppose 5 packets bhejne hain:

# 1  2  3  4  5

# Agar packet 3 missing ho gaya:

# 1 ✓
# 2 ✓
# 3 ✗
# 4 ✓
# 5 ✓

# TCP missing data ko detect/handle karke retransmission kar sakta hai.


# Isliye TCP ko broadly reliable kaha jata hai.






# 6.  UDP Kya Hai?

# UDP = User Datagram Protocol

# UDP connection-oriented handshake nahi karta like TCP.

# Basic idea:

# Client
#   │
#   ├── Packet 1 ──→
#   ├── Packet 2 ──→
#   ├── Packet 3 ──→
#   └── Packet 4 ──→

# UDP generally:

# Connection setup nahi karta like TCP
# Delivery acknowledgement/retransmission provide nahi karta like TCP
# Lower overhead rakhta hai
# Speed/latency-sensitive applications me useful ho sakta hai

# Isliye tumhari roadmap me:

# UDP = fast but unreliable

# likha hai.

# "Unreliable" ka matlab bad protocol nahi hai. It means UDP itself delivery guarantee nahi deta.



#  TCP vs UDP

#       TCP	                                    UDP
# Connection-oriented	                Connectionless
# Reliable delivery mechanisms	        No built-in delivery guarantee
# Acknowledgements	                    No TCP-style acknowledgements
# Retransmission	                    No TCP-style retransmission
# More overhead	                        Lower overhead
# Reliability important ho to useful	Low latency/overhead important ho to useful


# Easy memory:

# TCP
# ↓
# Trust / Reliability

# UDP
# ↓
# Speed / Low overhead




#  Real-World Example

# Imagine live voice/video communication.

# Agar ek tiny piece of audio late ho gaya:

# Audio:
# HELLO....

# Us purane packet ko bahut late receive karne se kabhi-kabhi benefit nahi hota.

# Real-time communication me low latency important ho sakti hai.

# Isi type ke use cases me UDP useful ho sakta hai.






# 7.  ss -tuln

# Ab practical part.

# Tumne Day 13 me already ss dekha tha.

# Run:

# ss -tuln

# Breakdown:

# -s

# Actually yahan ss command hai.

# Options:

# -t → TCP
# -u → UDP
# -l → listening
# -n → numeric

# So:

# ss -tuln

# means roughly:

# TCP/UDP sockets jo listening state me hain, unhe numeric form me show karo.




#  Practice

# Run:

# ss -tuln

# Output kuch aisa ho sakta hai:

# Netid  State   Local Address:Port
# tcp    LISTEN  0.0.0.0:22
# tcp    LISTEN  127.0.0.1:631
# udp    UNCONN  0.0.0.0:5353

# Tumhara output different ho sakta hai.




#  Output Kaise Read Karein?

# Suppose:

# tcp   LISTEN   127.0.0.1:8000

# Breakdown:

# tcp
#  ↓
# Protocol

# LISTEN
#  ↓
# Waiting for incoming connection

# 127.0.0.1
#  ↓
# Local machine / loopback

# 8000
#  ↓
# Port




# Important: 127.0.0.1 vs 0.0.0.0

# Ye cybersecurity ke liye important distinction hai.

# 127.0.0.1:8000

# Usually service sirf local machine par accessible hoti hai.

# Your Machine
#     ↓
# 127.0.0.1:8000
#     ↓
# Local only
# 0.0.0.0:8000

# Generally service all available IPv4 interfaces par listen karne ke liye bound hai.

# Network interfaces
#       ↓
# 0.0.0.0:8000

# Actual accessibility firewall/network configuration par depend karegi.



#  Cybersecurity Connection

# Open/listening ports ko simple language me machine ke potential network entry points ki tarah imagine kar sakte ho.

# Example:

# Machine
# │
# ├── Port 22   → SSH
# ├── Port 80   → HTTP
# └── Port 443  → HTTPS



# Security assessment me:

# Which ports are open?
#        ↓
# Which services are behind them?
#        ↓
# Are they expected?
#        ↓
# Are they securely configured?

# questions important hote hain.

#  Open port = automatically vulnerability nahi.

# A properly configured and expected service can legitimately listen on a port.





#  Day 18 Task

# Run:

# ss -tuln

# Aur jo output aaye usme har listening port note karo.

# Table:

# Protocol	Local Address	Port	Guess: What is it?
# TCP	...	...	...
# TCP	...	...	...
# UDP	...	...	...




# Important

# Agar koi port unfamiliar ho:

#  Immediately assume mat karo ki malware hai.

# Instead:

# "I don't know this service yet."

# Phir hum identify karenge.





#  Day 18 Notes

# Networking folder:

# cd ~/networking-practice

# File:

# touch day18-ports-tcp-udp.txt

# Edit:

# nano day18-ports-tcp-udp.txt

# Headings:

# DAY 18 — PORTS, TCP & UDP

# 1. What is a Port?

# 2. Port Range

# 3. Common Ports

# 4. TCP

# 5. UDP

# 6. TCP vs UDP

# 7. IP + Port

# 8. ss -tuln

# 9. My Listening Ports

# 10. Cybersecurity Connection

# 11. What I Learned



#  Revision

# Notes band karke answer karo:

# Q1. Port kya hota hai?

# Q2. TCP/UDP port range kya hai?

# Q3. Port 22 kis service ke saath commonly associated hai?

# Q4. Port 80?

# Q5. Port 443?

# Q6. Port 53?

# Q7. TCP ko reliable kyun kaha jata hai?

# Q8. UDP ko connectionless kyun kaha jata hai?

# Q9. ss -tuln kya karta hai?

# Q10. LISTEN ka basic meaning kya hai?

# Q11. 127.0.0.1:8000 aur 0.0.0.0:8000 me conceptual difference kya hai?

# Q12. Kya open port automatically vulnerability hota hai?



#  Quick Challenge

# Inhe identify karo:

# 22
# 53
# 80
# 443
# 3389

# Expected format:

# 22   → __________
# 53   → __________
# 80   → __________
# 443  → __________
# 3389 → __________


#  Day 18 Checklist
# ☐ Port concept understood
# ☐ 0–65535 range understood
# ☐ 5 common ports learned
# ☐ TCP understood
# ☐ UDP understood
# ☐ TCP vs UDP difference understood
# ☐ ss -tuln run kiya
# ☐ Listening ports identify kiye
# ☐ Unknown ports ko blindly suspicious nahi maana
# ☐ Notes written
# ☐ Revision completed

