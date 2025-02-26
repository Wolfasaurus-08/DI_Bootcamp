# class Text:
#     def __init__(self, text):
#         self.text = text
    
#     def word_frequency(self, word):
#         words = self.text.split()
#         count = words.count(word)
#         if count == 0:
#             return f"The word '{word}' does not appear in the text."
#         return count
    
#     def most_common_word(self):
#         words = self.text.split()
#         word_counts = {}
        
#         for word in words:
#             word_counts[word] = word_counts.get(word, 0) + 1
        
#         most_common = max(word_counts, key=word_counts.get)
#         return most_common
    
#     def unique_words(self):
#         words = self.text.split()
#         unique_words_set = set(words)
#         return list(unique_words_set)

# # Example usage
# text_string = "A good book would sometimes cost as much as a good house."
# text_instance = Text(text_string)

# # Test methods
# print(text_instance.word_frequency("good"))  # Output: 2
# print(text_instance.most_common_word())  # Output: "a" (or "good", depending on word splitting)
# print(text_instance.unique_words())  # Output: list of unique words
class Text:
    def __init__(self, text):
        self.text = text
    
    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return f"The word '{word}' does not appear in the text."
        return count
    
    def most_common_word(self):
        words = self.text.split()
        word_counts = {}
        
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        
        most_common = max(word_counts, key=word_counts.get)
        return most_common
    
    def unique_words(self):
        words = self.text.split()
        unique_words_set = set(words)
        return list(unique_words_set)
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return cls(text)

# Example usage with the provided the_stranger.txt file
text_instance = Text.from_file('C:/Users/corde/DI_Bootcamp/week2/day4/daily challenge/the_stranger.txt')

# Test methods with the text from the file
print(text_instance.word_frequency("the"))
print