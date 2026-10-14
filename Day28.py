# Day 28 — OWASP Top 10 Introduction 

# Aaj hum web security ki 5 important vulnerabilities samjhenge: Broken Access Control, Injection, Cross-Site Scripting (XSS), Authentication Failures aur Security Misconfiguration.


# Tumhara goal abhi exploitation seekhna nahi hai. Goal hai vulnerability ko pehchanna, uska root cause samajhna aur yeh explain kar pana ki developer use kaise prevent kar sakta hai.



# 1. OWASP Top 10 kya hai?

# OWASP ka full form hai Open Worldwide Application Security Project. Yeh web application security improve karne ke liye resources, guidance aur standards provide karta hai.

# OWASP Top 10 web application ki major security risks ko samajhne ke liye ek awareness document hai. Yeh har possible vulnerability ki complete list nahi hai.


# 2. Aaj ki 5 vulnerabilities



#   1. Broken Access Control

# Jab application user ko aisa data ya action access karne deti hai jiske liye uske paas permission nahi hai.

# Example: Ek normal user admin dashboard access kar leta hai.

# Prevention: Har sensitive request par server-side authorization check.




# 2. Injection (SQL Injection, etc.)

# Jab untrusted input ko galti se executable command ya query ka hissa bana diya jata hai.

# Example: Search field ka input database query ka meaning badal deta hai.

# Prevention: Parameterized queries, safe APIs aur input validation.




# 3. Cross-Site Scripting (XSS)

# Jab attacker ka diya hua harmful script kisi doosre user ke browser mein website ke context mein execute ho jata hai.

# Example: Unsafe comment display karne par browser uske andar ka script execute kar deta hai.

# Prevention: Context-appropriate output encoding, safe rendering aur zaroorat par sanitization.





# 4. Authentication Failures

# Jab login, identity verification ya session management mein weaknesses ki wajah se kisi aur ki identity mein access mil sakta hai.

# Example: Weak password protections ya stolen session ka misuse.

# Prevention: MFA, secure session handling, rate limiting aur safe account recovery.





# 5. Security Misconfiguration

# Jab server, application ya cloud ki settings unsafe ya unnecessarily exposed hoti hain.

# Example: Production website par debug mode enabled reh jana.

# Prevention: Secure defaults, unnecessary services disable karna aur regular configuration reviews.



# Yaad rakho: upar diye examples conceptual hain. Har case mein actual risk application ke design aur configuration par depend karta hai.




# 3. Real breach example — TalkTalk, UK (2015)

# news.sky.com

# Case study: TalkTalk data breach

# UK telecommunications provider TalkTalk suffered a cyberattack in October 2015. The UK Information Commissioner's Office (ICO) found that attackers exploited SQL injection vulnerabilities in webpages to access an underlying database containing customer information. Personal details of 156,959 customers were accessed, including bank account numbers and sort codes for 15,656 customers. The investigation also identified outdated database software and inadequate monitoring. 

# Source: ICO — How the TalkTalk investigation unfolded

# Practice summary (apne words mein):

# “TalkTalk ke 2015 breach mein attackers ne SQL injection vulnerability ka fayda uthaya aur customers ka personal data access kiya. Investigation mein outdated database software aur security monitoring ki kami bhi saamne aayi. Is case se seekh milti hai ki user input ko safely handle karna, software updates lagana aur suspicious activity monitor karna bahut zaroori hai.”


# 4. “Never trust user input” kyun kehte hain?

# User input sirf form mein type kiya gaya text nahi hota. Yeh URL parameters, search queries, comments, uploaded files, API requests aur cookies se bhi aa sakta hai.

# Example: agar website comment ko plain text ki jagah unsafe HTML ke roop mein render karti hai, toh attacker ka input browser mein script execute karwa sakta hai — yeh XSS ka example hai.

# Secure application ko:

# - Input ka expected format validate karna chahiye.
# - Database queries mein parameterized queries use karni chahiye.
# - Browser mein output ko uske context ke hisaab se safely encode/render karna chahiye.
# - Server-side permissions aur business rules enforce karne chahiye.

# Important: Sirf input validation karna har vulnerability ko prevent nahi karta. Har layer par appropriate security controls chahiye.




# 5. Day 28 Task — XSS par short note

# Yeh 4-sentence note apni notebook mein likh sakte ho. Isse samajhkar apne words mein bhi likhne ki practice karna.

# Cross-Site Scripting (XSS)

# Cross-Site Scripting (XSS) is a web security vulnerability in which untrusted content causes malicious JavaScript to execute in another user's browser within a website's context. It can allow attackers to interfere with a user's interaction with a website, access data available to scripts, or perform unwanted actions as the user. XSS commonly occurs when an application handles and displays user-controlled content unsafely. Developers can reduce this risk by using safe rendering methods, context-appropriate output encoding, and sanitization when required.



# OWASP update: Official OWASP Top 10:2025 mein XSS ko separate top-level category ke roop mein list nahi kiya gaya; ise A05:2025 — Injection ke under include kiya gaya hai. Tumhare Day 28 curriculum mein XSS ko separately padhna phir bhi useful hai. 


# Reference: Official OWASP Top 10:2025.


# 6. Day 28 — Final checklist

# Your Day 28 Progress

# [ ] Concept understood
# 5 vulnerabilities aur unke root causes samajh liye.

# [ ] Practice completed
# Har vulnerability ki one-sentence explanation likhi.

# [ ] Real breach researched
# TalkTalk breach ka summary apne words mein likha.

# [ ] User input explained
# Explain kiya ki user input ko safely validate aur handle karna kyun zaroori hai.

# [ ] Task completed
# XSS par 3–5 sentences ka note likha.

# [ ] Notes written
# Prevention methods aur important definitions note ki.




# 7. Quick revision quiz

# 1. Broken Access Control ka example kya hai?

# Normal user admin data access kar le
# Website slow load ho
# Image load na ho



# 2. SQL Injection ka root cause kya ho sakta hai?

# Unsafe database query construction
# Strong MFA
# Regular software updates



# 3. XSS mein script kahan execute hota hai?

# User ke browser mein
# Sirf router mein
# Sirf database mein



# 4. Authentication ka main purpose kya hai?

# Identity verify karna
# Website ka color badalna
# Database backup karna



# 5. Production mein debug mode unnecessarily enabled rehna kis category ka example hai?

# Security Misconfiguration
# Broken Access Control
# XSS



# Move Forward If… Tum apne words mein SQL Injection aur XSS ka difference explain kar sako, aur bata sako ki inhe prevent karne ke liye developers ko kya karna chahiye. Kal Day 29 mein web security ko safe, defensive practice ke through aage badhayenge.