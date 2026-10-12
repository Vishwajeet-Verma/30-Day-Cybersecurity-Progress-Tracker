# Day 26 — Security Controls

# Aaj hum Week 4 — Cybersecurity Foundation ka final learning day start kar rahe hain. Pichhle days mein tumne threats, CIA Triad, authentication, MFA aur common attacks seekhe. Ab dekhte hain ki organizations in attacks se protect hone ke liye kaun-se tools use karti hain.


#  Today's Goal
# Aaj tum 7 important security controls seekhoge:

# 1. Firewall
# 2. Antivirus
# 3. EDR — Endpoint Detection & Response
# 4. IDS / IPS — Intrusion Detection / Prevention System
# 5. WAF — Web Application Firewall
# 6. SIEM — Security Information & Event Management
# 7. VPN — Virtual Private Network

# Ek important baat: koi ek tool complete security provide nahi karta. Organizations multiple controls ko combine karti hain.






# 1. Firewall — Network traffic ka gatekeeper

# tutorialspoint.com

# Firewall incoming aur outgoing network traffic ko defined security rules ke according allow ya block karta hai.

# Example: Firewall kisi unauthorized connection ko block kar sakta hai.
# - Protects: Network access
# - Main role: Prevents / filters
# - CIA connection: Configuration ke according teeno properties ko support kar sakta hai.



# 2. Antivirus — Malicious software se protection

# fastsoftware.fr

# Antivirus malicious files aur programs ko known signatures, suspicious behavior aur other detection methods se identify karke block ya quarantine kar sakta hai.

# Example: Download ki hui infected file ko detect karna.
# - Main role: Prevents + detects
# - Related threat: Viruses, trojans aur other malware.




# 3. EDR — Endpoint Detection & Response

# kz.nwu.ua

# EDR laptops, desktops aur servers jaise endpoints ki activity monitor karta hai, suspicious behavior detect karta hai aur investigation/response mein help karta hai.

# Example: Suspicious process detect hone par security team device ko isolate kar sakti hai.
# - Main role: Detects + responds
# - Antivirus se difference: EDR generally deeper activity visibility, investigation aur response capabilities deta hai.





# 4. IDS / IPS — Intrusion Detection / Prevention System


# IDS — Intrusion Detection System
# Network traffic ya system activity mein suspicious patterns detect karke alert deta hai.
# Detects



# IPS — Intrusion Prevention System
# Suspicious traffic ko detect karke configured rules ke according automatically block kar sakta hai.
# Prevents + detects

# Easy trick: IDS = detect and alert. IPS = detect and potentially block.



# 5. WAF — Web Application Firewall

# openappsec.io


# WAF web application ke HTTP/HTTPS requests ko inspect karke malicious ya suspicious requests ko block karne mein help karta hai.

# Example: Properly configured WAF kuch common web attack patterns, jaise SQL injection attempts, ko block kar sakta hai.
# - Main role: Filters + prevents
# - Protects: Web applications and websites.
# - Important: WAF har vulnerability ko automatically fix nahi karta.



# 6. SIEM — Security Information & Event Management

# medium.com


# SIEM multiple systems se logs aur security events collect aur analyze karta hai, taaki suspicious patterns identify karke alerts generate kiye ja sakein.

# Example: SIEM detect karne mein help kar sakta hai ki ek account par bahut saare failed login attempts ho rahe hain.
# - Main role: Detects + supports investigation
# - Used by: Security Operations Center (SOC) analysts.

# - Examples: Microsoft Sentinel, Splunk Enterprise Security.

# SIEM khud har attack ko block nahi karta; automated response integrations ho sakti hain, lekin unki configuration alag se hoti hai.





# 7. VPN — Virtual Private Network

# yohomobile.com


# VPN tumhare device aur VPN server ke beech encrypted tunnel establish kar sakta hai, jisse connection par data protect hota hai..

# Example: Employee company VPN se connect karke authorized internal resources access karta hai.
# - Main role: Protects communication in transit
# - CIA connection: Primarily confidentiality; integrity protections bhi VPN protocol par depend kar sakti hain.

# - Important: VPN tumhe completely anonymous nahi banata aur phishing, malware ya unsafe downloads se automatically protect nahi karta.





#  Practice 1 — Apne machine ka firewall check karo

# Tum Ubuntu WSL use kar rahe ho, isliye hum Linux firewall status aur Windows Firewall status ko alag-alag check karenge. WSL ke results ko poore Windows computer ka firewall status mat samajhna.

# Step A: Ubuntu/WSL mein check karo

# Terminal mein:

# sudo ufw status


# Possible outputs:

# - Status: active — UFW enabled hai.
# - Status: inactive — UFW currently inactive hai; iska matlab automatically ye nahi ki machine bilkul unprotected hai.
# - ufw: command not found — UFW installed nahi hai.


# Agar UFW available nahi hai, to abhi install ya firewall rules change karne ki zarurat nahi.



# Step B: Windows Firewall check karo

# Windows mein PowerShell open karo aur ye command run karo:


# Get-NetFirewallProfile |
# Select-Object Name, Enabled


# Example output:

# Name     Enabled
# ----     -------
# Domain      True
# Private     True
# Public      True



# - True = us profile ka Windows Firewall enabled hai.
# - False = us profile ka Windows Firewall disabled hai.

# Ye sirf status check hai; koi setting change nahi hoti. Agar college-managed computer hai, to firewall disable mat karna aur policies ko modify mat karna.




#  Practice 2 — Controls ko group karo

# Ek security control multiple categories mein fit ho sakta hai. Ye beginner-level grouping hai; actual behavior configuration par depend karta hai.


# Firewall                          # Prevents / filters


# Antivirus                         # Prevents / filters # Detects                           
# # EDR                             # Detects # Responds
# IDS                               # Detects
# IPS                               # Prevents / filters # Detects 
# WAF                               # Prevents / filters # Detects
# SIEM                              # Detects # Responds
# VPN                               # Prevents / filters



# VPN ko yahan broad sense mein protective control maana gaya hai, kyunki encrypted tunnel communication ko protect karta hai. Ye typical network firewall jaisa traffic-filtering tool nahi hai.



#  Practice 3 — Security Control Glossary

# Apni notes file mein ye 7 entries likho:

# Control	        One-sentence explanation

# Firewall	        Network traffic ko security rules ke according allow ya block karta hai.
# Antivirus	        Malware ko detect, block ya quarantine karne mein help karta hai.
# EDR	            Endpoints ki suspicious activity detect karke investigation aur response mein help karta hai.
# IDS / IPS	        IDS suspicious activity par alert karta hai, jabki IPS traffic ko automatically block bhi kar sakta hai.
# WAF	            Web application requests ko inspect karke malicious requests filter karta hai.
# SIEM	            Logs aur security events ko analyze karke suspicious activity par alerts generate karta hai.
# VPN	            Device aur VPN server ke beech encrypted connection establish kar sakta hai.




# Day 26 ka Cybersecurity Connection

# Ek organization ke network ko imagine karo:

# Internet
#     ↓
# Firewall / IPS
# Network traffic filter
#     ↓
# WAF → Web application
# Web requests inspect aur filter



# Endpoint protection: Antivirus + EDR
# Devices par detection aur response
#               ↓
#              SIEM
# Logs, alerts aur security investigation


# Ye conceptual diagram hai, har organization ka exact setup aisa hi ho zaroori nahi.




#  Weekly Review — Week 4

# Aaj tumhare liye Week 4 ke quick-test answers bhi revise kar lete hain.


# 1. Vulnerability vs Risk: Vulnerability weakness hai; risk us weakness se potential harm hone ki likelihood aur impact se related hai.
# 2. CIA Triad: Confidentiality, Integrity, Availability.
# 3. Authentication vs Authorization: Identity verify karna vs permissions check karna.
# 4. Three common attacks: Phishing, malware, DoS. Other examples: MITM, brute force, social engineering.
# 5. Firewall: Network traffic ko defined rules ke according filter karta hai.
# 6. MFA: Password ke alawa ek ya zyada additional, different authentication factor categories add karta hai.
# 7. Least privilege: Sirf required minimum permissions dena.


# Practical Challenge

# Apne kisi daily-use account, jaise email, ko choose karo aur notes mein likho:

# - HTTPS use hota hai ya nahi?
# - MFA option enabled hai ya nahi?
# - Session timeout ya logout option hai?
# - Kaun-se security controls likely use ho rahe hain?
# - CIA Triad ka kaunsa pillar us account ke liye sabse important hai, aur kyun?
# Kisi bhi password, OTP, recovery code ya session cookie ko notes mein mat likhna.



#  Day 26 Checklist

# [ ] Firewall status checked in WSL
# [ ] Windows Firewall status checked
# [ ] 7 security controls explained
# [ ] Prevents / detects / responds grouping completed
# [ ] Security glossary written
# [ ] Week 4 quick test revised
# [ ] Practical challenge completed