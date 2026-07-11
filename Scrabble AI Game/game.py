"""
game.py

Main Scrabble game engine.
"""

from src.board import Board
from src.bag import TileBag
from src.player import Player
from src.dictionary import Dictionary
from src.move_generator import MoveGenerator
from src.scoring import Scoring
from src.ai import AIPlayer

from src.utils import (
    title,
    print_board,
    print_rack,
    print_score,
    game_over
)


class Game:
    """
    Main Scrabble Game Engine.
    """

    def __init__(self):
        """
        Initialize a new Scrabble game.
        """

        # Create board
        self.board = Board()

        # Tile bag
        self.bag = TileBag()

        # Dictionary
        self.dictionary = Dictionary()

        # Scoring engine
        self.scoring = Scoring()

        # Move generator
        self.generator = MoveGenerator(self.dictionary)

        # Human player
        self.human = Player("Human")

        # AI player
        self.ai = AIPlayer("Computer")

        # Players
        self.players = [
            self.human,
            self.ai
        ]

        # Current turn
        self.current_player = 0

        # Give players starting tiles
        self.initialize_players()


    def initialize_players(self):
        """
        Give each player 7 tiles.
        """

        for player in self.players:

            while len(player.rack) < 7:

                tile = self.bag.draw_tile()

                if tile is None:
                    break

                player.add_tile(tile)


    def active_player(self):
        """
        Return current player.
        """

        return self.players[self.current_player]


    def switch_turn(self):
        """
        Switch player turn.
        """

        self.current_player = (
            self.current_player + 1
        ) % len(self.players)


    def refill_rack(self, player):
        """
        Draw tiles until player has 7 tiles.
        """

        while len(player.rack) < 7:

            tile = self.bag.draw_tile()

            if tile is None:
                break

            player.add_tile(tile)


    def show_status(self):
        """
        Display current board and scores.
        """

        title("SCRABBLE AI")

        print_board(self.board.grid)

        print()

        print_score(self.human)
        print_score(self.ai)

        print()

        print(
            "Tiles Remaining:",
            len(self.bag.tiles)
        )

        print()


    def human_turn(self):
        """
        Handle human player's turn.
        """

        player = self.human

        print()
        print("YOUR TURN")
        print()

        print_rack(player.rack)

        word = input(
            "Word (PASS to skip): "
        ).upper()


        if word == "PASS":
            return


        if not self.dictionary.is_word(word):

            print("Invalid word.")

            return


        if not player.has_tiles(word):

            print(
                "You don't have those letters."
            )

            return


        row = int(
            input("Row: ")
        )


        column = int(
            input("Column: ")
        )


        direction = input(
            "Direction (H/V): "
        ).upper()


        success = self.board.place_word(
            word,
            row,
            column,
            direction
        )


        if not success:

            print(
                "Cannot place word."
            )

            return


        score = self.scoring.score_word(word)

        player.score += score

        player.remove_tiles(word)

        self.refill_rack(player)


        print(
            f"You scored {score} points."
        )


    def ai_turn(self):
        """
        Handle AI player's turn.
        """

        player = self.ai


        print()
        print("AI THINKING...")


        move = player.choose_move(
            self.board,
            self.dictionary,
            self.scoring
        )


        if move is None:

            print("AI PASSES")

            return


        success = self.board.place_word(
            move.word,
            move.row,
            move.column,
            move.direction
        )


        if not success:

            print(
                "AI failed to place word."
            )

            return


        player.score += move.score

        player.remove_tiles(move.word)

        self.refill_rack(player)


        print()

        print(
            f"AI played {move.word}"
        )

        print(
            f"Score +{move.score}"
        )


    def play_turn(self):
        """
        Play one complete turn.
        """

        player = self.active_player()

        print()
        print("=" * 60)
        print(f"{player.name}'s Turn")
        print("=" * 60)


        if player == self.human:

            self.human_turn()

        else:

            self.ai_turn()


        self.switch_turn()


    def display_scores(self):
        """
        Display current scores.
        """

        print()

        print("=" * 40)
        print("SCORES")
        print("=" * 40)


        for player in self.players:

            print(
                f"{player.name:<12}: {player.score}"
            )


        print("=" * 40)



    def winner(self):
        """
        Return player with highest score.
        """

        return max(
            self.players,
            key=lambda player: player.score
        )



    def display_winner(self):
        """
        Display final winner.
        """

        winner = self.winner()

        print()

        print("=" * 60)
        print("GAME OVER")
        print("=" * 60)


        print(
            f"Winner : {winner.name}"
        )

        print(
            f"Score  : {winner.score}"
        )


        print()


        for player in self.players:

            print(
                f"{player.name:<12}: {player.score}"
            )


        print("=" * 60)



    def play(self):
        """
        Main game loop.
        """

        while not game_over(
            self.players,
            self.bag
        ):

            self.show_status()

            self.play_turn()


        self.display_winner()



    # ======================================================
    # SAVE / LOAD
    # ======================================================


    def save(self, filename):
        """
        Save current game.
        """

        import pickle


        with open(filename, "wb") as file:

            pickle.dump(
                self,
                file
            )


        print(
            f"Game saved to '{filename}'"
        )



    @staticmethod
    def load(filename):
        """
        Load saved game.
        """

        import pickle


        with open(filename, "rb") as file:

            game = pickle.load(file)


        print(
            f"Game loaded from '{filename}'"
        )


        return game



    # ======================================================
    # RESTART
    # ======================================================


    def restart(self):
        """
        Restart game.
        """

        self.__init__()



    # ======================================================
    # DEBUG
    # ======================================================


    def debug(self):
        """
        Print debugging information.
        """

        print()

        print("=" * 60)
        print("DEBUG INFORMATION")
        print("=" * 60)


        print(
            f"Current Player : {self.active_player().name}"
        )


        print(
            f"Tiles Left     : {len(self.bag.tiles)}"
        )


        print()


        for player in self.players:

            print(player.name)

            print(
                f"Score : {player.score}"
            )

            print(
                f"Rack  : {' '.join(player.rack)}"
            )

            print()


        print("=" * 60)



# ==========================================================
# STANDALONE EXECUTION
# ==========================================================


if __name__ == "__main__":

    game = Game()

    game.play()
