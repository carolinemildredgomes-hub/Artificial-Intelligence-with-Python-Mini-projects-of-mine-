"""
Game tests.
"""

import unittest

from src.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):

        self.game = Game()


    def test_players(self):

        self.assertEqual(
            len(self.game.players),
            2
        )


    def test_scores_start_zero(self):

        self.assertEqual(
            self.game.human.score,
            0
        )


        self.assertEqual(
            self.game.ai.score,
            0
        )


    def test_initial_rack_size(self):

        self.assertEqual(
            len(self.game.human.rack),
            7
        )


        self.assertEqual(
            len(self.game.ai.rack),
            7
        )


if __name__ == "__main__":
    unittest.main()
