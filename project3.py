import random
import string


def generate_password(length):
    # Name that must be included
    name = "Abhi"

    # Check minimum length
    if length < len(name) + 2:
        return None

    # Character sets
    numbers = string.digits
    special_characters = string.punctuation
    all_characters = string.ascii_letters + numbers + special_characters

    # Start password with "Abhi"
    password = list(name)

    # Make sure there is at least one number
    password.append(random.choice(numbers))

    # Add random characters
    for _ in range(length - len(password)):
        password.append(random.choice(all_characters))

    # Shuffle everything
    random.shuffle(password)

    return ''.join(password)


# Main program
print("=" * 50)
print("       RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:
    try:
        length = int(input("Enter password length (minimum 6): "))

        if length < 6:
            print("❌ Password length must be at least 6.\n")
            continue

        password = generate_password(length)

        print("\n✅ Password Generated Successfully!")
        print("Your password:", password)
        print("Password length:", len(password))

        break

    except ValueError:
        print("❌ Please enter a valid number.")
