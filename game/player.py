"""Player class for scrabble game.
   Attributes:
            hand: List[str], Current hand of 7 scrabble tiles
            points: int, Total game points
   Methods:
            display_hand()
            fetch_tiles()
            word_choice()
"""
import random
from typing import List


class Player():
    """Represents pLayer in scrabble game."""
    def __init__(self):
        self.hand = []
        self.points = 0

    def __repr__(self):
        return 'Player()'

    def __str__(self):
        return f'Player. Hand, {self.hand}, Points, {self.points}'

    def fetch_tiles(self, pouch: List[str]):
        """Top up player hand to have 7 scrabble tiles."""
        while len(self.hand) < 7:
            rand_idx = random.randint(0, (len(pouch)-1))
            self.hand.extend(pouch.pop(rand_idx))
  
    def display_hand(self):
        """Print current hand to screen."""
        print(', '.join(self.hand), '\n')
