import re
def password_strength(password):
    strength = "Weak"
    feedback = []

    # Check length
    if len(password) >= 12:
        strength = "Strong"
    else:
        feedback.append("Password should be at least 12 characters long.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        if strength == "Weak":
            strength = "Medium"
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        if strength == "Weak":
            strength = "Medium"
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check numbers
    if any(char.isdigit() for char in password):
        if strength == "Weak":
            strength = "Medium"
    else:
        feedback.append("Password should contain at least one number.")

    # Check special characters
    if any(not char.isalnum() for char in password):
        if strength == "Strong":
            strength = "Very Strong"
    else:
        feedback.append("Password should contain at least one special character.")

    return strength, feedback

password = input("Enter a password: ")
strength, feedback = password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for item in feedback:
        print(f"- {item}")
