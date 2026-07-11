"""
pattern_recognition.py

Pattern Recognition module for the Scrabble AI.

This module helps the AI:
- Detect anchor squares
- Find playable positions
- Analyze board patterns
- Detect prefixes and suffixes
- Estimate move quality

Later this module will work together with
Q-Learning to improve move selection.
"""

from collections import Counter


class PatternRecognizer:
    """
    Analyze Scrabble board patterns.
    """

    def __init__(self):
        pass

    # =====================================================
    # BOARD ANALYSIS
    # =====================================================

    def occupied_squares(self, board):
        """
        Return all occupied coordinates.
        """

        occupied = []

        for row in range(15):
            for col in range(15):

                if board.grid[row][col] is not None:
                    occupied.append((row, col))

        return occupied

    def empty_squares(self, board):
        """
        Return all empty coordinates.
        """

        empty = []

        for row in range(15):
            for col in range(15):

                if board.grid[row][col] is None:
                    empty.append((row, col))

        return empty

    # =====================================================
    # ANCHOR SQUARES
    # =====================================================

    def anchor_squares(self, board):
        """
        Return playable anchor squares.

        An anchor square is an empty square adjacent
        to an existing tile.
        """

        anchors = []

        for row in range(15):
            for col in range(15):

                if board.grid[row][col] is not None:
                    continue

                if self.has_neighbor(board, row, col):
                    anchors.append((row, col))

        return anchors

    def has_neighbor(self, board, row, col):
        """
        Return True if an adjacent tile exists.
        """

        directions = [

            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)

        ]

        for dr, dc in directions:

            r = row + dr
            c = col + dc

            if (
                0 <= r < 15 and
                0 <= c < 15
            ):

                if board.grid[r][c] is not None:
                    return True

        return False

    # =====================================================
    # PREFIX / SUFFIX
    # =====================================================

    def prefix(self, board, row, col):
        """
        Letters to the left.
        """

        letters = []

        c = col - 1

        while c >= 0:

            value = board.grid[row][c]

            if value is None:
                break

            letters.insert(0, value)

            c -= 1

        return "".join(letters)

    def suffix(self, board, row, col):
        """
        Letters to the right.
        """

        letters = []

        c = col + 1

        while c < 15:

            value = board.grid[row][c]

            if value is None:
                break

            letters.append(value)

            c += 1

        return "".join(letters)

    # =====================================================
    # BOARD DENSITY
    # =====================================================

    def board_density(self, board):
        """
        Percentage of occupied squares.
        """

        occupied = len(self.occupied_squares(board))

        return occupied / (15 * 15)

    # =====================================================
    # LETTER FREQUENCY
    # =====================================================

    def frequency(self, board):
        """
        Count letters currently on board.
        """

        counter = Counter()

        for row in board.grid:

            for tile in row:

                if tile is not None:
                    counter[tile] += 1

        return counter

    # =====================================================
    # OPEN SPACES
    # =====================================================

    def open_spaces(self, board):
        """
        Count empty squares.
        """

        return len(self.empty_squares(board))

    # =====================================================
    # CENTER CONTROL
    # =====================================================

    def center_used(self, board):
        """
        Return True if center square is occupied.
        """

        return board.grid[7][7] is not None

    # =====================================================
    # MOVE FEATURES
    # =====================================================

    def move_features(self, move):
        """
        Extract simple numerical features.
        """

        return {

            "length": len(move.word),

            "score": move.score,

            "row": move.row,

            "column": move.column,

            "horizontal":
                move.direction == "H"

        }

    # =====================================================
    # PATTERN SCORE
    # =====================================================

    def heuristic_score(
        self,
        move,
        board
    ):
        """
        Compute a heuristic score.

        Higher is better.
        """

        score = move.score

        score += len(move.word)

        if self.center_used(board):
            score += 2

        score += self.board_density(board)

        return score

    # =====================================================
    # BEST PATTERN
    # =====================================================

    def best_pattern(
        self,
        moves,
        board
    ):
        """
        Return highest heuristic move.
        """

        if not moves:
            return None

        return max(

            moves,

            key=lambda move:
                self.heuristic_score(
                    move,
                    board
                )

        )


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    print("Pattern Recognition Module Loaded.")
