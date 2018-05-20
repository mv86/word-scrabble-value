"""Test module for round_helper."""
from unittest.mock import patch

import pytest

from player import Player
from round_helper import _is_valid_word, _prompt_for_word, _word_in_hand


HAND = ['Z', 'O', 'E', 'T', 'A', 'O', 'P']

@pytest.mark.parametrize('word, hand, rt_val', [
    ('at', [], False),
    ('', HAND, False),
    ('at', HAND, True),
    ('poet', HAND, True), # Handles duplicates in hand (P)
    ('zoo', HAND, True),  # Handles duplicates in word (O)
    ('trap', HAND, False),  # No 'R'
    ('tote', HAND, False)  # Double use of 'T'
])
def test_word_in_hand(word, hand, rt_val):
    assert _word_in_hand(word, hand) == rt_val


# @patch('builtins.input', side_effect=['trap', 'no', 'zzz', 'RAP'])
# def test_prompt_for_word(side_input, capfd):
#     player = Player()
#     assert _prompt_for_word(player) == 'trap'
#     out, _ = capfd.readouterr()


def test_is_valid_word(capfd):
    msg = 'Please choose a valid word!'
    assert _is_valid_word('pot', HAND)

    assert not _is_valid_word('zzz', HAND)  # Not in dictionary
    out, _ = capfd.readouterr()
    assert out.strip() == msg

    assert not _is_valid_word('no', HAND)  # Not in hand
    out, _ = capfd.readouterr()
    assert out.strip() == msg
