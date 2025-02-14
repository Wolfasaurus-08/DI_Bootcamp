from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker('C:\\Users\\corde\\DI_Bootcamp\\week2\\day5\\mini_project_anagrams\\sowpods.txt')  # Load your word list file here

    while True:
        print("Anagram Checker")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            word = input("Enter a word: ").strip()

            if ' ' in word:
                print("Error: Only a single word is allowed.")
                continue

            if not word.isalpha():
                print("Error: This is not a valid word.")
                continue

            if checker.is_valid_word(word):
                print(f"YOUR WORD: {word.upper()}")
                print("This is a valid English word.")
                anagrams = checker.get_anagrams(word)
                print("Anagrams for your word:", ", ".join(anagrams))
            else:
                print(f"YOUR WORD: {word.upper()}")
                print("This is not a valid English word.")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()