class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(f"Alphabet ({self.lang}): {self.letters}")

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26  # количество букв в алфавите

    def __init__(self):
        lang = 'En'
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        super().__init__(lang, letters)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "Hello, World!"

# Пример использования классов
alphabet = Alphabet('Generic', 'ABC')
alphabet.print()
print(f"Number of letters: {alphabet.letters_num()}")

eng_alphabet = EngAlphabet()
eng_alphabet.print()
print(f"Number of letters in English alphabet: {eng_alphabet.letters_num()}")
print(f"Is 'A' an English letter? {eng_alphabet.is_en_letter('A')}")
print(f"Is 'Я' an English letter? {eng_alphabet.is_en_letter('Я')}")
print(EngAlphabet.example())
