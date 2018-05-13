"""Test module for scrabble."""
from scrabble import get_random_seven, create_tiles


def test_create_tiles():
    correct_tiles = ('JKQXZBBCCFFHHMMPPVVWWYY**GGGDDDDLLLLSSSSUUUUNNNNNN'
                     'RRRRRRTTTTTTOOOOOOOOAAAAAAAAAIIIIIIIIIEEEEEEEEEEEE')
    game_tiles = create_tiles()
    assert len(game_tiles) == 100
    assert game_tiles == correct_tiles


def test_get_random_seven():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    seven_tiles = get_random_seven()
    assert len(seven_tiles) == 7
    for tile in seven_tiles:
        assert tile in alphabet
