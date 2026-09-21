# Day 7 Start — 
# 
# Python Mini-Project + Weekly Revision

# Aaj Day 7 hai, aur aaj tak jo Python concepts seekhe hain unko combine karke first complete cybersecurity-related mini-project banayenge: Password Strength Checker.

# Aaj ka Goal

# program:

# Password ki minimum length check karega → 8+
# Number check karega → 0–9
# Special character check karega → @, #, $, ! etc.
# Uppercase letter check karega → A-Z
# Password ko rate karega:
# ❌ Weak
# ⚠️ Medium
# ✅ Strong
# User baar-baar password test kar sakega.
# "exit" type karne par program band ho jayega.




def has_min_length(password):
    return len(password) >= 8


def has_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special_char(password):
    special_chars = "!@#$%^&*"

    for char in password:
        if char in special_chars:
            return True
    return False


def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def check_strength(password):
    score = 0

    if has_min_length(password):
        score += 1

    if has_number(password):
        score += 1

    if has_special_char(password):
        score += 1

    if has_uppercase(password):
        score += 1

    if score <= 1:
        return "Weak"

    elif score <= 3:
        return "Medium"

    else:
        return "Strong"


# Main Program

print("================================")
print("   PASSWORD STRENGTH CHECKER")
print("================================")

while True:

    password = input("\nEnter password (or type 'exit'): ")

    if password.lower() == "exit":
        print("\nProgram closed.")
        break

    print("\nChecking password...")

    # Individual checks
    length = has_min_length(password)
    number = has_number(password)
    special = has_special_char(password)
    uppercase = has_uppercase(password)

    print("\n--- Security Checks ---")

    print("Minimum Length (8+):", "PASS" if length else "FAIL")
    print("Number:             ", "PASS" if number else "FAIL")
    print("Special Character:  ", "PASS" if special else "FAIL")
    print("Uppercase Letter:   ", "PASS" if uppercase else "FAIL")

    # Final rating
    rating = check_strength(password)

    print("\nPassword Strength:", rating)









































