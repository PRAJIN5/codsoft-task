import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits

    # Combine letters and digits
    all_chars = letters + digits

    # Generate the password ensuring at least one letter and one digit
    password_chars = [
        random.choice(letters),
        random.choice(digits)
    ]
    
    # Generate remaining characters
    password_chars += random.choices(all_chars, k=length - len(password_chars))

    # Shuffle the characters to ensure randomness
    random.shuffle(password_chars)

    # Join the list to form the final password string
    return ''.join(password_chars)

def main():
    while True:
        try:
            # Get user-defined password length
            length = int(input("Enter the desired password length: "))
            
            # Generate and print the password
            print("Generated password:", generate_password(length))
            
            # Ask if the user wants to generate another password or exit
            choice = input("Do you want to generate another password? (y/n): ").strip().lower()
            
            if choice == 'n':
                print("Exiting...")
                break  # Exit the loop and end the program
        except ValueError:
            print("Invalid input, please enter a valid number for the length.")

# Run the program
main()
