"""
utils.py

General utility functions used throughout the Scrabble AI project.
"""

from __future__ import annotations

import json
import pickle
import random
import string
from pathlib import Path
from typing import Iterable, List, Tuple

BOARD_SIZE = 15


# ==========================================================
# FILE UTILITIES
# ==========================================================

def ensure_directory(path: str | Path):
    """
    Create directory if it does not exist.
    """

    Path(path).mkdir(parents=True, exist_ok=True)


def file_exists(path: str | Path) -> bool:
    """
    Return True if file exists.
    """

    return Path(path).exists()


def load_json(path: str | Path):
    """
    Load JSON file.
    """

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path: str | Path, data):
    """
    Save JSON file.
    """

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_pickle(path: str | Path):
    """
    Load pickle object.
    """

    with open(path, "rb") as file:
        return pickle.load(file)


def save_pickle(path: str | Path, obj):
    """
    Save pickle object.
    """

    with open(path, "wb") as file:
        pickle.dump(obj, file)


# ==========================================================
# RANDOM UTILITIES
# ==========================================================

def random_letter():
    """
    Return a random uppercase letter.
    """

    return random.choice(string.ascii_uppercase)


def random_letters(count: int):
    """
    Return list of random letters.
    """

    return [random_letter() for _ in range(count)]


def shuffle_tiles(tiles: List[str]):
    """
    Shuffle tiles in place.
    """

    random.shuffle(tiles)
    return tiles


# ==========================================================
# BOARD UTILITIES
# ==========================================================

def is_valid_coordinate(row: int, column: int):
    """
    Return True if coordinate lies on board.
    """

    return (
        0 <= row < BOARD_SIZE
        and
        0 <= column < BOARD_SIZE
    )


def board_center():
    """
    Return center coordinate.
    """

    return (7, 7)


def neighbors(row: int, column: int):
    """
    Return adjacent coordinates.
    """

    results = []

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:

        nr = row + dr
        nc = column + dc

        if is_valid_coordinate(nr, nc):
            results.append((nr, nc))

    return results


# ==========================================================
# STRING UTILITIES
# ==========================================================

def clean_word(word: str):
    """
    Remove whitespace and uppercase.
    """

    return word.strip().upper()


def is_alpha(word: str):
    """
    Return True if word contains only letters.
    """

    return word.isalpha()


def letters(word: str):
    """
    Convert word into list of letters.
    """

    return list(clean_word(word))


def join_letters(chars: Iterable[str]):
    """
    Join letters into a string.
    """

    return "".join(chars)


# ==========================================================
# RACK UTILITIES
# ==========================================================

def rack_contains_word(rack, word):
    """
    Return True if the rack contains all letters
    needed to build the given word.

    Supports Tile objects and strings.
    """

    rack_letters = []

    for tile in rack:

        if isinstance(tile, str):

            rack_letters.append(tile.upper())

        elif hasattr(tile, "letter"):

            rack_letters.append(tile.letter.upper())

        else:

            rack_letters.append(str(tile).upper())

    for letter in word.upper():

        if letter not in rack_letters:
            return False

        rack_letters.remove(letter)

    return True


def remove_letters(rack, word):
    """
    Remove letters from a rack.

    Supports Tile objects and strings.
    """

    rack = list(rack)

    for letter in word.upper():

        for tile in rack:

            tile_letter = (
                tile if isinstance(tile, str)
                else tile.letter
            )

            if tile_letter.upper() == letter:

                rack.remove(tile)

                break

    return rack

def add_letters(rack, letters):
    """
    Add letters or Tile objects to the rack.
    """

    rack = list(rack)

    for letter in letters:

        rack.append(letter)

    return rack


# ==========================================================
# DISPLAY UTILITIES
# ==========================================================

def divider(length=60):
    print("=" * length)


def title(text):
    divider()
    print(text)
    divider()


def print_rack(rack):
    """
    Display a player's rack.

    Works with both strings and Tile objects.
    """

    letters = []

    for tile in rack:

        if isinstance(tile, str):

            letters.append(tile)

        elif hasattr(tile, "letter"):

            letters.append(tile.letter)

        else:

            letters.append(str(tile))

    print("Rack:", " ".join(letters))


def print_score(player):
    """
    Display player score.
    """

    print(f"{player.name}: {player.score}")


# ==========================================================
# STATISTICS
# ==========================================================

def average(values):
    """
    Compute average.
    """

    if not values:
        return 0

    return sum(values) / len(values)


def maximum(values):

    if not values:
        return 0

    return max(values)


def minimum(values):

    if not values:
        return 0

    return min(values)


def clamp(value, low, high):
    """
    Clamp value between low and high.
    """

    return max(low, min(high, value))

# ==========================================================
# WORD UTILITIES
# ==========================================================

def word_score(word, scoring):
    """
    Return score of a word using the scoring engine.
    """

    return scoring.score_word(word)


def longest_word(words):
    """
    Return the longest word.
    """

    if not words:
        return ""

    return max(words, key=len)


def shortest_word(words):
    """
    Return the shortest word.
    """

    if not words:
        return ""

    return min(words, key=len)


def sort_words(words):
    """
    Return alphabetically sorted words.
    """

    return sorted(words)


def unique_words(words):
    """
    Remove duplicate words.
    """

    return sorted(set(words))


# ==========================================================
# MOVE UTILITIES
# ==========================================================

def sort_moves_by_score(moves):
    """
    Sort moves by descending score.
    """

    return sorted(
        moves,
        key=lambda move: move.score,
        reverse=True
    )


def best_move(moves):
    """
    Return highest-scoring move.
    """

    if not moves:
        return None

    return max(
        moves,
        key=lambda move: move.score
    )


def top_moves(moves, limit=10):
    """
    Return top scoring moves.
    """

    return sort_moves_by_score(moves)[:limit]


# ==========================================================
# BOARD DISPLAY
# ==========================================================

def print_board(board):
    """
    Display a board in the console.
    """

    divider(70)

    print("   ", end="")

    for column in range(15):
        print(f"{column:2}", end=" ")

    print()

    divider(70)

    for row in range(15):

        print(f"{row:2}|", end=" ")

        for column in range(15):

            cell = board[row][column]

            if cell is None:
                cell = "."

            print(f"{cell:2}", end=" ")

        print()

    divider(70)


# ==========================================================
# GAME STATUS
# ==========================================================

def game_over(players, bag):
    """
    Determine if the game has finished.

    Game ends when:
        - Tile bag is empty
        - One player has no tiles
    """

    if len(bag.tiles) > 0:
        return False

    for player in players:

        if len(player.rack) == 0:
            return True

    return False


# ==========================================================
# SERIALIZATION
# ==========================================================

def save_game(filename, game):
    """
    Save game object.
    """

    save_pickle(filename, game)


def load_game(filename):
    """
    Load game object.
    """

    return load_pickle(filename)


# ==========================================================
# LOGGING
# ==========================================================

def log(message):
    """
    Print log message.
    """

    print(f"[LOG] {message}")


def warning(message):
    """
    Print warning.
    """

    print(f"[WARNING] {message}")


def error(message):
    """
    Print error.
    """

    print(f"[ERROR] {message}")


# ==========================================================
# DEBUGGING
# ==========================================================

def debug_board(board):
    """
    Print board for debugging.
    """

    title("BOARD DEBUG")

    print_board(board)


def debug_rack(player):
    """
    Print player's rack.
    """

    title(player.name)

    print_rack(player.rack)

    print_score(player)


# ==========================================================
# COORDINATE HELPERS
# ==========================================================

def move_coordinates(row, column, word, horizontal=True):
    """
    Return coordinates occupied by a word.
    """

    coords = []

    for index in range(len(word)):

        if horizontal:
            coords.append((row, column + index))
        else:
            coords.append((row + index, column))

    return coords


def fits_board(row, column, word, horizontal=True):
    """
    Check if a word fits on the board.
    """

    if horizontal:
        return column + len(word) <= BOARD_SIZE

    return row + len(word) <= BOARD_SIZE


# ==========================================================
# LETTER FREQUENCIES
# ==========================================================

def frequency(word):
    """
    Count letter frequencies.
    """

    counts = {}

    for letter in word.upper():

        counts[letter] = counts.get(letter, 0) + 1

    return counts


# ==========================================================
# TIMER
# ==========================================================

class Timer:
    """
    Simple execution timer.
    """

    def __init__(self):
        import time
        self.time = time
        self.start_time = None

    def start(self):
        self.start_time = self.time.time()

    def stop(self):
        return self.time.time() - self.start_time
