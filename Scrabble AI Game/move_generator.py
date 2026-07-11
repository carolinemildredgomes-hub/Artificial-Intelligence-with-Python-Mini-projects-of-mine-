"""
move_generator.py

Generates possible Scrabble moves.
"""

from itertools import permutations

from src.move import Move
from src.scoring import Scoring


class MoveGenerator:
    """
    Generates candidate Scrabble moves from a player's rack.
    """

    def __init__(self, dictionary):
        """
        Parameters
        ----------
        dictionary : Dictionary
            Scrabble dictionary.
        """
        self.dictionary = dictionary

    def _rack_letters(self, rack):
        """
        Convert a rack into a list of uppercase letters.

        Supports:
            - list[Tile]
            - list[str]
        """

        letters = []

        for item in rack:

            # Tile object
            if hasattr(item, "letter"):
                letters.append(item.letter.upper())

            # Already a string
            else:
                letters.append(str(item).upper())

        return letters

    def generate_words(self, rack):
        """
        Generate every valid dictionary word
        that can be built from the rack.
        """

        letters = self._rack_letters(rack)

        found_words = set()

        for length in range(2, len(letters) + 1):

            for perm in permutations(letters, length):

                word = "".join(perm)

                if self.dictionary.is_word(word):
                    found_words.add(word)

        return sorted(found_words)

    def generate_moves(self, rack):
        """
        Generate Move objects.

        Currently every move starts from the center
        of the board horizontally.
        """

        moves = []

        words = self.generate_words(rack)

        for word in words:

            move = Move(
                word=word,
                row=7,
                column=7,
                direction=Move.HORIZONTAL,
                score=Scoring.score_word(word)
            )

            moves.append(move)

        return moves
