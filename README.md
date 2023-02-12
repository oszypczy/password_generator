Password Generator:
This is a password generator program written in Python. It generates random passwords based on the specified parameters. The program uses a file containing a list of words and generates passwords using the following steps:
- Reads a file named "words.txt" which contains a list of words to be used in generating the password.
- Selects words randomly from the list based on the specified number of words to be included in the password.
- Selects a random separator character to separate the words in the password.
- Selects a random padding symbol to be used in the beginning and end of the password.
- Generates random padding digits to be included in the beginning and end of the password.

Usage:
The program takes the following arguments:
- possible_separators: a string of characters to be used as separators between the words in the password.
- padding_digits: an integer indicating the number of random digits to be included in the beginning and end of the password.
- padding_symbol_number: an integer indicating the number of random padding symbols to be included in the beginning and end of the password.
- possible_padding_symbols: a string of characters to be used as padding symbols in the password.
- words_number: an integer indicating the number of words to be included in the password.
- minimal_word_length: an integer indicating the minimum length of a word to be included in the password.
- maximal_word_length: an integer indicating the maximum length of a word to be included in the password.
- generated_passwords: an integer indicating the number of passwords to be generated.

Output:
The program outputs the generated password(s) to the console.

Note:
The program assumes that the file "words.txt" is in the same directory as the script.
Make sure the file "words.txt" contains words with lengths between the specified minimum and maximum word length parameters.
