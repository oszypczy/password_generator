import sys
import argparse
from zaliczenie_password_io import Password


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("possible_separators")
    parser.add_argument("padding_digits")
    parser.add_argument("padding_symbol_number")
    parser.add_argument("possible_padding_symbols")
    parser.add_argument("words_number")
    parser.add_argument("minimal_word_length")
    parser.add_argument("maximal_word_length")
    parser.add_argument("generated_passwords")
    args = parser.parse_args(arguments[1:])
    print()
    for _ in range(int(args.generated_passwords)):
        print(str(Password(args)) + '\n')


if __name__ == "__main__":
    main(sys.argv)
