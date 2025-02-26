import random

def get_words_from_file(file_path):
    """Reads words from a given file and returns them as a list."""
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def get_random_sentence(length, words):
    """Generates a random sentence with the specified number of words."""
    random_words = random.sample(words, length)  # Get unique random words
    sentence = ' '.join(random_words).lower()  # Create sentence and convert to lower case
    return sentence

def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program will generate a random sentence of a specified length.")
    
    # User input for sentence length
    try:
        length = int(input("How long should the sentence be? (2-20): "))
        if length < 2 or length > 20:
            print("Error: Please enter an integer between 2 and 20.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        return
    
    # Load words from file
    file_path = r"C:\Users\corde\DI_Bootcamp\week2\day4\exercises\sowpods.txt"
    words = get_words_from_file(file_path)
    
    # Generate and print the random sentence
    random_sentence = get_random_sentence(length, words)
    print("Generated Sentence:", random_sentence)

if __name__ == "__main__":
    main()

