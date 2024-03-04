import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_punctuation=True):
    
    # Caractères pour le mot de passe
    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_punctuation:
        chars += string.punctuation

    if not chars:
        print("Error!")
        return None

    pw = ''.join(random.choice(chars) for _ in range(length))
    return pw

def main():
    print("Welcome to Random Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue

            letter = input("Use letters? (yes/no): ").lower() == 'yes'
            digit = input("Use digits? (yes/no): ").lower() == 'yes'
            punctuation = input("Use punctuation? (yes/no): ").lower() == 'yes'

            pw = generate_password(length, letter, digit, punctuation)
            if pw:
                print("Generated Password:", pw)
            break
        except ValueError:
            print("Invalid input!")

if __name__ == "__main__":
    main()