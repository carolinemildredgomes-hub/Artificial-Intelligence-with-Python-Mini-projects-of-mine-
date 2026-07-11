"""
Training tests.
"""

import unittest

from src.training import Trainer


class TestTraining(unittest.TestCase):

    def setUp(self):

        self.trainer = Trainer(
            episodes=5
        )


    def test_episode_count(self):

        self.assertEqual(
            self.trainer.episodes,
            5
        )


    def test_agent_exists(self):

        self.assertTrue(
            hasattr(
                self.trainer,
                "agent"
            )
        )


        self.assertIsNotNone(
            self.trainer.agent
        )


if __name__ == "__main__":
    unittest.main()
