"""
trie.py

Trie (Prefix Tree) implementation for ScrabbleAI.
"""


class TrieNode:
    """
    Represents a single node in the Trie.
    """

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Trie data structure.
    """

    def __init__(self):
        """
        Create an empty Trie.
        """

        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.
        """

        current = self.root

        for letter in word.upper():

            if letter not in current.children:
                current.children[letter] = TrieNode()

            current = current.children[letter]

        current.is_end_of_word = True

    def search(self, word):
        """
        Return True if the complete word exists.
        """

        current = self.root

        for letter in word.upper():

            if letter not in current.children:
                return False

            current = current.children[letter]

        return current.is_end_of_word

    def starts_with(self, prefix):
        """
        Return True if any word begins with prefix.
        """

        current = self.root

        for letter in prefix.upper():

            if letter not in current.children:
                return False

            current = current.children[letter]

        return True

    def __contains__(self, word):
        """
        Allow:

        word in trie
        """

        return self.search(word)
