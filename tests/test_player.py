"""Test module for player."""
from scrabble_helper import new_pouch
from player import Player


def test_player_initialisation(capsys):
    player = Player()
    assert player.hand == []
    assert player.points == 0
    assert repr(player) == 'Player()'
    print(player)
    out, _ = capsys.readouterr()
    assert out.rstrip() == 'Player. Hand, [], Points, 0'


def test_fetch_tiles():
    pouch = new_pouch()
    player = Player()
    assert len(pouch) == 98
    assert player.hand == []

    player.fetch_tiles(pouch)
    assert len(pouch) == 91
    assert len(player.hand) == 7

    player.hand.pop()
    player.hand.pop()
    assert len(player.hand) == 5
    player.fetch_tiles(pouch)
    assert len(pouch) == 89
    assert len(player.hand) == 7


def test_display_hand(capsys):
    player = Player()
    player.hand = ['Z', 'O', 'E', 'T', 'A', 'O', 'P']
    player.display_hand()
    out, _ = capsys.readouterr()
    assert out.rstrip() == 'Z, O, E, T, A, O, P'
