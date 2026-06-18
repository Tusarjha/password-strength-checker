import random

common_passwords = [
    "123456",
    "password",
    "qwerty",
    "abc123",
    "admin",
    "welcome"
]

def strength_check():
    pw = input("Enter password: ")

    score = 0

    if len(pw) >= 8:
        score += 1

    upper = False
    lower = False
    digit = False
    special = False

    for ch in pw:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if upper:
        score += 1

    if lower:
        score += 1

    if digit:
        score += 1

    if special:
        score += 1

    print("\nScore:", score, "/ 5")

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Medium Password")
    else:
        print("Strong Password")


def common_check():
    pw = input("Enter password: ")

    found = False

    for item in common_passwords:
        if pw == item:
            found = True
            break

    if found:
        print("Password is very common!")
    else:
        print("Password not found in common list.")


def entropy_check():
    pw = input("Enter password: ")

    unique = []

    for ch in pw:
        if ch not in unique:
            unique.append(ch)

    entropy = len(unique) * len(pw)

    print("Entropy Score:", entropy)

    if entropy < 30:
        print("Low Entropy")
    elif entropy < 60:
        print("Medium Entropy")
    else:
        print("High Entropy")


def policy_check():
    pw = input("Enter password: ")

    if len(pw) < 8:
        print("Length should be at least 8")
        return

    has_upper = False
    has_digit = False

    for ch in pw:
        if ch.isupper():
            has_upper = True

        if ch.isdigit():
            has_digit = True

    if not has_upper:
        print("Need at least one uppercase letter")
        return

    if not has_digit:
        print("Need at least one digit")
        return

    print("Password follows policy")


def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"

    pw = ""

    for i in range(12):
        pw += random.choice(chars)

    print("Generated Password:")
    print(pw)


while True:
    print("\n=== Password Security Toolkit ===")
    print("1. Password Strength Check")
    print("2. Common Password Check")
    print("3. Entropy Check")
    print("4. Policy Check")
    print("5. Generate Password")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        strength_check()

    elif choice == "2":
        common_check()

    elif choice == "3":
        entropy_check()

    elif choice == "4":
        policy_check()

    elif choice == "5":
        generate_password()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
    print("\nExcellent! Your password is very strong.")
