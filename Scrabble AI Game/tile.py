"""
tile.py

Represents a single Scrabble tile.
"""


class Tile:
    """
    Represents a Scrabble tile.
    """

    def __init__(self, letter: str, score: int):
        self.letter = letter.upper()
        self.score = int(score)

    def __str__(self):
        """
        Human-readable representation.
        """
        return self.letter

    def __repr__(self):
        """
        Debug representation.
        """
        return f"Tile('{self.letter}', {self.score})"

    def __eq__(self, other):
        if isinstance(other, Tile):
            return (
                self.letter == other.letter
                and self.score == other.score
            )
        return False

    def __hash__(self):
        return hash((self.letter, self.score))

    def display(self):
        print("+-----+")
        print(f"|  {self.letter}  |")
        print(f"|  {self.score:2} |")
        print("+-----+")
