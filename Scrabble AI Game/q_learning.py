"""
q_learning.py

Reinforcement Learning (Q-Learning) module for Scrabble AI.
"""

import random
import pickle


class QLearningAgent:
    """
    Q-Learning Agent.
    """

    def __init__(
        self,
        learning_rate=0.10,
        discount_factor=0.95,
        epsilon=0.20
    ):

        self.q_table = {}

        self.alpha = learning_rate

        self.gamma = discount_factor

        self.epsilon = epsilon

    # ======================================================
    # STATE ENCODING
    # ======================================================

    def encode_state(
        self,
        board,
        rack
    ):
        """
        Convert board and rack into a hashable state.
        """

        board_state = tuple(

            tuple(row)

            for row in board.grid

        )

        rack_state = tuple(

            sorted(rack)

        )

        return (

            board_state,

            rack_state

        )

    # ======================================================
    # Q VALUE
    # ======================================================

    def get_q_value(
        self,
        state,
        action
    ):
        """
        Return stored Q-value.
        """

        return self.q_table.get(

            (state, action),

            0.0

        )

    def set_q_value(
        self,
        state,
        action,
        value
    ):

        self.q_table[

            (state, action)

        ] = value

    # ======================================================
    # ACTION SELECTION
    # ======================================================

    def choose_action(
        self,
        state,
        legal_moves
    ):
        """
        Epsilon-greedy action selection.
        """

        if not legal_moves:

            return None

        if random.random() < self.epsilon:

            return random.choice(

                legal_moves

            )

        return self.best_action(

            state,

            legal_moves

        )

    def best_action(
        self,
        state,
        legal_moves
    ):
        """
        Highest-Q move.
        """

        best = None

        best_q = float("-inf")

        for move in legal_moves:

            action = self.action_key(move)

            q = self.get_q_value(

                state,

                action

            )

            if q > best_q:

                best_q = q

                best = move

        return best

    # ======================================================
    # ACTION KEY
    # ======================================================

    def action_key(
        self,
        move
    ):
        """
        Convert Move into tuple.
        """

        return (

            move.word,

            move.row,

            move.column,

            move.direction

        )



     # ======================================================
    # REWARD FUNCTION
    # ======================================================

    def calculate_reward(
        self,
        move,
        game_over=False,
        won=False
    ):
        """
        Calculate the immediate reward for a move.
        """

        reward = move.score

        # Bonus for using many tiles
        reward += len(move.word)

        # Bonus for using all 7 tiles (Bingo)
        if len(move.word) == 7:
            reward += 50

        # Winning bonus
        if game_over and won:
            reward += 100

        # Losing penalty
        if game_over and not won:
            reward -= 100

        return reward

    # ======================================================
    # FUTURE REWARD
    # ======================================================

    def best_future_reward(
        self,
        next_state,
        legal_moves
    ):
        """
        Return the maximum future Q-value.
        """

        if not legal_moves:
            return 0.0

        best = float("-inf")

        for move in legal_moves:

            action = self.action_key(move)

            q = self.get_q_value(
                next_state,
                action
            )

            if q > best:
                best = q

        if best == float("-inf"):
            return 0.0

        return best

    # ======================================================
    # Q-LEARNING UPDATE
    # ======================================================

    def update(
        self,
        state,
        action,
        reward,
        next_state,
        next_moves
    ):
        """
        Apply the Q-learning update rule.

        Q(s,a) ← Q(s,a) +
                 α [ reward +
                     γ * max(Q(s',a'))
                     - Q(s,a)
                   ]
        """

        old_q = self.get_q_value(
            state,
            action
        )

        future = self.best_future_reward(
            next_state,
            next_moves
        )

        new_q = old_q + self.alpha * (
            reward +
            self.gamma * future -
            old_q
        )

        self.set_q_value(
            state,
            action,
            new_q
        )

    # ======================================================
    # EPSILON CONTROL
    # ======================================================

    def decay_epsilon(
        self,
        decay_rate=0.995,
        minimum=0.01
    ):
        """
        Reduce exploration over time.
        """

        self.epsilon = max(
            minimum,
            self.epsilon * decay_rate
        )

    def reset_epsilon(
        self,
        value=0.20
    ):
        """
        Reset epsilon to its initial value.
        """

        self.epsilon = value

    # ======================================================
    # SAVE / LOAD MODEL
    # ======================================================

    def save(
        self,
        filename
    ):
        """
        Save the learned Q-table.
        """

        with open(filename, "wb") as file:
            pickle.dump(
                self.q_table,
                file
            )

    def load(
        self,
        filename
    ):
        """
        Load a previously trained Q-table.
        """

        with open(filename, "rb") as file:
            self.q_table = pickle.load(file)

    # ======================================================
    # INFORMATION
    # ======================================================

    def statistics(self):
        """
        Return model information.
        """

        return {
            "states": len(self.q_table),
            "learning_rate": self.alpha,
            "discount_factor": self.gamma,
            "epsilon": self.epsilon
        }

    def print_statistics(self):
        """
        Display training information.
        """

        stats = self.statistics()

        print()
        print("=" * 50)
        print("Q-LEARNING MODEL")
        print("=" * 50)

        print(f"Stored Entries : {stats['states']}")
        print(f"Learning Rate  : {stats['learning_rate']}")
        print(f"Discount       : {stats['discount_factor']}")
        print(f"Epsilon        : {stats['epsilon']:.4f}")

        print("=" * 50)


# ==========================================================
# SIMPLE TEST
# ==========================================================

if __name__ == "__main__":

    agent = QLearningAgent()

    agent.print_statistics()
