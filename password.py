import random
import string

def generate_password(length):
    # Define the character sets to be used
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation  # includes punctuation symbols

    # Combine all character sets to form the full set of possible characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a password by randomly selecting characters from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be greater than zero. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password of length {length}: {password}")

if __name__ == "__main__":
    main()
