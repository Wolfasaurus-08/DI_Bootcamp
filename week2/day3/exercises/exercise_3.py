# Instructions Generate random String of length 5 Note: String must be the 
# combination of the UPPER case and lower case letters only.
# No numbers and a special symbol. Hint: use the string module
import random
import string

def generate_random_string(length=5):
    letters = string.ascii_letters  # Contains both uppercase and lowercase letters
    return ''.join(random.choice(letters) for _ in range(length))

print(generate_random_string())