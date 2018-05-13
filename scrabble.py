"""Simple scrabble game."""
import random

from word_value import TILE_QUANTITY



def create_tiles() -> str:
    "Return str of all tiles in scrabble game."
    all_tiles = []
    for tiles in TILE_QUANTITY:
        quantity, letters = tiles[0], tiles[1].split()
        for letter in letters:
            letter_quantity = letter * quantity
            all_tiles.append(letter_quantity)
    return ''.join(all_tiles)


def get_random_seven():
    """Return list of seven random tiles."""
    tiles = create_tiles()
    return random.sample(tiles, 7)

# print to screen

# user input word
# - validate all letters in word and no duplicate cheating
# lookup word value
# print to screen

# lookup optimal word value
# find combination of every word with score (logic needed)
# print to screen

# calculate users total score
# print total score to screen