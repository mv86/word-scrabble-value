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
