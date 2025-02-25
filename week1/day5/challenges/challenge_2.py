def longest_word(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Initialize variables to track the longest word and its length
    longest = ""
    max_length = 0
    
    # Iterate through each word in the list
    for word in words:
        # Update the longest word if the current word's length is greater than the max_length
        if len(word) > max_length:
            longest = word
            max_length = len(word)
    
    return longest


def menu():
    while True:
        print("\nMenu:")
        print("1. Input a sentence")
        print("2. Quit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            user_input = input("Enter a sentence: ")
            result = longest_word(user_input)
            print("The longest word is:", result)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Run the menu function
menu()
