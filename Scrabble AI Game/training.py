"""
training.py

Train the Scrabble AI using self-play and Q-Learning.
"""

from pathlib import Path

from src.game import Game
from src.q_learning import QLearningAgent
from src.pattern_recognition import PatternRecognizer


class Trainer:
    """
    Train the Scrabble AI.
    """

    def __init__(
        self,
        episodes=1000,
        model_path="models/q_table.pkl"
    ):

        self.episodes = episodes

        self.model_path = model_path

        self.agent = QLearningAgent()

        self.patterns = PatternRecognizer()

        self.total_rewards = []

    # =====================================================
    # TRAINING
    # =====================================================

    def train(self):
        """
        Run self-play training.
        """

        Path("models").mkdir(
            exist_ok=True
        )

        print("=" * 60)
        print("TRAINING STARTED")
        print("=" * 60)

        for episode in range(
            1,
            self.episodes + 1
        ):

            reward = self.play_episode()

            self.total_rewards.append(
                reward
            )

            self.agent.decay_epsilon()

            if episode % 100 == 0:

                average = (
                    sum(self.total_rewards[-100:])
                    / 100
                )

                print(
                    f"Episode {episode:5d} "
                    f"| Average Reward: {average:.2f}"
                )

        self.agent.save(
            self.model_path
        )

        print()
        print("Training Complete!")
        print(
            f"Model saved to {self.model_path}"
        )

    # =====================================================
    # SINGLE EPISODE
    # =====================================================

    def play_episode(self):
        """
        Train using one self-play game.
        """

        game = Game()

        total_reward = 0

        while True:

            player = game.active_player()

            if player.name == "Human":
                ai = game.ai
            else:
                ai = player

            state = self.agent.encode_state(
                game.board,
                ai.rack
            )

            moves = game.generator.generate_moves(
                ai.rack
            )

            legal = ai.filter_legal_moves(
                game.board,
                moves
            )

            move = self.agent.choose_action(
                state,
                legal
            )

            if move is None:

                game.switch_turn()

            else:

                success = game.board.place_word(

                    move.word,

                    move.row,

                    move.column,

                    move.direction

                )

                if success:

                    reward = self.agent.calculate_reward(
                        move
                    )

                    total_reward += reward

                    next_state = self.agent.encode_state(
                        game.board,
                        ai.rack
                    )

                    next_moves = ai.filter_legal_moves(

                        game.board,

                        game.generator.generate_moves(
                            ai.rack
                        )

                    )

                    self.agent.update(

                        state,

                        self.agent.action_key(move),

                        reward,

                        next_state,

                        next_moves

                    )

                    ai.score += move.score

                    ai.remove_tiles(
                        move.word
                    )

                    game.refill_rack(ai)

                    game.switch_turn()

            if len(game.bag.tiles) == 0:

                break

        return total_reward

    # =====================================================
    # EVALUATION
    # =====================================================

    def evaluate(self):
        """
        Print simple training statistics.
        """

        print()
        print("=" * 60)
        print("TRAINING SUMMARY")
        print("=" * 60)

        print(
            f"Episodes : {self.episodes}"
        )

        print(
            f"Best Reward : {max(self.total_rewards):.2f}"
        )

        print(
            f"Worst Reward : {min(self.total_rewards):.2f}"
        )

        print(
            f"Average Reward : "
            f"{sum(self.total_rewards)/len(self.total_rewards):.2f}"
        )

        print("=" * 60)

    # =====================================================
    # LOAD EXISTING MODEL
    # =====================================================

    def load_model(self):

        self.agent.load(
            self.model_path
        )

        print(
            "Existing model loaded."
        )

    # =====================================================
    # SAVE MODEL
    # =====================================================

    def save_model(self):

        self.agent.save(
            self.model_path
        )

        print(
            "Model saved."
        )


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    trainer = Trainer(
        episodes=1000
    )

    trainer.train()

    trainer.evaluate()
