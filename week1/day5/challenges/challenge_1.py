def sort_words(input_string):
    # Split the input string by comma to get a list of words
    words = [word.strip() for word in input_string.split(",")]
    
    # Sort the list of words alphabetically
    sorted_words = sorted(words)
    
    # Join the sorted list back into a comma-separated string
    result = ",".join(sorted_words)
    
    return result

# Prompt the user to enter a comma-separated sequence of words
user_input = input("Enter a comma-separated sequence of words: ")
sorted_string = sort_words(user_input)
print("Sorted words:", sorted_string)
