"""
Unit tests for Board.
"""

import unittest

from src.board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):

        self.board = Board()


    def test_board_size(self):

        self.assertEqual(
            len(self.board.grid),
            15
        )


        self.assertEqual(
            len(self.board.grid[0]),
            15
        )


    def test_empty_board(self):

        empty_cells = 0


        for row in self.board.grid:

            for cell in row:

                if cell is None:

                    empty_cells += 1


        self.assertEqual(
            empty_cells,
            225
        )


    def test_place_horizontal_word(self):

        result = self.board.place_word(
            "HELLO",
            7,
            7,
            "H"
        )


        self.assertTrue(
            result
        )


    def test_place_vertical_word(self):

        result = self.board.place_word(
            "WORLD",
            5,
            5,
            "V"
        )


        self.assertTrue(
            result
        )


if __name__ == "__main__":
    unittest.main()
