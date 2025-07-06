import random
import string

# Prompt the user for the desired password length
length = int(input("Enter the desired password length: "))

# Define character sets for complexity
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Combine all character sets
all_characters = lowercase + uppercase + digits + symbols

# Generate a random password
password = ''.join(random.choice(all_characters) for _ in range(length))

# Display the password
print(f"\nGenerated Password: {password}")