# Day 23 — CIA Triad

# Great, EveryOne. Day 22 ke baad ab Cybersecurity ka ek sabse important foundation concept start karte hain: CIA Triad.

# CIA = Confidentiality + Integrity + Availability

# Almost har cybersecurity control ko in 3 questions se evaluate kiya ja sakta hai:

# Kya data secret hai? → Confidentiality
# Kya data correct/unchanged hai? → Integrity
# Kya system/data available hai? → Availability



# 1. Confidentiality
# Meaning

# Confidentiality = information sirf authorized people/systems ko accessible honi chahiye.

# Simple words:

# "Who can see the data?"

# Example

# Tumhare email account mein private emails hain.

# Agar attacker tumhara password chura kar emails read kar leta hai:


# Confidentiality violated




# Security controls


# Confidentiality protect karne ke liye:

# Encryption
# Passwords
# Access control
# MFA
# Permissions

# Example:

# Password + MFA
#       ↓
# Unauthorized person blocked
#       ↓
# Confidentiality protected





# 2.  Integrity


# Meaning

# Integrity = data accurate, complete aur unauthorized modification se protected hona chahiye.

# Simple question:

# "Has the data been changed without authorization?"

# Example

# Maan lo college database mein:

# Original marks: 85

# Kisi unauthorized person ne database change karke:

# Modified marks: 95

# kar diye.


#  Integrity violated

# Data available ho sakta hai aur secret bhi ho sakta hai, but data incorrect/change ho gaya.

# Security controls

# Integrity ke liye:

# Hashing
# Digital signatures
# Access controls
# File integrity monitoring
# Audit logs






# 3.  Availability


# Meaning

# Availability = authorized users ko system/data jab zarurat ho tab available hona chahiye.

# Simple question:

# "Can authorized users access it when they need it?"

# Example

# Tumhari college website normally accessible hai:

# collegewebsite.com
#         ↓
# Server
#         ↓
# Website available 


# Agar server par DDoS attack ho aur website inaccessible ho jaye:

# Website
#    ↓
# Server overloaded
#    ↓
# Users cannot access
#    ↓
# Availability X




# CIA Triad ko ek simple example se samjho

# Maan lo tumhare paas ek important PDF hai.

# Confidentiality

# Sirf tum aur authorized person PDF dekh sakte hain.

# Who can see it?

# Integrity

# PDF ko kisi ne secretly modify nahi kiya.

#  Is it still original/correct?

# Availability

# Jab tumhe PDF chahiye, tum usse access kar sakte ho.

#  Can I access it when needed?



# CIA Triad Table

# Pillar	            Main Question	        Example Violation

# Confidentiality	    Who can see it?	        Hacker reads private emails
# Integrity	            Has it been changed?	Marks/database modified
# Availability	        Can I access it?	    DDoS takes website offline


# Easy memory trick:

#  C = Can others see it?
#  I = Is it still correct?
#  A = Am I able to access it?




#  Encryption aur CIA Triad

# Tumhare task mein specifically poocha gaya hai:

# Why does encryption mainly protect Confidentiality?

# Suppose tum ek message bhejte ho:

# HELLO VISHWAJEET

# Encryption ke baad:

# 8fA$x92K...

# Agar attacker encrypted data intercept bhi kare, without the proper key uske liye original message samajhna difficult hota hai.

# Therefore:

# Encryption → primarily Confidentiality 

# Lekin Integrity?

# Encryption alone ka main purpose integrity guarantee karna nahi hai.

# Modern cryptographic systems mein authenticated encryption (for example, AEAD) confidentiality ke saath integrity/authenticity protection bhi provide kar sakta hai.

# So remember:

# Encryption alone ≠ automatically integrity.





#  Practice 1 — Identify the CIA Violation

# Scenario A

# A hacker gains unauthorized access to a company's customer database and reads customers' private information.

# Which pillar?

# C / I / A?


# Scenario B

# An attacker changes the amount of a bank transaction from:

# ₹1,000

# to:

# ₹10,000

# Which pillar?

# C / I / A?



# Scenario C

# A hospital's computer system becomes unavailable because of a cyberattack, and staff cannot access patient records.

# Which pillar?

# C / I / A?



#  Practice 2 — Real-World Examples

# Tumhe 3 examples dene hain:

# 1. Confidentiality failure

# Example structure:

# Situation:
# What happened:
# Why Confidentiality was violated:



# 2. Integrity failure

# Situation:
# What happened:
# Why Integrity was violated:



# 3. Availability failure

# Situation:
# What happened:
# Why Availability was violated:




#  Main Day 23 Task

# Ab tum ek-ek short example likho:

# Confidentiality:
# ____________________________

# Integrity:
# ____________________________

# Availability:
# ____________________________

# Har example mein clearly explain karna hai ki CIA ka kaunsa pillar violate hua aur kyun.



#  Cybersecurity Connection

# Aage jab hum security controls padhenge, tum har control ko CIA ke saath connect kar sakoge.

# For example:



# Firewall
#    ↓
# Unauthorized traffic block
#    ↓
# C / I / A protection depending on use



# Backup
#    ↓
# Data recovery
#    ↓
# Availability



# Encryption
#    ↓
# Protect data from unauthorized reading
#    ↓
# Confidentiality



# Access Control
#    ↓
# Only authorized users
#    ↓
# Confidentiality + Integrity



# Isliye CIA Triad ko cybersecurity ka mental framework samjho.



# Day 23 Checklist


#  Confidentiality understood
#  Integrity understood
#  Availability understood
#  CIA difference understood
#  Encryption connection understood
#  3 scenarios classified
#  3 real-world examples written
#  Notes completed