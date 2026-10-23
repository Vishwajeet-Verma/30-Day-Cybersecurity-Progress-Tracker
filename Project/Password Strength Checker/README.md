# Password Strength Checker

A beginner-friendly Python project that evaluates password characteristics and classifies password strength as Weak, Medium, or Strong.

## Features

- Minimum password length check (8 characters).
- Uppercase and lowercase letter checks.
- Number and special character checks.
- Clear validation results.
- Password input hidden in the terminal using Python's `getpass`.
- No password values printed or intentionally saved by the program.

## Requirements

- Python 3
- No external packages required.

## Setup

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the program:

   ```bash
   python password_strength_checker.py
   ```

4. Enter a dummy password when prompted.

## Strength Rules

- **Weak:** Fails the minimum length requirement or passes fewer than three checks.
- **Medium:** Passes the minimum length requirement and at least three checks, but not all five.
- **Strong:** Passes all five checks.

## Testing

Test using dummy inputs, including:
- Empty input
- Passwords shorter than 8 characters
- Lowercase-only input
- Inputs missing uppercase, numbers, or special characters
- An input that passes all checks

## Security Notes

- Never use real account passwords for testing.
- The program does not print or intentionally write passwords to files.
- `getpass` hides typed input in supported terminals but does not guarantee secure memory erasure.
- This is an educational project, not a complete password-security assessment.

## Project Status

Project 1 — Password Strength Checker: Final review and publication.