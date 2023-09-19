class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        length_text = len(self.text)
        non_vowel_characters = []
        while i < length_text:
            if self.text[i].lower() not in self.vowels:
                non_vowel_characters.append(self.text[i])
            i += 1
        self.text = "".join(non_vowel_characters)
        return self.text

# File: tests/test_vowel_remover.py

def test_can_remove_vowels_from_all_vowel_string():
    remover = VowelRemover("aeiou")
    result_no_vowels = remover.remove_vowels()
    print (result_no_vowels)
def test_can_remove_adjacent_vowels():
    remover = VowelRemover("book")
    result_no_vowels = remover.remove_vowels()
    print(result_no_vowels)

test_can_remove_vowels_from_all_vowel_string()
test_can_remove_adjacent_vowels()

