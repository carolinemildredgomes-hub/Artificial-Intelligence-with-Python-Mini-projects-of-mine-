"""
scoring.py

Scrabble scoring engine.
"""


class Scoring:
    """
    Provides methods for calculating Scrabble scores.
    """

    LETTER_VALUES = {
        "A": 1, "B": 3, "C": 3, "D": 2,
        "E": 1, "F": 4, "G": 2, "H": 4,
        "I": 1, "J": 8, "K": 5, "L": 1,
        "M": 3, "N": 1, "O": 1, "P": 3,
        "Q": 10, "R": 1, "S": 1, "T": 1,
        "U": 1, "V": 4, "W": 4, "X": 8,
        "Y": 4, "Z": 10
    }

    @staticmethod
    def letter_score(letter):
        """
        Return the score of a single letter.

        Parameters
        ----------
        letter : str

        Returns
        -------
        int
        """

        return Scoring.LETTER_VALUES.get(letter.upper(), 0)

    @staticmethod
    def score_word(word):
        """
        Calculate the total score of a word.

        Parameters
        ----------
        word : str

        Returns
        -------
        int
        """

        total = 0

        for letter in word.upper():
            total += Scoring.letter_score(letter)

        return total
