"""
board_layout.py

Defines the official Scrabble board layout.

Symbols
-------
TW : Triple Word
DW : Double Word
TL : Triple Letter
DL : Double Letter
** : Center Star
.  : Normal Square
"""

BOARD_SIZE = 15


BOARD_LAYOUT = [

    ["TW", ".", ".", "DL", ".", ".", ".", "TW", ".", ".", ".", "DL", ".", ".", "TW"],

    [".", "DW", ".", ".", ".", "TL", ".", ".", ".", "TL", ".", ".", ".", "DW", "."],

    [".", ".", "DW", ".", ".", ".", "DL", ".", "DL", ".", ".", ".", "DW", ".", "."],

    ["DL", ".", ".", "DW", ".", ".", ".", "DL", ".", ".", ".", "DW", ".", ".", "DL"],

    [".", ".", ".", ".", "DW", ".", ".", ".", ".", ".", "DW", ".", ".", ".", "."],

    [".", "TL", ".", ".", ".", "TL", ".", ".", ".", "TL", ".", ".", ".", "TL", "."],

    [".", ".", "DL", ".", ".", ".", "DL", ".", "DL", ".", ".", ".", "DL", ".", "."],

    ["TW", ".", ".", "DL", ".", ".", ".", "**", ".", ".", ".", "DL", ".", ".", "TW"],

    [".", ".", "DL", ".", ".", ".", "DL", ".", "DL", ".", ".", ".", "DL", ".", "."],

    [".", "TL", ".", ".", ".", "TL", ".", ".", ".", "TL", ".", ".", ".", "TL", "."],

    [".", ".", ".", ".", "DW", ".", ".", ".", ".", ".", "DW", ".", ".", ".", "."],

    ["DL", ".", ".", "DW", ".", ".", ".", "DL", ".", ".", ".", "DW", ".", ".", "DL"],

    [".", ".", "DW", ".", ".", ".", "DL", ".", "DL", ".", ".", ".", "DW", ".", "."],

    [".", "DW", ".", ".", ".", "TL", ".", ".", ".", "TL", ".", ".", ".", "DW", "."],

    ["TW", ".", ".", "DL", ".", ".", ".", "TW", ".", ".", ".", "DL", ".", ".", "TW"]

]


def get_square(row, col):
    """
    Return the board square type.

    Parameters
    ----------
    row : int

    col : int

    Returns
    -------
    str
    """

    return BOARD_LAYOUT[row][col]


def is_bonus(row, col):
    """
    Return True if square contains a bonus.
    """

    value = get_square(row, col)

    return value != "."


def display_layout():
    """
    Print the bonus layout.
    """

    print()

    print("=" * 70)

    print("SCRABBLE BOARD LAYOUT")

    print("=" * 70)

    for row in BOARD_LAYOUT:

        print(" ".join(f"{cell:>2}" for cell in row))

    print()


if __name__ == "__main__":

    display_layout()
