from zaliczenie_password_io import Password
import argparse


def test_generate_password(monkeypatch):
    args = argparse.Namespace(
        possible_separators="-",
        padding_digits=1,
        padding_symbol_number=1,
        possible_padding_symbols="@",
        words_number=1,
        minimal_word_length=3,
        maximal_word_length=8
    )

    def get_fake_words(a):
        return ['AAA']

    def get_fake_number(a, b):
        return 0
    monkeypatch.setattr('zaliczenie_password_io.Password.get_words', get_fake_words)
    monkeypatch.setattr('zaliczenie_password_io.randint', get_fake_number)
    password = Password(args)
    assert str(password) == "@0-AAA-0@"


def test_generate_password_another_example(monkeypatch):
    args = argparse.Namespace(
        possible_separators="+",
        padding_digits=2,
        padding_symbol_number=3,
        possible_padding_symbols="?",
        words_number=2,
        minimal_word_length=3,
        maximal_word_length=8
    )
    def get_fake_words(a):
        return ['BBB', 'BBB']
    def get_fake_number(a, b):
        return 8
    monkeypatch.setattr('zaliczenie_password_io.Password.get_words', get_fake_words)
    monkeypatch.setattr('zaliczenie_password_io.randint', get_fake_number)
    password = Password(args)
    assert str(password) == '???88+BBB+BBB+88???'


def test_generate_password_third_example(monkeypatch):
    args = argparse.Namespace(
        possible_separators="&",
        padding_digits=4,
        padding_symbol_number=1,
        possible_padding_symbols="*",
        words_number=3,
        minimal_word_length=3,
        maximal_word_length=8
    )

    def get_fake_words(a):
        return ['AAA', 'BBB', 'CCC']

    def get_fake_number(a, b):
        return 3
    monkeypatch.setattr('zaliczenie_password_io.Password.get_words', get_fake_words)
    monkeypatch.setattr('zaliczenie_password_io.randint', get_fake_number)
    password = Password(args)
    assert str(password) == "*3333&AAA&BBB&CCC&3333*"
