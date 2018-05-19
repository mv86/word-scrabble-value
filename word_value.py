"""Module to generate scrabble constants and calculate scrabble word scores.
   
   Constants:
            DICTIONARY: Set of words found at /usr/share/dict/words
            LETTER_SCORES: Dict of letter: score
            SCRABBLE_SCORES: List of tuples (score, letters)
            TILE_QUANTITY: List of tuples (quantity, letters)
   Functions:
            new_pouch()
            top_n_scrabble_words()
            word_in_dictionary()
            word_value()
            words_values()
"""
from typing import Iterable, List, Tuple
import random


SCRABBLE_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]


# TODO Add blank/wild tile for enhanced functionality (symbol = *, quantity = 2)
TILE_QUANTITY = [(1, "J K Q X Z"), (2, "B C F H M P V W Y"), (3, "G"), 
                 (4, "D L S U"), (6, "N R T"), (8, "O"), (9, "A I"), (12, "E")]


LETTER_SCORES = {letter: score for score, letters in SCRABBLE_SCORES
                 for letter in letters.split()}


with open('word_list.txt') as word_list:
    DICTIONARY = set(word.strip() for word in word_list)


def word_in_dictionary(word: str) -> bool:
    """Check dictionary for word."""
    return word in DICTIONARY


def new_pouch() -> List[str]:
    """Return shuffled list of all tiles in scrabble game."""
    pouch = []
    for tiles in TILE_QUANTITY:
        quantity, letters = tiles[0], tiles[1].split()
        for letter in letters:
            all_letters = letter * quantity
            pouch.extend(list(all_letters))
    random.shuffle(pouch)
    return pouch


def top_n_scrabble_words(words=None, *, n=1) -> List[Tuple]:
    """ Return list of top n scrabble word scores from word list. 

        Args:
            words=None: Iterable of words used to calculate scores.
                        Default to words list found at /usr/share/dict/words.
            n=1: Limit of highest score words to return,
    """
    if not words:
        scrabble_values = words_values(DICTIONARY)
    else:
        scrabble_values = words_values(words)
    scrabble_values.sort(key=lambda x: x[1], reverse=True)
    return scrabble_values[:n]


def words_values(words: Iterable) -> List[Tuple]:
    """Take an iterable of words and return a list of tuples (word, scrabble_value).""" 
    return [(word, word_value(word)) for word in words]


def word_value(word: str) -> int:
    """Return scrabble value for given word. Return 0 for non-words."""
    try:
        word = word.replace(' ', '')
        letter_scores = (LETTER_SCORES[letter.upper()] for letter in word)
        return sum(letter_scores)
    except (TypeError, KeyError, AttributeError):  # Invalid word
        return 0
