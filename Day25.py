# Day 25 — Common Cyberattacks: Conceptual Overview


# Aaj hum Week 4 ke next important topic par hain. Pichhle lessons mein tumne CIA Triad, Authentication, Authorization, MFA aur Least Privilege seekha. Ab samjhenge ki attackers commonly kaun-se methods use karte hain aur unse protection kaise ki jaati hai.

# Today's goal: 6 common attack types ko identify karna, unke warning signs samajhna aur har attack ke liye ek realistic defense batana. Aaj koi attack execute nahi karenge.


# 1. Phishing 

# Meaning: Phishing mein attacker fake email, message, website ya login page ke through kisi ko sensitive information reveal karne ya unsafe action lene ke liye trick karta hai.

# Example: Suspicious email

# Subject: URGENT! Your account will be blocked
# Your account will be suspended in 10 minutes. Click this link immediately to verify your password.

# Warning signs:
# - Urgent threats or pressure
# - Unexpected login or password request
# - Suspicious sender address or mismatched link
# - Unexpected attachment

#   Defense: Email filtering, verify the sender independently, and never enter credentials through suspicious links.

# Yaad rakho: Professional-looking email ya HTTPS lock icon hone se website automatically legitimate nahi ho jaati.



# 2. Brute Force / Password Attacks 

# Meaning: Password attack mein attacker passwords guess karne, leaked credentials reuse karne, ya password weakness ka fayda uthane ki koshish karta hai.

# Common concepts:
# - Brute force: Bahut saare possible password combinations try karna.
# - Credential stuffing: Pehle se leaked username-password combinations ko doosri services par try karna.
# - Password spraying: Bahut se accounts par kuch common passwords try karna.
# Defense: Unique, long passwords; MFA; login rate limiting; suspicious-login detection; aur breached passwords ko block karna.

# MFA kaise help karta hai?

# Agar attacker password jaan bhi leta hai, to MFA ka additional factor unauthorized login ko rokne mein help kar sakta hai. Lekin MFA har attack ke khilaaf perfect protection nahi hai—phishing-resistant security keys/passkeys aur bhi strong protection de sakte hain.



# 3. Malware 
# Meaning: Malware malicious software hai jo data chura sakta hai, files damage kar sakta hai, activity spy kar sakta hai ya system ko control karne ki koshish kar sakta hai.

# Common types:

# - Virus: Files/programs se attach hokar spread kar sakta hai.
# - Trojan: Legitimate software jaisa dikhkar malicious activity karta hai.
# - Ransomware: Files encrypt karke unhe inaccessible kar sakta hai aur ransom demand kar sakta hai.
# - Spyware: User ki activity ya information secretly collect kar sakta hai.
# Defense: Software updates, trusted downloads, endpoint protection, standard-user permissions aur offline/isolated backups.


# 4. Social Engineering 

# Meaning: Social engineering mein attacker technology ke bajay ya technology ke saath-saath human trust, fear, curiosity ya authority ka misuse karke kisi ko action lene ke liye manipulate karta hai.

# Example: Koi person khud ko IT support batakar phone karta hai aur tumse OTP ya password maangta hai.
# Defense: Identity ko independent channel se verify karo. OTP, password ya recovery code kisi caller ko mat batao—even if they claim to be an administrator.
# Phishing vs Social Engineering: Social engineering broader category hai. Phishing uska ek common form hai.


# 5. Denial of Service (DoS) 
# Meaning: DoS attack ka aim service ko legitimate users ke liye unavailable ya difficult to access banana hota hai, usually system ki limited resources ko overwhelm karke.


# DoS vs DDoS:
# - DoS: Attack traffic ek source ya limited source setup se aa sakta hai.
# - DDoS: Distributed Denial of Service mein multiple systems/sources se traffic aata hai.

# Example: College admission website overload hone ki wajah se genuine students form submit nahi kar paate.

# Defense: Traffic monitoring, rate limiting, DDoS protection services, traffic filtering aur resilient infrastructure.
# CIA connection: DoS primarily Availability ko affect karta hai.




# 6. Man-in-the-Middle (MITM) 

# Meaning: MITM attack mein attacker do communicating parties ke beech communication ko intercept karne ya, circumstances ke hisaab se, alter karne ki koshish karta hai.

# You
# Message bhejte ho
#       ↓
# Potential attacker
# Communication intercept/alter karne ki koshish
#       ↓
# Website / recipient


# Example: Public Wi-Fi par attacker insecure communication ko intercept karne ki koshish karta hai.
 
# Defense: HTTPS/TLS, certificate warnings ko ignore na karna, trusted networks, updated devices aur sensitive activity ke liye appropriate secure connections.
# HTTPS interception ko difficult banata hai, lekin compromised device, malicious certificates ya other weaknesses ke cases mein risk completely eliminate nahi hota.



# 7. Six attacks — quick revision table

# Attack    	                    Plain-English meaning	                            One realistic defense

# Phishing	                        Fake messages se trick karna	                    Sender/link verify karna
# Brute force/password attacks	    Password guess ya stolen credentials use karna	    Unique passwords + MFA + rate limiting
# Malware	                        Harmful software se system/data ko affect karna	    Updates + endpoint protection
# Social engineering	            Human trust/manipulation ka misuse	                Identity independently verify karna
# DoS/DDoS	                        Service ko unavailable karne ki koshish	            DDoS mitigation + traffic filtering
# MITM	                            Communication intercept ya alter karne ki koshish	HTTPS/TLS + certificate validation




#  Practice 1 — Match the attack type

# 1. You receive a fake email asking you to verify your password urgently.

# Malware

# Phishing

# DoS



# 2. Someone tries many password combinations to access an account.

# MITM

# Social engineering

# Brute force / password attack



# 3. A malicious program encrypts your files and demands payment.

# Malware

# Phishing

# MITM



# 4. A caller pretends to be your college administrator and asks for your OTP.

# DoS

# Social engineering

# Malware



# 5. A website becomes unavailable because its capacity is overwhelmed by attack traffic.

# MITM

# DoS

# Credential stuffing



# 6. An attacker attempts to intercept communication between your device and a website.

# Phishing

# MITM

# Brute force / password attack





# Practice 2 — Analyze a suspicious email


# Imagine tumhe ye email milta hai:
# Subject: Your college account will be permanently deleted!
# Dear Student, your account will be closed in 15 minutes. Click the link and enter your password and OTP immediately to restore access.

# Apne answers likho:
# 1. Kaun-se warning signs suspicious hain?
# 2. Ye kaun-sa attack ho sakta hai?
# 3. Tumhara safest next step kya hoga?

# Hint: Urgency, password/OTP demand aur unexpected link par focus karo.



# Day 25 Main Task — Create your attack-defense table

# Apni notes file mein ye table banao. Har row ke defense ko apne words mein explain karna.

# Attack Name	                    One-sentence description	                                One defense

# Phishing	                        Fake messages se sensitive information lene ki koshish	    Sender verify karna
# Brute force/password attacks	    Password guess ya stolen credentials ka misuse	            MFA and rate limiting
# Malware	                        Harmful software se system ko affect karna	                Updates and endpoint protection
# Social engineering	            Trust ya emotions manipulate karna	                        Independent identity verification
# DoS	                            Service ko unavailable karna	                            Traffic filtering
# MITM	                            Communication intercept/alter karna	                        HTTPS/TLS and certificate validation




# Cybersecurity Connection

# Aaj ke attacks ko CIA Triad ke saath connect karo:

# - Confidentiality: Phishing, credential theft, spyware aur MITM.
# - Integrity: Unauthorized data modification, including some MITM scenarios or malware incidents.
# - Availability: DoS/DDoS aur ransomware.

# Ek attack multiple pillars ko affect kar sakta hai. For example, ransomware files ko unavailable kar sakta hai aur data theft ke saath ho to confidentiality bhi affect ho sakti hai.


#  Day 25 Checklist

# - [ ] All 6 attack types understood
# - [ ] Attack-defense table completed
# - [ ] Phishing warning signs identified
# - [ ] MFA protection concept understood
# - [ ] CIA Triad connection understood
# - [ ] Notes saved