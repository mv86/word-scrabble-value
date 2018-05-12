"""Module to calculate scrabble word scores.
   
   Constants:
            SCRABBLE_SCORES: List of tuples (score, letters)
            LETTER_SCORES: Dict of letter: score
   Functions:
            top_n_scrabble_words()
            words_values()
            word_value()
"""
SCRABBLE_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]


LETTER_SCORES = {letter: score for score, letters in SCRABBLE_SCORES
                 for letter in letters.split()}


with open('word_list.txt') as word_list:
    DICTIONARY = [word.strip() for word in word_list]


def top_n_scrabble_words(words=None, n=1):
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


def words_values(words):
    """Take an iterable of words and return a list of tuples (word, scrabble_value).""" 
    return [(word, word_value(word)) for word in words]


def word_value(word):
    """Return scrabble value for given word. Return 0 for non-words."""
    try:
        word = word.replace(' ', '')
        letter_scores = (LETTER_SCORES[letter.upper()] for letter in word)
        return sum(letter_scores)
    except (TypeError, KeyError, AttributeError):  # Invalid word
        return 0
