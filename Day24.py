# Day 24 — Authentication & Authorization

# Everyone, welcome to Week 4 — Cybersecurity Foundation, Day 24!

# Aaj ka concept real-world cybersecurity mein bahut important hai. jaise apps, email accounts, banking apps aur websites mein authentication aur authorization dono use hote hain.



#  Today's Goal


# Aaj hum 4 important topics seekhenge:

# Authentication vs Authorization

# Passwords and MFA

# Sessions

# Principle of Least Privilege (PoLP)




# 1. Authentication — Who are you?

# Authentication ka matlab hai verify karna ki tum wahi user ho hone ka claim kar rahe ho.

# Example: Tum apne email account mein login karte ho.

# Email address enter kiya.
# Password enter kiya.
# System ne credentials verify kiye.
# Login successful.



# Yahan system verify kar raha hai: “Are you really this user?”

# Authentication
# Identity verify karna

# Who are you?

# Common authentication methods

# Password ya PIN
# OTP
# Authenticator app
# Fingerprint ya face recognition
# Security key






# 2. Authorization — What are you allowed to do?

# Authorization ka matlab hai decide karna ki authenticated user ko kaun-se resources ya actions ki permission hai.


# Example: 
# Tum college portal mein login kar chuke ho.
# Student apne marks dekh sakta hai.
# Teacher apni classes ke marks update kar sakta hai.
# Authorized administrator user accounts manage kar sakta hai.

# Login successful hone ka matlab ye nahi ki student teacher ya administrator ke saare actions kar sakta hai.


# Authorization
# Permissions check karna

# What can you do?

# Examples

# File read karne ki permission
# File edit karne ki permission
# Admin panel access
# Account delete karne ki permission


# Authentication vs Authorization

# Authentication                    # Authorization

# Identity verify karta hai         # Permissions decide/check karta hai
# Login se commonly associated      # Access control se associated
# “Who are you?”                    # “What can you do?”
# Example: password verify hua      # Example: user ko admin access nahi hai



# Yaad rakhna: Authentication pehle hota hai aur authorization aksar uske baad, lekin authorization checks har protected action par bhi hone chahiye.





# 3. Passwords and MFA
# Password kya hai?

# Password ek secret credential hai jo identity verify karne mein use hota hai. Agar password weak, reused ya stolen ho, to account risk mein aa sakta hai.


# Good practices:

# Har important account ke liye unique password.
# Long password ya passphrase.
# Password manager use karna.
# Kisi ke saath password share nahi karna.
# Unexpected login links par credentials enter na karna.



# MFA — Multi-Factor Authentication

# MFA ka matlab hai do ya zyada different categories of authentication factors use karna.

# Authentication ke 3 factor categories


# 1. Something you know
# Password, PIN


# 2. Something you have
# Authenticator app, security key, registered device


# 3. Something you are
# Fingerprint, face recognition




# For example:

# Password + Authenticator app code
#               ↓
#      Two different factors
#               ↓
#              MFA


# Password ke saath sirf do passwords use karna MFA nahi hai, kyunki dono same category ke factors hain.


# Practical task: Apne kisi important account—preferably email—par MFA enable karo, agar available hai aur abhi enabled nahi hai.

# Account ki official settings open karo.
# Security section mein jao.
# Two-step verification / 2FA / MFA option dekho.
# Authenticator app ya security key jaise available secure method ko configure karo.
# Recovery codes milen to unhe safely offline store karo.
# Apna password, OTP ya recovery codes yahan share mat karna.




# 4. Sessions — Login ke baad kya hota hai?

# Har webpage par baar-baar password enter karna inconvenient hoga. Isliye login ke baad website aksar session ya session token use karti hai, jisse subsequent requests ko authenticated user se associate kiya ja sake.


# 1. Login
# Credentials verify hote hain


# 2. Session established
# Browser ko session identifier/token mil sakta hai


# 3. Subsequent requests
# Server session/token validate karta hai


# Security connection

# Agar attacker valid session token chura le, to woh kuch cases mein password ke bina bhi user ki session impersonate kar sakta hai.

# Isliye:

# HTTPS use karo.
# Session tokens ko secret rakho.
# Public/shared computer par logout karo.
# Secure session cookies mein HttpOnly, Secure aur suitable SameSite settings use ki ja sakti hain.
# Logout aur session expiry ko properly implement karna important hai.

# Important: Session cookie ya authentication token kisi ke saath share mat karna.



# 5. Principle of Least Privilege (PoLP)

# Definition: Kisi user, application ya process ko sirf utni permissions dena jitni uske kaam ke liye zaroori hain—usse zyada nahi.

# Real-world analogy: Hotel keycard

# Maan lo tum hotel mein guest ho.

# Tumhara keycard tumhare room ko unlock karta hai.

# Lekin woh hotel manager ka office, security room aur cash vault unlock nahi karta.

# Kyun? Tumhe apne room ke liye access chahiye, poore hotel ke liye nahi.

# Yehi Principle of Least Privilege hai.

# Cybersecurity example

# Role                      # Appropriate access

# Student                   # Apne records dekhna
# Teacher                   # Assigned students ke marks manage karna
# Administrator             # Approved administrative tasks
# Ordinary application      # Sirf required files/resources access karna

# Least privilege se accidental damage, unauthorized changes aur compromised accounts ke impact ko reduce kiya ja sakta hai.



# Practice 1 — Quick Knowledge Check

# 1. A website checks whether your password is correct. What is this?

# Authentication
# Authorization
# Availability

# 2. A logged-in student tries to open an admin-only page. Which control decides whether access is allowed?

# Authentication
# Authorization
# Encryption

# 3. Password + authenticator-app code is an example of:

# Single-factor authentication
# Multi-factor authentication
# Authorization

# 4. A hotel guest's keycard opens only their assigned room. This illustrates:

# Least privilege
# Data integrity
# DNS resolution

# 5. What can happen if an attacker steals a valid session token?

# They may impersonate the logged-in user
# The token always becomes harmless
# The account automatically gets MFA




#  Practice 2 — Write your own answers

# Apni notebook mein ye complete karo:

# Authentication: Apne words mein one-sentence definition.

# Authorization: Apne words mein one-sentence definition.

# MFA: Phone ki un apps/accounts ki list banao jo MFA offer karte hain. Ek eligible account par MFA enable karo, agar already enabled nahi hai.

# Least privilege: Hotel keycard ke alawa ek real-world example likho.




# Day 24 Main Task

# Neeche diye scenario ko use karke ek short paragraph apne words mein likho:

# Ek student college portal mein successfully login karta hai. Woh apne marks dekh sakta hai, lekin doosre students ke marks edit nahi kar sakta. Portal ka session student ko baar-baar login karne se bachata hai.

# Paragraph mein explain karo:

# Authentication kahan hua?

# Authorization kahan hua?

# Login hone ke baad student ko har permission kyun nahi milti?

# Least privilege kaise apply hota hai?





#  End-of-Day Checklist

# Authentication vs Authorization understood
# Password security understood
# MFA factors understood
# Sessions understood
# Least privilege understood
# Quiz completed
# One account's MFA status checked
# Main task paragraph written
# Notes saved