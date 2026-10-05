# Day 20 — HTTP & HTTPS

# Day 15–19 mein humne networking ke fundamentals cover kiye:

# Day 15 → Network
# Day 16 → OSI Model
# Day 17 → IP Addresses
# Day 18 → Ports, TCP & UDP
# Day 19 → DNS
# Day 20 → HTTP & HTTPS 

# Aaj ka concept web security ke liye bahut important hai, kyunki Day 27–29 mein web vulnerabilities start hongi.



#  Today's Goal

# Aaj ke end tak tum samajh paoge:

# Browser aur web server kaise communicate karte hain
# HTTP Request kya hoti hai
# HTTP Response kya hoti hai
# GET, POST jaise HTTP methods
# Status codes: 200, 404, 500 etc.
# Headers kya hote hain
# Cookies kya hoti hain
# HTTPS HTTP se kaise different hai
# Chrome DevTools ke Network tab mein request inspect karna



# 1. HTTP Kya Hai?

# HTTP = HyperText Transfer Protocol

# Simple language mein:

# HTTP ek protocol hai jo web client aur web server ke beech communication ke rules define karta hai.

# Jab tum browser mein:

# https://example.com

# open karte ho, browser server se request karta hai.

# Basic flow:

# Browser
#    │
#    │ HTTP Request
#    ▼
# Web Server
#    │
#    │ HTTP Response
#    ▼
# Browser




# 2. Request → Response Model

# Ye Day 20 ka sabse important concept hai.

# Request

# Browser server ko bolta hai:

# "Mujhe ye resource chahiye."

# Example:

# GET / HTTP/1.1
# Host: example.com

# Response

# Server reply karta hai:

# HTTP/1.1 200 OK

# aur uske baad webpage ka content bhej sakta hai.

# Complete concept:

# Client
#   │
#   │ Request
#   ▼
# Server
#   │
#   │ Response
#   ▼
# Client
# Real-life example

# Restaurant mein:

# You → "Mujhe Pizza chahiye."
# Restaurant → "Ye raha Pizza."

# Web mein:

# Browser → "GET /"
# Server  → "200 OK + webpage"





# 3. HTTP Methods

# HTTP request mein method batata hai ki client kya action karna chahta hai.



# Important methods:

# Method	    Basic purpose
# GET	        Data/resource retrieve karna
# POST	        Data submit/create karna
# PUT	        Resource ko replace/update karna
# PATCH	        Resource ka partial update
# DELETE	    Resource delete karna




# GET

# Example:

# GET /index.html

# Meaning:

# Server, mujhe index.html resource do.

# Browser jab webpage/resources fetch karta hai, GET requests bahut common hoti hain.




# POST

# Example:

# POST /login

# POST commonly server ko data submit karne ke liye use hota hai.

# Conceptually:

# Browser
#    ↓
# POST /login
# username=vishwajeet
# password=******
#    ↓
# Server



# Important cybersecurity point:

# POST ka matlab automatically secure nahi hota.

# Agar request HTTP par ja rahi hai, POST data encrypted nahi hota merely because method POST hai.

# Security ke liye HTTPS important hai.




# 4. HTTP Status Codes

# Server response mein status code deta hai.

# Ye 5 major categories mein divide hote hain:

# 1xx → Informational
# 2xx → Success
# 3xx → Redirection
# 4xx → Client error
# 5xx → Server error


 
# 200 OK

# Meaning:

# Request successfully process hui.

# Example:

# GET /
#    ↓
# 200 OK



# 201 Created

# Usually successful creation ke context mein.

# Example:

# POST /users
#    ↓
# 201 Created



# 301 / 302 — Redirect

# Server/client ko another URL/resource ki taraf redirect kar sakta hai.

# For example:

# http://example.com
#        ↓
# redirect
#        ↓
# https://example.com




# 404 Not Found

# Meaning:

# Requested resource nahi mila.

# Example:

# GET /abc123
#        ↓
# 404





# 500 Internal Server Error

# Usually server side par unexpected error indicate karta hai.

# 5. Status Code Yaad Karne Ka Easy Trick

# 2xx → "Sab successful"
# 3xx → "Idhar se udhar jao"
# 4xx → "Client/request side problem"
# 5xx → "Server side problem"

# Examples:

# 200 → Success
# 301 → Redirect
# 404 → Not Found
# 500 → Server Error




# 6. Headers Kya Hote Hain?

# Headers request/response ke saath additional information/metadata carry karte hain.

# Example response:

# HTTP/1.1 200 OK
# Content-Type: text/html
# Content-Length: 1250
# Server: example

# Yahan:

# Content-Type
# Content-Length
# Server

# headers hain.






# 7. Important Response Headers


# Content-Type

# Batata hai response mein kis type ka content hai.

# Example:

# Content-Type: text/html

# Meaning:

# Response HTML hai.

# Another example:

# Content-Type: application/json

# Meaning:

# Response JSON data hai.

# Content-Length

# Response body ka size indicate kar sakta hai.

# Example:

# Content-Length: 1250



# Location

# Redirect ke case mein destination specify kar sakta hai.

# Example:

# Location: https://example.com/




# Set-Cookie

# Server browser ko cookie set karne ke liye bhej sakta hai.

# Example:

# Set-Cookie: session_id=abc123




#  8. Cookies Kya Hoti Hain?

# Cookie ko simple language mein:

# Browser mein stored small piece of data jo website/browser interaction ko maintain karne mein help karta hai.

# Example:

# Tum website par login karte ho.

# Without some mechanism, server ko har request par ye identify karna difficult hota ki:

# "Ye kaunsa logged-in user hai?"

# Cookie/session mechanism help kar sakta hai.

# Conceptually:

# Login
#   ↓
# Server
#   ↓
# Set-Cookie
#   ↓
# Browser stores cookie
#   ↓
# Next request
#   ↓
# Cookie sent
#   ↓
# Server identifies session




# 🔐 9. Cookies & Cybersecurity

# Cookies web security mein extremely important hain.

# Especially:

# Session cookies
# Authentication cookies
# Secure cookies
# HttpOnly cookies
# SameSite cookies

# Example security-related cookie attributes:

# Set-Cookie: session=abc123; Secure; HttpOnly; SameSite=Lax

# Abhi in attributes ko deeply memorize nahi karna hai.

# Bas concept samjho:

# Secure

# Cookie ko HTTPS connections ke saath restrict karne mein help karta hai.

# HttpOnly

# JavaScript se cookie access ko restrict karne mein help karta hai.

# SameSite

# Cross-site request scenarios mein cookie behavior control karne mein help karta hai.



# Ye concepts future web-security lessons mein kaam aayenge.







#  10. HTTPS Kya Hai?

# HTTPS = HTTP Secure

# HTTPS basically HTTP communication ko TLS ke through secure karta hai.



# Simple flow:


# HTTP:

# Browser
#    ↓
# Request
#    ↓
# Network
#    ↓
# Server




# HTTPS mein:

# Browser
#    ↓
# Encrypted TLS connection
#    ↓
# Network
#    ↓
# Server



# 11. HTTPS Kya Provide Karta Hai?

# High level par HTTPS/TLS important security properties provide karta hai:



#  Confidentiality

# Communication ko unauthorized observers ke liye readable hone se protect karta hai.


# Integrity

# Data ko transit mein tamper hone se detect/protect karne mein help karta hai.


#  Authentication

# TLS certificates ke through browser ko server identity verify karne mein help karta hai.

# Isliye:

# HTTP
# ❌ No TLS protection

# HTTPS
# ✅ HTTP + TLS protection






# 12. HTTP vs HTTPS

# HTTP	                                    HTTPS

# HTTP protocol	                            HTTP over TLS
# No TLS encryption	                        TLS protection
# Typically port 80	                        Typically port 443
# Less secure for sensitive traffic	        Secure transport for web traffic
# URL starts http://	                    URL starts https://

# Important: HTTPS ka matlab website automatically trustworthy nahi hai.

# A malicious/phishing website bhi HTTPS use kar sakti hai.

# HTTPS primarily connection security and server authentication provide karta hai; ye website ke intentions ko guarantee nahi karta.



#  13. Ab Real Website Inspect Karte Hain

# Ab theory khatam. Actual browser traffic dekhte hain.

# Chrome open karo.

# Press:

# F12

# Ya:

# Ctrl + Shift + I

# DevTools open ho jayega.



# Practice 1 — Network Tab

# DevTools mein:

# Network

# tab select karo.

# Phir page reload karo:

# Ctrl + R

# Ab bahut saari requests dikhegi.

# Tumhe columns mil sakte hain:

# Name
# Status
# Type
# Initiator
# Size
# Time



# 14. Homepage Request Find Karo

# Network tab mein page ki main document request find karo.

# Usually:

# Name → website domain
# Type → document

# Example:

# example.com
# Status → 200
# Type → document

# Us request par click karo.



# 15. Headers Dekho

# Request details mein:

# Headers

# tab open karo.

# Tumhe sections mil sakte hain:

# General
# Response Headers
# Request Headers




# General

# Yahan tumhe mil sakta hai:

# Request URL
# Request Method
# Status Code
# Remote Address
# Referrer Policy

# Example:

# Request Method: GET
# Status Code: 200 OK




# 16. Response Headers Find Karo

# Scroll karke:

# Response Headers

# find karo.

# Wahan se 3 headers note karo.

# For example:

# Content-Type: ...
# Content-Encoding: ...
# Cache-Control: ...

# Tumhare selected website par headers different ho sakte hain.

# Jo actual values tumhare browser mein hain wahi note karna.




#  Practice 2 — Cookie Find Karo

# Chrome DevTools mein:

# Application

# tab open karo.

# Left side mein:

# Storage
#    ↓
# Cookies

# Expand karo.

# Phir current website select karo.

# Tumhe columns dikh sakte hain:

# Name
# Value
# Domain
# Path
# Expires / Max-Age
# Size
# HttpOnly
# Secure
# SameSite



#  Important: Agar tum kisi logged-in website ki cookie dekh rahe ho, uska value yahan chat mein paste mat karna. Session/authentication cookies sensitive credentials ki tarah treat karo.




#  Day 20 Task

# Kisi normal website ki homepage inspect karo.

# Best practice: kisi public website ko use karo jahan tumhare private login/session data ki zarurat na ho.

# Notes mein ye information record karo:

# DAY 20 — HTTP & HTTPS

# Website:
# ____________________

# Request Method:
# ____________________

# Status Code:
# ____________________

# HTTPS Used:
# Yes / No

# Response Header 1:
# Name:
# Value:

# Response Header 2:
# Name:
# Value:

# Response Header 3:
# Name:
# Value:

# Cookie Found:
# Yes / No

# Cookie Name:
# ____________________

# What I Learned:
# 1.
# 2.
# 3.

# Cookie ka actual Value notes mein bhi mat likhna, especially agar woh session/authentication cookie ho.

# 17. HTTP/HTTPS + Cybersecurity

# Aage web security mein tumhe concepts milenge:

# HTTP Request
#      ↓
# Parameters
#      ↓
# Headers
#      ↓
# Cookies
#      ↓
# Authentication
#      ↓
# Web vulnerabilities

# For example, future mein tumhe:

# SQL Injection
# XSS
# CSRF
# Authentication vulnerabilities
# Session security
# Access control

# jaise concepts samajhne honge.

# In sabko samajhne ke liye pehle normal HTTP request/response samajhna zaroori hai.




#  Day 20 Revision

# Khud answer karo:

# Q1. HTTP ka full form kya hai?

# Q2. HTTP request kya hoti hai?

# Q3. HTTP response kya hoti hai?

# Q4. GET aur POST mein basic difference kya hai?

# Q5. 200 OK ka kya meaning hai?

# Q6. 404 ka kya meaning hai?

# Q7. 500 ka kya meaning hai?

# Q8. HTTP headers kya hote hain?

# Q9. Cookie kya hoti hai?

# Q10. HTTPS HTTP se kaise different hai?

# Q11. HTTPS mein TLS ka role kya hai?

# Q12. HTTPS hone ka matlab kya website automatically trustworthy hai?





# Quick Challenge

# Is flow ko explain karo:

# Browser
#    ↓
# GET /
#    ↓
# Web Server
#    ↓
# 200 OK
#    ↓
# HTML + Headers
#    ↓
# Browser

# Aur ye bhi:

# HTTP  → Port 80
# HTTPS → Port 443

# Question: HTTPS mein 443 port use karne ke alawa HTTP communication ko security kaise milti hai?




#  Day 20 Checklist

# ☐ HTTP understood
# ☐ Request/Response understood
# ☐ GET understood
# ☐ POST understood
# ☐ Status codes understood
# ☐ Headers understood
# ☐ Cookies understood
# ☐ HTTPS understood
# ☐ TLS high-level concept understood
# ☐ DevTools Network tab opened
# ☐ Real request inspected
# ☐ Status code recorded
# ☐ 3 response headers recorded
# ☐ HTTPS checked
# ☐ Cookie inspected
# ☐ Notes written
# ☐ Revision completed





#  Move Forward If...

# Tum bina notes dekhe ye explain kar sako:

# “Browser HTTP request bhejta hai, server HTTP response deta hai, status code result batata hai, headers additional information dete hain, cookies state/session maintain karne mein help karti hain, aur HTTPS HTTP communication ko TLS ke through secure karta hai.”

# Ab practical karo: DevTools → Network → page reload → homepage/document request par click karo.