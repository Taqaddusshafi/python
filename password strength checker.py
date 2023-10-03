import re

def is_strong_password(password):
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

if __name__ == "__main__":
    password = input("Enter a password: ")

    if is_strong_password(password):
        print("Password is strong!")
    else:
        print("Password is weak. Please choose a stronger password.")
