"""
move.py

Represents a Scrabble move.
"""


class Move:
    """
    Represents a single Scrabble move.
    """

    HORIZONTAL = "H"
    VERTICAL = "V"

    def __init__(self, word, row, column, direction, score=0):
        """
        Initialize a move.

        Parameters
        ----------
        word : str
            Word being played.

        row : int
            Starting row.

        column : int
            Starting column.

        direction : str
            "H" or "V"

        score : int
            Score of the move.
        """

        self.word = word.upper()
        self.row = row
        self.column = column
        self.direction = direction
        self.score = score

    def is_horizontal(self):
        """
        Return True if the move is horizontal.
        """

        return self.direction == Move.HORIZONTAL

    def is_vertical(self):
        """
        Return True if the move is vertical.
        """

        return self.direction == Move.VERTICAL

    def __str__(self):
        """
        Return a readable representation.
        """

        direction = (
            "Horizontal"
            if self.is_horizontal()
            else "Vertical"
        )

        return (
            f"{self.word} "
            f"at ({self.row}, {self.column}) "
            f"{direction} "
            f"Score={self.score}"
        )
