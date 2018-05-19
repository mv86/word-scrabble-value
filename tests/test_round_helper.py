import pytest

from round_helper import _word_in_hand


HAND = ['Z', 'O', 'E', 'T', 'A', 'O', 'P']

@pytest.mark.parametrize('hand, word, rt_val', [
    (HAND, 'at', True),
    (HAND, 'poet', True), # Handles duplicates in hand (P)
    (HAND, 'zoo', True),  # Handles duplicates in word (O)
    (HAND, 'trap', False),  # No 'R'
    (HAND, 'tote', False),  # Double use of 'T'
])
def test_word_in_hand(hand, word, rt_val):
    assert _word_in_hand(word, hand) == rt_val
