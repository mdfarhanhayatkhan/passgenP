import random
import string

def generate_password(length, use_upper, use_numbers, use_symbols):
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    length = int(input("Enter password length: "))
    upper = input("Include uppercase? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, upper, numbers, symbols)

    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
