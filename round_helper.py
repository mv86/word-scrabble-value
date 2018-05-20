"""Contains helper functions for each scrabble round.
   Functions:
            player_round()
            print_round_stats()
"""
from typing import List, NamedTuple, Tuple
from collections import namedtuple
from itertools import filterfalse, permutations

from player import Player
from scrabble_helper import word_value, word_in_dictionary


Word = namedtuple('Word', 'word value')


def player_round(player: Player, pouch: List[str]) -> Tuple[NamedTuple, List[NamedTuple]]:
    """One round of scrabble game."""
    player.fetch_tiles(pouch)
    player.display_hand()
    word = _prompt_for_word(player)     
    value = word_value(word)
    player.points += value
    player_word = Word(word.upper(), value)
    optimal_words = _get_optimal_words(player.hand)
    _remove_tiles(word, player.hand)
    return player_word, optimal_words


def print_round_stats(player: Player, player_word: NamedTuple, optimal_words: List[NamedTuple]):
    """Display current word_score, any optimal words and player points."""
    opt_words = [word.upper() for word, _ in optimal_words]
    opt_value = optimal_words[0].value
    print(f'\nYour word {player_word.word} scored {player_word.value}!\n')
    print(f"Optimal word(s) for hand: {', '.join(opt_words)}, value: {opt_value}\n")
    print(f'Total points = {player.points}.\n')


def _prompt_for_word(player: Player) -> str:
    """Prompt player for word and validate."""
    valid_word = False
    while not valid_word:
        word = input('Form a valid word --> ').lower().strip()
        valid_word = _is_valid_word(word, player.hand)
    return word


def _is_valid_word(word: str, hand: List[str]) -> bool:
    """Validate player word choice."""
    if word_in_dictionary(word) and _word_in_hand(word, hand):
        return True
    print(f'\nPlease choose a valid word!\n')
    return False


def _word_in_hand(word: str, hand: List[str]) -> bool:
    """Test all letters for word are in users current hand."""
    letters_in_hand = []
    test_hand = hand[:]  # Don't want to pop from real hand
    for letter in word:
        for idx, tile in enumerate(test_hand):
            if letter.lower() == tile.lower():
                letters_in_hand.extend(test_hand.pop(idx))
                break
    if not word:
        return False
    return len(word) == len(letters_in_hand)


def _remove_tiles(word: str, hand: List[str]):
    """Remove tiles for chosen word from players hand."""
    for letter in word:
        for idx, tile in enumerate(hand):
            if letter.lower() == tile.lower():
                hand.pop(idx)
                break 


def _get_optimal_words(hand: List[str]) -> List[NamedTuple]:
    """Return optimal words from all permutations of given hand."""
    words = set(''.join(word)for perm_size in range(2, 8)
                for word in permutations(hand, perm_size))

    valid_words = [Word(word, word_value(word)) 
                   for word in words
                   if word_in_dictionary(word)]

    max_value = max(value for word, value in valid_words)
    optimal_words = filterfalse(lambda word: word.value < max_value, valid_words)
    return list(optimal_words)
