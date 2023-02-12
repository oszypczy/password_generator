from random import choice, randint


class Password:
    def __init__(self, args):
        self.args = args
        self.words = self.get_words()
        self.separator = self.get_separator()
        self.padding_symbol = self.get_padding_symbol()

    def get_words(self):
        with open('words.txt', 'r') as handle:
            words = handle.readlines()
        list_of_words = [
            word.rstrip() for word in words
            if int(self.args.minimal_word_length) <= len(word.rstrip()) <= int(self.args.maximal_word_length) # noqa 551
        ]
        final_list_of_words = []
        for _ in range(int(self.args.words_number)):
            final_list_of_words.append(choice(list_of_words))
        return final_list_of_words

    def get_separator(self):
        separators = [char for char in self.args.possible_separators]
        return choice(separators)

    def get_padding_symbol(self):
        padding_symcols = [char for char in self.args.possible_padding_symbols]
        return choice(padding_symcols)

    def __str__(self):
        final_password = ''
        padding_digits = int(self.args.padding_digits)
        padding_symbols_number = int(self.args.padding_symbol_number)
        for _ in range(padding_symbols_number):
            final_password += self.padding_symbol
        for _ in range(padding_digits):
            final_password += str(randint(0, 9))
        for each_word in self.words:
            separated_word = self.separator + each_word
            final_password += separated_word
        final_password += self.separator
        for _ in range(padding_digits):
            final_password += str(randint(0, 9))
        for _ in range(padding_symbols_number):
            final_password += self.padding_symbol
        return final_password
