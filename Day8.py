# Day 8 — Linux Foundation

# Aaj se Week 2: Linux Foundation start karte hain. Aaj ka focus coding nahi, balki Linux + Terminal ki basic understanding hai.

# Today's Goal

# Aaj ke end tak tum:

# Linux kya hai samjhoge
# Windows/macOS aur Linux ka basic difference samjhoge
# Distro kya hota hai samjhoge
# Ubuntu, Debian, Kali Linux ka relation samjhoge
# Terminal/Shell ka concept samjhoge
# Linux terminal me basic commands run kar paoge




# 1. Operating System kya hota hai?

# Operating System (OS) woh software hai jo user aur computer hardware ke beech bridge ka kaam karta hai.
# Examples:
# Windows
# Linux
# macOS
# Android
# iOS
# Simple flow:

# You
#  ↓
# Operating System
#  ↓
# CPU / RAM / Storage / Network / Hardware



# Example

# Jab tum VS Code open karte ho:

# You → Windows → CPU/RAM → VS Code

# OS resources ko manage karta hai aur applications ko hardware ke saath communicate karne deta hai.




# 2. Linux kya hai?

# Linux ek open-source operating system kernel hai.

# Yahan ek important distinction hai:

# Linux = Kernel
# Ubuntu = Linux-based Distribution
# Kali Linux = Linux-based Distribution
# Debian = Linux-based Distribution

# Kernel operating system ka core part hota hai jo hardware aur software ke beech communication manage karta hai.




# 3. Windows vs Linux
# Windows                   	            Linux

# Microsoft develops it	                    Open-source ecosystem
# Mostly GUI-focused	                    GUI + Terminal
# Proprietary	                            Open-source
# .exe commonly used	                    Package managers commonly used
# Windows-specific environment	            Many distributions available
# Desktop users me very common	            Servers/development/security me heavily used

# Linux ka terminal cybersecurity me particularly important hai because many servers, labs and security tools Linux environments me commonly use hote hain.










# 4. Linux Distribution kya hoti hai?

# Linux kernel akela complete user-friendly operating system nahi hota.

# Different organizations/projects Linux kernel ke saath:

# software
# package managers
# desktop environments
# system utilities
# configuration tools

# combine karke different distributions (distros) banate hain.

# Common distros
# Linux
# │
# ├── Debian
# │   ├── Ubuntu
# │   └── Kali Linux
# │
# ├── Fedora
# │
# └── Arch Linux

# Ubuntu

# Beginner-friendly Linux distribution.

# Kali Linux

# Cybersecurity aur penetration-testing related tools ke liye specially designed distribution.

# Debian

# Stable aur widely used Linux distribution.

# Important: Kali Linux ko "hacking OS" samajhna incomplete hai. It is a Linux distribution that comes with many security-testing tools.





# 5. Cybersecurity me Linux important kyun hai?

# Cybersecurity me tum frequently kaam karoge:

# Terminal
#    ↓
# Files
#    ↓
# Processes
#    ↓
# Networking
#    ↓
# Permissions
#    ↓
# Logs
#    ↓
# Security Tools

# For example, future me tum commands use karoge:

# ls
# cd
# pwd
# cat
# grep
# chmod
# ps
# ip
# ssh

# Isliye terminal se comfortable hona important hai.



# 6. Terminal aur Shell kya hai?
# Terminal

# Terminal ek interface/application hai jahan tum commands type kar sakte ho.
# Example:
# user@ubuntu:~$

# Shell

# Shell woh program hai jo tumhari command ko interpret karke system ko execute karne ke liye deta hai.
# Common Linux shell:
# Bash
# Simple analogy:

# You
#  ↓
# Terminal
#  ↓
# Shell
#  ↓
# Linux
#  ↓
# Hardware / Files / Processes






# 7. Aaj Linux Environment Setup karo

# Tum Windows use kar rahe ho, isliye beginner ke liye WSL + Ubuntu convenient option hai.

# Windows PowerShell ko Administrator ke roop me open karke:

# wsl --install

# Phir system restart karne ko kahe to restart karo.

# Ubuntu setup hone ke baad Ubuntu open karo.

# Agar WSL already installed hai, check karo:

# wsl --status

# Aur installed distributions dekhne ke liye:

# wsl -l -v

# Agar tumhare system me Ubuntu/WSL already available hai, dobara installation ki zarurat nahi.







# 8. First Linux Commands 🐧

# Ubuntu terminal open karke ek-ek command run karo.

# Command 1 — whoami
# whoami

# Ye batata hai ki tum currently kis user account se logged in ho.

# Command 2 — date
# date

# Current date/time show karega.

# Command 3 — echo
# echo Hello

# Output:

# Hello

# Tum ye bhi try kar sakte ho:

# echo "Hello Everyone!"


# Command 4 — pwd
# pwd

# Print Working Directory

# Ye batata hai ki tum currently filesystem ke kis directory/location me ho.

# Example:

# /home/vishwajeet

# Command 5 — ls
# ls

# Current directory ke andar available files/folders show karta hai.



#  Practice: Invalid Command

# Ab jaan-bujhkar wrong command run karo:

# hello123

# Tumhe kuch is type ka error mil sakta hai:

# command not found
# Iska meaning?

# Shell ne hello123 ko ek command ke roop me execute karne ki koshish ki, lekin us naam ka executable command nahi mila.

# Error se darna nahi hai. Linux learning me errors read karna bhi skill hai.








