# Password Strength Checker
# Author: Ashenafi Tsge
# Date: October 2025

import re

def check_password(password):
    """
    Check password strength:
    - Length >= 8
    - Contains uppercase, lowercase, number, symbol
    Returns: Weak / Medium / Strong
    """
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def main():
    print("=== Password Strength Checker ===")
    while True:
        pwd = input("Enter a password (or type 'exit' to quit): ")
        if pwd.lower() == "exit":
            print("Goodbye!")
            break
        print("Your password strength is:", check_password(pwd))
        # Optional: save attempts to file
        with open("example_passwords.txt", "a") as f:
            f.write(f"{pwd} -> {check_password(pwd)}\n")

if name == "main":
    main()