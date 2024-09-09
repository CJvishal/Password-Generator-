import random
import string

# Function to generate a random password
def generate_password(length):
    if length < 4:  # Ensures the password has at least 1 character from each category
        print("Password length should be at least 4")
        return None

    # Define possible characters for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters into one list
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password contains at least one from each category
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Generate the rest of the password randomly from the full set
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to avoid any predictable patterns
    random.shuffle(password)

    # Join the list into a string and return it
    return ''.join(password)

# Main program
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    if password:
        print(f"Generated password: {password}")
