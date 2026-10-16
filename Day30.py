# Day 30 — Final Review + Mini Project + Next Steps 

# Aaj tumhare 30-Day Cybersecurity Starter Roadmap ka final day hai. Is din hum Python, Linux, Networking aur Cybersecurity ki learning ko ek combined project mein use karenge.

# Aaj ka main goal hai ek working Python tool banana jo system information collect kare, network checks kare aur ek text-based security report generate kare.


# Part 1 — Full Revision (20–25 minutes)

# Project start karne se pehle apne Day 1–29 ke notes revise karo.

# Python
# Variables, data types, conditions, loops, functions, file handling, exceptions, subprocess aur socket.

# Linux
# Navigation, files, permissions, processes, ip a, grep, ss aur basic networking commands.

# Networking
# IP addresses, ports, TCP/UDP, DNS, HTTP/HTTPS, requests, responses aur headers.

# Cybersecurity
# CIA Triad, threat, vulnerability, risk, authentication, authorization, XSS, injection aur security controls.



# Part 2 — Mini Project: Basic Security & System Information Toolkit
# cybrary.it


# Project 3 — Cybersecurity Starter Toolkit
# Language: Python · Environment: Ubuntu/WSL · Output: Terminal + text report


# Is tool ke 6 features honge:

# 1. System hostname, username aur operating system show karega.
# 2. IP address information display karega.
# 3. Internet connectivity ke liye ping check karega.
# 4. User ke diye domain ka DNS lookup karega.
# 5. Sirf apne localhost par selected common TCP ports check karega.
# 6. Results ko security_report.txt mein save karega.

# Yeh basic diagnostic tool hai, full security scanner nahi. Port check sirf tumhari apni machine (127.0.0.1) par chalega. Python ke standard library modules use karenge, isliye extra packages install karne ki zaroorat nahi honi chahiye.


# Step 1 — Ubuntu/WSL mein project folder banao
# Apna Ubuntu terminal open karo aur ye commands ek-ek karke run karo:

# mkdir -p ~/cybersecurity-starter-toolkit

# cd ~/cybersecurity-starter-toolkit
# python3 --version


# Ab project file create karo:
# nano security_toolkit.py


# Step 2 — Complete Python code

# Neeche ka code copy karke nano editor mein paste karo.


# import getpass
# import platform
# import socket
# import subprocess
# from datetime import datetime

# REPORT_FILE = "security_report.txt"

# # Selected TCP ports checked on this computer only
# LOCAL_PORTS = [22, 53, 80, 443, 3000, 5000, 8000, 8080]


# def get_system_info():
#     """Collect basic system information."""
#     info = [
#         f"Hostname: {socket.gethostname()}",
#         f"Username: {getpass.getuser()}",
#         f"Operating System: {platform.system()} {platform.release()}",
#         f"Python Version: {platform.python_version()}",
#     ]
#     return info


# def get_ip_info():
#     """Display IP addresses from the local network interfaces."""
#     try:
#         result = subprocess.run(
#             ["ip", "-brief", "address"],
#             capture_output=True,
#             text=True,
#             timeout=5,
#             check=False,
#         )

#         if result.returncode == 0 and result.stdout.strip():
#             return result.stdout.strip()

#         return "Could not retrieve interface details."
#     except (FileNotFoundError, subprocess.TimeoutExpired):
#         return "The 'ip' command is unavailable or timed out."


# def check_connectivity():
#     """Check connectivity to a fixed public IP using one ping."""
#     try:
#         result = subprocess.run(
#             ["ping", "-c", "1", "-W", "2", "1.1.1.1"],
#             capture_output=True,
#             text=True,
#             timeout=4,
#             check=False,
#         )

#         if result.returncode == 0:
#             return "Reachable (ping succeeded)."

#         return "Ping failed; connectivity may be unavailable or ICMP may be blocked."
#     except (FileNotFoundError, subprocess.TimeoutExpired):
#         return "Ping command unavailable or timed out."


# def dns_lookup(domain):
#     """Resolve a user-entered domain name."""
#     domain = domain.strip().rstrip(".")

#     if not domain or len(domain) > 253:
#         return "Invalid or empty domain."

#     if any(not (char.isalnum() or char in ".-") for char in domain):
#         return "Invalid domain format."

#     try:
#         results = socket.getaddrinfo(
#             domain, None, type=socket.SOCK_STREAM
#         )
#         addresses = sorted({item[4][0] for item in results})

#         if addresses:
#             return "\n".join(addresses)

#         return "No addresses returned."
#     except socket.gaierror:
#         return "DNS lookup failed; check the domain or DNS connectivity."


# def check_local_ports():
#     """Check selected TCP ports on localhost only."""
#     results = []

#     for port in LOCAL_PORTS:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(0.5)

#         try:
#             status = sock.connect_ex(("127.0.0.1", port))
#             if status == 0:
#                 results.append(f"127.0.0.1:{port} - OPEN")
#             else:
#                 results.append(f"127.0.0.1:{port} - NOT OPEN")
#         except OSError:
#             results.append(f"127.0.0.1:{port} - CHECK FAILED")
#         finally:
#             sock.close()

#     return "\n".join(results)


# def generate_report(domain):
#     """Run checks and save the results to a text report."""
#     report = [
#         "=" * 48,
#         "BASIC SECURITY & SYSTEM INFORMATION REPORT",
#         "=" * 48,
#         f"Generated: {datetime.now().astimezone().isoformat()}",
#         "",
#         "[1] SYSTEM INFORMATION",
#         *get_system_info(),
#         "",
#         "[2] IP ADDRESS INFORMATION",
#         get_ip_info(),
#         "",
#         "[3] INTERNET CONNECTIVITY",
#         check_connectivity(),
#         "",
#         f"[4] DNS LOOKUP: {domain}",
#         dns_lookup(domain),
#         "",
#         "[5] SELECTED LOCALHOST TCP PORTS",
#         check_local_ports(),
#         "",
#         "NOTES:",
#         "- This is a basic diagnostic report, not a full security audit.",
#         "- Only selected TCP ports on 127.0.0.1 were checked.",
#         "- A port reported NOT OPEN may be closed or filtered.",
#         "- Ping failure alone does not prove the internet is unavailable.",
#         "=" * 48,
#     ]

#     report_text = "\n".join(report)

#     print("\n" + report_text)

#     try:
#         with open(REPORT_FILE, "w", encoding="utf-8") as file:
#             file.write(report_text + "\n")
#         print(f"\nReport saved to: {REPORT_FILE}")
#     except OSError as error:
#         print(f"\nCould not save report: {error}")


# def main():
#     print("Cybersecurity Starter Toolkit")
#     print("-" * 30)

#     domain = input("Enter a domain for DNS lookup (e.g. example.com): ")
#     generate_report(domain)


# if __name__ == "__main__":
#     main()





# Step 3 — Save aur run karo

# nano editor mein:

# 1. Ctrl + O dabao.
# 2. Enter dabao.
# 3. Ctrl + X dabao.

# Phir terminal mein run karo:
# python3 security_toolkit.py


# Domain prompt par example.com enter karke Enter dabao. DNS lookup ke liye internet/DNS available hona chahiye.


# Step 4 — Expected output
# Tumhare computer ke results alag honge. Output ka format roughly aisa dikhega:

# Cybersecurity Starter Toolkit
# ------------------------------
# Enter a domain for DNS lookup (e.g. example.com): example.com

# ================================================
# BASIC SECURITY & SYSTEM INFORMATION REPORT
# ================================================
# [1] SYSTEM INFORMATION
# Hostname: MCAL532
# Username: vishwajeet
# Operating System: Linux ...

# [2] IP ADDRESS INFORMATION
# lo               UNKNOWN 127.0.0.1/8 ::1/128
# eth0             UP      ...

# [3] INTERNET CONNECTIVITY
# Reachable (ping succeeded).

# [4] DNS LOOKUP: example.com
# 93.184.216.34

# [5] SELECTED LOCALHOST TCP PORTS
# 127.0.0.1:22 - NOT OPEN
# 127.0.0.1:53 - NOT OPEN
# ...

# Report saved to: security_report.txt


# Yeh illustrative output hai, tumhare actual IPs, DNS addresses aur port status ki guarantee nahi.



# Step 5 — Report verify karo
# cat security_report.txt


# Phir files check karo:
# ls -l


# Expected files:
# security_toolkit.py
# security_report.txt


# Part 3 — GitHub par project upload karo

# Step 1: GitHub repository create karo

# 1. Create a new GitHub repository open karo.
# 2. Repository name rakho: cybersecurity-starter-toolkit
# 3. Description: A beginner-friendly Python toolkit for system and network diagnostics.
# 4. Public ya Private choose karo. Public repo mein personal details ya sensitive reports upload mat karna.
# 5. Add a README ko abhi unchecked rakh sakte ho, kyunki hum terminal se files upload karenge.
# 6. Create repository click karo.

# Step 2: README file banao
# Terminal mein:
# nano README.md


# Yeh content paste karo:
######################################################################################

# # Cybersecurity Starter Toolkit

# A beginner-friendly Python command-line project built during my
# 30-Day Cybersecurity Starter Roadmap.

# ## Features

# - Displays hostname, username, OS and Python version.
# - Displays IP address information using Linux networking tools.
# - Checks basic internet reachability using ping.
# - Performs a DNS lookup for a user-provided domain.
# - Checks selected TCP ports on localhost only.
# - Generates a text-based security report.

# ## Requirements

# - Python 3
# - Linux or Ubuntu/WSL
# - The `ip` and `ping` commands for their respective checks

# No third-party Python packages are required.

# ## How to Run

# ```bash
# python3 security_toolkit.py
# ```

# Enter a domain when prompted. The report is saved as
# `security_report.txt` in the current directory.

# ## Security Scope

# This is an educational diagnostic tool, not a complete security audit.
# Port checks are restricted to the local computer (`127.0.0.1`).
# A failed ping or a port marked NOT OPEN is not definitive proof
# of an outage or a particular security state.

# ## What I Learned

# - Python functions, exception handling and file operations.
# - Using subprocess to run basic Linux commands.
# - Using sockets for DNS resolution and TCP connection checks.
# - Understanding IP addresses, ports and connectivity.
# - Organizing diagnostic results into a text report.

# ## Project

# Part of my 30-Day Cybersecurity Starter Roadmap.

###########################################################################


# Save: Ctrl + O → Enter → Ctrl + X.



# Step 3: Upload files

# Pehle check karo ki Git installed hai:
# git --version


# Agar Git installed hai aur tum is folder mein ho, toh:

# git init
# git add security_toolkit.py README.md
# git commit -m "Add cybersecurity starter toolkit"
# git branch -M main
# git remote add origin https://github.com/YOUR-USERNAME/cybersecurity-starter-toolkit.git
# git push -u origin main


# YOUR-USERNAME ki jagah apna actual GitHub username use karna. Agar Git identity set nahi hai, toh commit se pehle Git tumhara name/email maang sakta hai. git remote add origin par remote pehle se configured hone ka error aaye, toh command blindly repeat mat karna—git remote -v se check karo.


# Important: security_report.txt ko upload karna optional hai. Report mein tumhara username, hostname aur local network details ho sakte hain, isliye public repo mein upload karne se pehle review karo. Is project mein secrets nahi hone chahiye.


# Step 4: Screenshot add karo

# - Toolkit ke successful run ka terminal screenshot lo.
# - Personal information aur internal IP details ko zaroorat ke mutabik hide karo.
# - Screenshot ko screenshots/ folder mein rakh sakte ho aur README mein add kar sakte ho.





# Day 30 — Final checklist

# [ ] Revision completed
# Day 1–29 ke notes revise kiye.

# [ ] Final project working
# Toolkit run hua aur security_report.txt generate hui.

# [ ] GitHub repo created and populated
# Python source aur README repository mein upload kiye.

# [ ] Self-assessment completed
# Skills rate kiye aur Month 2 ka focus choose kiya.

