# password_generator.py

# 🔸 Author: Amir Khan
# 🔸 Internship: CodSoft (Python Programming)
# 🔸 Task 3: Password Generator

import random
import string

def generate_password(length):
    if length < 4:
        return "❌ Password length should be at least 4 characters."

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all
    all_chars = lower + upper + digits + symbols

    # Ensure strong password (at least 1 of each)
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill remaining with random characters
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

def main():
    print("🔐 Welcome to Password Generator!")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"\n✅ Generated Password: {password}")
    except ValueError:
        print("❗ Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
