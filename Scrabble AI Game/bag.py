from src.tile import Tile
import random


class TileBag:
    """
    Represents the Scrabble tile bag.
    """

    LETTER_DISTRIBUTION = {
        "A": (9, 1),
        "B": (2, 3),
        "C": (2, 3),
        "D": (4, 2),
        "E": (12, 1),
        "F": (2, 4),
        "G": (3, 2),
        "H": (2, 4),
        "I": (9, 1),
        "J": (1, 8),
        "K": (1, 5),
        "L": (4, 1),
        "M": (2, 3),
        "N": (6, 1),
        "O": (8, 1),
        "P": (2, 3),
        "Q": (1, 10),
        "R": (6, 1),
        "S": (4, 1),
        "T": (6, 1),
        "U": (4, 1),
        "V": (2, 4),
        "W": (2, 4),
        "X": (1, 8),
        "Y": (2, 4),
        "Z": (1, 10),
    }

    def __init__(self):
        self.tiles = []
        self._create_tiles()
        self.shuffle()

    def _create_tiles(self):
        for letter, (count, score) in self.LETTER_DISTRIBUTION.items():
            for _ in range(count):
                self.tiles.append(Tile(letter, score))

    def shuffle(self):
        random.shuffle(self.tiles)

    def draw_tile(self):
        if len(self.tiles) == 0:
            return None

        return self.tiles.pop()

    def tiles_remaining(self):
        return len(self.tiles)

    def __str__(self):
        return f"TileBag({len(self.tiles)} tiles remaining)"
