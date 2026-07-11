"""
player.py

Player classes.
"""


class Player:

    def __init__(
        self,
        name
    ):

        self.name = name

        self.rack = []

        self.score = 0



    def add_tile(self, tile):
        """
        Add tile to rack.
        """

        self.rack.append(tile)



    def remove_tiles(self, word):
        """
        Remove letters used in word.
        """

        for letter in word:

            if letter in self.rack:

                self.rack.remove(letter)



    def has_tile(self, letter):
        """
        Check one tile.
        """

        return letter in self.rack



    def has_tiles(self, word):
        """
        Check if player owns all letters.
        """

        temp = self.rack.copy()


        for letter in word:

            if letter in temp:

                temp.remove(letter)

            else:

                return False


        return True
