# Day 1 of Project - Password Strength Checker

# Requirement for Password Checker

# Minimum password length: 8 characters
# Uppercase and lowercase letters required for stronger ratings
# At least one number required
# At least one special character required
# Strength categories defined: Weak, Medium, Strong



from getpass import getpass


def has_min_length(password):
    return len(password) >= 8


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_number(password):
    return any(char.isdigit() for char in password)


def has_special_character(password):
    return any(
        not char.isalnum() and not char.isspace()
        for char in password
    )


def validate_password(password):
    return {
        "minimum_length": has_min_length(password),
        "uppercase": has_uppercase(password),
        "lowercase": has_lowercase(password),
        "number": has_number(password),
        "special_character": has_special_character(password),
    }


def get_password_strength(results):
    passed = sum(results.values())

    if not results["minimum_length"]:
        return "Weak"

    if passed == 5:
        return "Strong"

    if passed >= 3:
        return "Medium"

    return "Weak"


if __name__ == "__main__":
    password = getpass("Enter a test password: ")

    results = validate_password(password)
    strength = get_password_strength(results)

    print("\n--- Password Validation Results ---\n")

    print(f"Your Entered Password is: {password}\n")

    for check, passed in results.items():
        print(f"{check}: {'PASS' if passed else 'FAIL'}")



    print(f"\nPassword Strength: {strength}\n")

    # Never print or log the actual password.
    del password
