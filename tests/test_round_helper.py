"""Test module for round_helper."""
from unittest.mock import patch

import pytest

from player import Player
from round_helper import (_get_optimal_words, _is_valid_word, _prompt_for_word,
                          _remove_tiles, _word_in_hand)


HAND = 'Z O E T A O P'.split()


@patch('builtins.input', side_effect=['pot', 'zzz', 'no', 'top'])
def test_prompt_for_word(side_input):
    player = Player()
    player.hand = HAND
    assert _prompt_for_word(player) == 'pot'
    # Player re-prompted until valid word chosen
    assert _prompt_for_word(player) == 'top'


def test_is_valid_word(capsys):
    msg = 'Please choose a valid word!'
    assert _is_valid_word('pot', HAND)

    assert not _is_valid_word('zzz', HAND)  # Not in dictionary
    out, _ = capsys.readouterr()
    assert out.strip() == msg

    assert not _is_valid_word('no', HAND)  # Not in hand
    out, _ = capsys.readouterr()
    assert out.strip() == msg


@pytest.mark.parametrize('word, hand, rt_val', [
    ('at', [], False),
    ('', HAND, False),
    ('at', HAND, True),
    ('poet', HAND, True), # Handles duplicates in hand (O)
    ('zoo', HAND, True),  # Handles duplicates in word (O)
    ('trap', HAND, False),  # No 'R'
    ('tote', HAND, False)  # Double use of 'T'
])
def test_word_in_hand(word, hand, rt_val):
    assert _word_in_hand(word, hand) == rt_val


def test_remove_tiles():
    hand = 'Z O E T A O P'.split()

    _remove_tiles('at', hand)
    assert hand == ['Z', 'O', 'E', 'O', 'P']

    _remove_tiles('zoo', hand)  # Handles duplicated letters
    assert hand == ['E', 'P']


def test_get_optimal_words():
    optimal_word = _get_optimal_words(HAND)
    assert optimal_word[0].word == 'TOPAZ'
    assert optimal_word[0].value == 16

    # Return multiple word when applicable
    optimal_words = _get_optimal_words('A B C D E F G'.split())
    for word, value in optimal_words:
        assert word in ('FACED', 'DECAF')
        assert value == 11
