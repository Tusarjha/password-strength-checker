import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*)")

    return score, feedback


def get_strength_label(score):
    if score <= 2:
        return "WEAK 🔴"
    elif score <= 4:
        return "MEDIUM 🟡"
    else:
        return "STRONG 🟢"


print("=== Password Strength Checker ===")
password = input("Enter your password: ")

score, feedback = check_password_strength(password)
strength = get_strength_label(score)

print(f"\nStrength: {strength}")
print(f"Score: {score}/5")

if feedback:
    print("\nSuggestions to improve:")
    for tip in feedback:
        print(f"  → {tip}")
else:
    print("\nExcellent! Your password is very strong.")