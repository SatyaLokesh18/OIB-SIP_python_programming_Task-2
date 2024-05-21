import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ""
    
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        return "No character set selected. Please choose at least one."

    generated_password = ''.join(random.choice(character_set) for _ in range(length))
    return generated_password

def run_password_generator():
    """
    Main function to run the password generator.
    """
    print("Password Generator")

    # Obtain user preferences for password generation
    try:
        password_length = int(input("Enter the desired password length: "))
        include_letters = input("Include letters (yes/no)? ").lower() == 'yes'
        include_numbers = input("Include numbers (yes/no)? ").lower() == 'yes'
        include_symbols = input("Include symbols (yes/no)? ").lower() == 'yes'
    except ValueError:
        print("Invalid input. Please enter a valid password length.")
        return

    # Generate password
    generated_password = generate_password(password_length, include_letters, include_numbers, include_symbols)

    # Display the generated password
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    run_password_generator()
