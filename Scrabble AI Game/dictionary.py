"""
dictionary.py

Loads and manages Scrabble dictionary words.
"""

from pathlib import Path


class Dictionary:
    """
    Loads dictionary words from a text file.
    """

    def __init__(self, filename="data/dictionary.txt"):
        self.words = set()

        path = Path(filename)

        if not path.exists():
            raise FileNotFoundError(
                f"Dictionary file not found: {path.resolve()}"
            )

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip().upper()

                if word:
                    self.words.add(word)

    def is_word(self, word):
        """
        Return True if word exists.
        """
        return word.upper() in self.words

    def __contains__(self, word):
        return self.is_word(word)

    def __len__(self):
        return len(self.words)

    def all_words(self):
        return sorted(self.words)
