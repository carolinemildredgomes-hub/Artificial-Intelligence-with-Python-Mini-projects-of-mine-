"""
ai.py

Artificial Intelligence player for Scrabble.
"""

import random

from src.player import Player
from src.move import Move
from src.move_generator import MoveGenerator


class AIPlayer(Player):
    """
    Computer-controlled Scrabble player.
    """

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    def __init__(self, name="AI", difficulty=MEDIUM):
        """
        Initialize AI player.
        """

        super().__init__(name)

        self.difficulty = difficulty

        self.total_moves = 0
        self.total_score = 0

        self.last_move = None

    # ======================================================
    # MAIN AI
    # ======================================================

    def choose_move(
        self,
        board,
        dictionary,
        scoring
    ):
        """
        Select the best move.
        """

        generator = MoveGenerator(dictionary)

        candidate_moves = generator.generate_moves(
            self.rack
        )

        if not candidate_moves:
            return None

        legal_moves = self.filter_legal_moves(
            board,
            candidate_moves
        )

        if not legal_moves:
            return None

        move = self.select_move(
            legal_moves
        )

        self.last_move = move

        self.total_moves += 1
        self.total_score += move.score

        return move

    # ======================================================
    # FILTER MOVES
    # ======================================================

    def filter_legal_moves(
        self,
        board,
        moves
    ):
        """
        Keep only moves that fit the board.
        """

        legal = []

        for move in moves:

            if board.can_place_word(
                move.word,
                move.row,
                move.column,
                move.direction
            ):

                legal.append(move)

        return legal

    # ======================================================
    # MOVE SELECTION
    # ======================================================

    def select_move(self, moves):
        """
        Select a move depending on
        AI difficulty.
        """

        if self.difficulty == AIPlayer.EASY:
            return self.random_move(moves)

        if self.difficulty == AIPlayer.MEDIUM:
            return self.medium_move(moves)

        return self.best_move(moves)

    def random_move(self, moves):
        """
        Random legal move.
        """

        return random.choice(moves)

    def medium_move(self, moves):
        """
        Medium difficulty.

        Chooses randomly from
        top 5 scoring moves.
        """

        ranked = sorted(
            moves,
            key=lambda move: move.score,
            reverse=True
        )

        top = ranked[:5]

        return random.choice(top)

    def best_move(self, moves):
        """
        Highest-scoring move.
        """

        return max(
            moves,
            key=lambda move: move.score
        )

    # ======================================================
    # MOVE ANALYSIS
    # ======================================================

    def rank_moves(self, moves):
        """
        Return moves sorted by score.
        """

        return sorted(
            moves,
            key=lambda move: move.score,
            reverse=True
        )

    def top_moves(
        self,
        moves,
        limit=10
    ):
        """
        Return top scoring moves.
        """

        ranked = self.rank_moves(moves)

        return ranked[:limit]

    def average_score(self):
        """
        Average move score.
        """

        if self.total_moves == 0:
            return 0

        return (
            self.total_score
            / self.total_moves
        )
"""
ai.py

Artificial Intelligence player for Scrabble.
"""

import random

from src.player import Player
from src.move import Move
from src.move_generator import MoveGenerator


class AIPlayer(Player):
    """
    Computer-controlled Scrabble player.
    """

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    def __init__(self, name="AI", difficulty=MEDIUM):
        """
        Initialize AI player.
        """

        super().__init__(name)

        self.difficulty = difficulty

        self.total_moves = 0
        self.total_score = 0

        self.last_move = None

    # ======================================================
    # MAIN AI
    # ======================================================

    def choose_move(
        self,
        board,
        dictionary,
        scoring
    ):
        """
        Select the best move.
        """

        generator = MoveGenerator(dictionary)

        candidate_moves = generator.generate_moves(
            self.rack
        )

        if not candidate_moves:
            return None

        legal_moves = self.filter_legal_moves(
            board,
            candidate_moves
        )

        if not legal_moves:
            return None

        move = self.select_move(
            legal_moves
        )

        self.last_move = move

        self.total_moves += 1
        self.total_score += move.score

        return move

    # ======================================================
    # FILTER MOVES
    # ======================================================

    def filter_legal_moves(
        self,
        board,
        moves
    ):
        """
        Keep only moves that fit the board.
        """

        legal = []

        for move in moves:

            if board.can_place_word(
                move.word,
                move.row,
                move.column,
                move.direction
            ):

                legal.append(move)

        return legal

    # ======================================================
    # MOVE SELECTION
    # ======================================================

    def select_move(self, moves):
        """
        Select a move depending on
        AI difficulty.
        """

        if self.difficulty == AIPlayer.EASY:
            return self.random_move(moves)

        if self.difficulty == AIPlayer.MEDIUM:
            return self.medium_move(moves)

        return self.best_move(moves)

    def random_move(self, moves):
        """
        Random legal move.
        """

        return random.choice(moves)

    def medium_move(self, moves):
        """
        Medium difficulty.

        Chooses randomly from
        top 5 scoring moves.
        """

        ranked = sorted(
            moves,
            key=lambda move: move.score,
            reverse=True
        )

        top = ranked[:5]

        return random.choice(top)

    def best_move(self, moves):
        """
        Highest-scoring move.
        """

        return max(
            moves,
            key=lambda move: move.score
        )

    # ======================================================
    # MOVE ANALYSIS
    # ======================================================

    def rank_moves(self, moves):
        """
        Return moves sorted by score.
        """

        return sorted(
            moves,
            key=lambda move: move.score,
            reverse=True
        )

    def top_moves(
        self,
        moves,
        limit=10
    ):
        """
        Return top scoring moves.
        """

        ranked = self.rank_moves(moves)

        return ranked[:limit]

    def average_score(self):
        """
        Average move score.
        """

        if self.total_moves == 0:
            return 0

        return (
            self.total_score
            / self.total_moves
        )

    # ======================================================
    # STRATEGY
    # ======================================================

    def evaluate_move(
        self,
        move,
        board,
        scoring
    ):
        """
        Evaluate a move using a heuristic score.

        This method will later be extended with
        Q-learning and pattern recognition.
        """

        score = move.score

        # Prefer longer words
        score += len(move.word)

        # Prefer using more tiles
        score += len(move.word) * 0.5

        return score

    def choose_best_heuristic(
        self,
        board,
        scoring,
        moves
    ):
        """
        Select the move with the highest heuristic value.
        """

        if not moves:
            return None

        best = None
        best_value = float("-inf")

        for move in moves:

            value = self.evaluate_move(
                move,
                board,
                scoring
            )

            if value > best_value:
                best_value = value
                best = move

        return best

    # ======================================================
    # GAME STATISTICS
    # ======================================================

    def reset_statistics(self):
        """
        Reset AI statistics.
        """

        self.total_moves = 0
        self.total_score = 0
        self.last_move = None

    def statistics(self):
        """
        Return AI statistics.
        """

        return {
            "name": self.name,
            "difficulty": self.difficulty,
            "moves": self.total_moves,
            "score": self.total_score,
            "average_score": self.average_score()
        }

    def print_statistics(self):
        """
        Print AI statistics.
        """

        stats = self.statistics()

        print()
        print("=" * 50)
        print("AI STATISTICS")
        print("=" * 50)

        print(f"Name           : {stats['name']}")
        print(f"Difficulty     : {stats['difficulty']}")
        print(f"Moves Played   : {stats['moves']}")
        print(f"Total Score    : {stats['score']}")
        print(f"Average Score  : {stats['average_score']:.2f}")

        print("=" * 50)

    # ======================================================
    # FUTURE RL HOOKS
    # ======================================================

    def observe(
        self,
        state,
        action,
        reward,
        next_state
    ):
        """
        Placeholder for reinforcement learning.

        This will call the Q-learning module later.
        """

        pass

    def train(
        self,
        episodes=1000
    ):
        """
        Placeholder for self-play training.

        Implemented in training.py.
        """

        pass

    # ======================================================
    # REPRESENTATION
    # ======================================================

    def __str__(self):

        return (
            f"AIPlayer("
            f"name={self.name}, "
            f"difficulty={self.difficulty}, "
            f"score={self.score})"
        )

    def __repr__(self):

        return self.__str__()


# ==========================================================
# SIMPLE TEST
# ==========================================================

if __name__ == "__main__":

    ai = AIPlayer(
        "Computer",
        AIPlayer.HARD
    )

    print(ai)

    print()

    ai.print_statistics()
