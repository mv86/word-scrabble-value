"""Simple scrabble game."""
from player import Player
from round_helper import player_round, print_round_stats
from scrabble_helper import new_pouch

# Enhancement: Add functionaliry for 2 player game

def scrabble():
    """Main Scrabble loop."""
    print('\nWelcome to scrabble, press CTRL+C to quit any time.\n')
    pouch = new_pouch()
    player = Player()
    rounds = 0
    while player.points < 100:  # Play round of scrabble
        player_word, optimal_words = player_round(player, pouch)
        print_round_stats(player, player_word, optimal_words)
        rounds += 1
    print(f'You scored {player.points} in {rounds} rounds! Goodbye!')


if __name__ == '__main__':
    try:
        scrabble()
    except (KeyboardInterrupt, EOFError):  # Player wants to quit
        print('\n\nYou got it, goodbye!\n')
    