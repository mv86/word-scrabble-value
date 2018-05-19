"""Test module for word_value."""
import pytest

from word_value import word_in_dictionary, word_value, words_values, top_n_scrabble_words


@pytest.mark.parametrize('word, rt_val', [
    ('', False),
    ('true', True),
    ('TRUE', True),
    ('  tRuE  ', True),
    (99, False),
    (99.99, False),
    (['false'], False),
    (False, False),
])
def test_word_in_dictionary(word, rt_val):
    assert word_in_dictionary(word) == rt_val


@pytest.mark.parametrize('word, rt_value', [
    ('a', 1),
    ('word', 8),
    ('miXeD', 15),
    ('  spaces   ', 10),
    ('ga p s', 7),
    ('', 0),
    ('1nval$d', 0),
    (999, 0),
    (20.5, 0),
    (False, 0)
])
def test_word_value(word, rt_value):
    assert word_value(word) == rt_value


def test_word_values():
    words = (True, 99, 'b aD! ', 'good', 'amazing')
    values = (0, 0, 0, 6, 19)

    scrabble_values = words_values(words)
    assert scrabble_values == list(zip(words, values))


def test_top_n_scrabble_words():
    words = ['b aD! ', 'good', 'amazing']

    # Call with no 'n' argument returns top word
    top_word = top_n_scrabble_words(words)
    word, score = top_word[0]
    assert word == 'amazing'
    assert score == 19

    # Can select top n words
    top_word, second_word, third_word = top_n_scrabble_words(words, n=3)
    assert top_word == ('amazing', 19)
    assert second_word == ('good', 6)
    assert third_word == ('b aD! ', 0)

    # No words argument results in default word list used
    top_two_words = top_n_scrabble_words(n=2)
    assert top_two_words == [
        ('pizzazz', 45), 
        ('quizzically', 43), 
    ]
 