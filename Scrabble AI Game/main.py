"""
main.py

Main entry point for the Scrabble AI project.
"""

from pathlib import Path

from src.game import Game
from src.training import Trainer


MODEL_PATH = Path("models/q_table.pkl")


def print_menu():
    """
    Display the main menu.
    """

    print()
    print("=" * 60)
    print("SCRABBLE AI")
    print("=" * 60)
    print("1. Play Human vs AI")
    print("2. Train AI")
    print("3. Load Trained Model")
    print("4. Save Current Model")
    print("5. View Training Statistics")
    print("6. Exit")
    print("=" * 60)



def play_game():
    print("Creating Game...")

    game = Game()

    print("Starting Game...")

    game.play()

    print("Game Finished.")



def train_ai():
    """
    Train the AI model.
    """

    try:

        episodes = int(
            input(
                "Number of training episodes: "
            )
        )

    except ValueError:

        episodes = 1000


    try:

        trainer = Trainer(
            episodes=episodes
        )

        trainer.train()

        trainer.evaluate()


    except Exception as error:

        print()
        print("Training error:")
        print(error)



def load_model():
    """
    Load trained Q-learning model.
    """

    if not MODEL_PATH.exists():

        print()
        print("No trained model found.")

        return


    try:

        trainer = Trainer()

        trainer.load_model()


        if hasattr(trainer, "agent"):

            trainer.agent.print_statistics()

        else:

            print(
                "Model loaded successfully."
            )


    except Exception as error:

        print()
        print("Loading error:")
        print(error)



def save_model():
    """
    Save current AI model.
    """

    try:

        Path("models").mkdir(
            exist_ok=True
        )


        trainer = Trainer()

        trainer.save_model()


        print()
        print(
            "Model saved successfully."
        )


    except Exception as error:

        print()
        print("Saving error:")
        print(error)



def show_statistics():
    """
    Display AI statistics.
    """

    if not MODEL_PATH.exists():

        print()
        print(
            "No trained model available."
        )

        return


    try:

        trainer = Trainer()

        trainer.load_model()


        if hasattr(trainer, "agent"):

            trainer.agent.print_statistics()

        else:

            print(
                "Statistics unavailable."
            )


    except Exception as error:

        print()
        print("Statistics error:")
        print(error)



def main():
    """
    Main application loop.
    """

    while True:

        print_menu()


        choice = input(
            "Select an option: "
        ).strip()



        if choice == "1":

            play_game()



        elif choice == "2":

            train_ai()



        elif choice == "3":

            load_model()



        elif choice == "4":

            save_model()



        elif choice == "5":

            show_statistics()



        elif choice == "6":

            print()

            print(
                "Thank you for using Scrabble AI."
            )

            break



        else:

            print()

            print(
                "Invalid choice. Please try again."
            )



if __name__ == "__main__":

    main()
