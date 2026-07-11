"""
Unit tests for AI.
"""

import unittest

from src.ai import AIPlayer


class TestAI(unittest.TestCase):

    def setUp(self):
        self.ai = AIPlayer()


    def test_ai_creation(self):

        self.assertIsNotNone(
            self.ai
        )


    def test_default_difficulty(self):

        self.assertEqual(
            self.ai.difficulty,
            AIPlayer.MEDIUM
        )


    def test_statistics(self):

        stats = self.ai.statistics()

        self.assertIsInstance(
            stats,
            dict
        )


        self.assertIn(
            "moves",
            stats
        )


        self.assertEqual(
            stats["moves"],
            0
        )


    def test_average_score(self):

        score = self.ai.average_score()

        self.assertEqual(
            score,
            0
        )


if __name__ == "__main__":
    unittest.main()
