"""
board.py

Scrabble board management.
"""


class Board:

    SIZE = 15


    def __init__(self):
        """
        Create empty Scrabble board.
        """

        self.grid = [
            [None for _ in range(self.SIZE)]
            for _ in range(self.SIZE)
        ]



    def is_valid_position(self, row, col):
        """
        Check if position is inside board.
        """

        return (
            0 <= row < self.SIZE
            and
            0 <= col < self.SIZE
        )



    def place_word(
        self,
        word,
        row,
        col,
        direction
    ):
        """
        Place word on board.

        direction:
        H = horizontal
        V = vertical
        """

        word = word.upper()

        direction = direction.upper()


        if direction not in ("H", "V"):

            return False



        positions = []


        for index, letter in enumerate(word):

            if direction == "H":

                r = row
                c = col + index

            else:

                r = row + index
                c = col



            if not self.is_valid_position(r, c):

                return False



            existing = self.grid[r][c]


            if existing is not None and existing != letter:

                return False



            positions.append(
                (r, c, letter)
            )



        for r, c, letter in positions:

            self.grid[r][c] = letter



        return True



    def get_letter(self, row, col):
        """
        Return letter at position.
        """

        if self.is_valid_position(row, col):

            return self.grid[row][col]

        return None



    def display(self):
        """
        Print board.
        """

        for row in self.grid:

            print(
                " ".join(
                    cell if cell else "."
                    for cell in row
                )
            )
