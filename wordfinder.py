from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Create word finder from file path"""
        file = open(path)

        self.words = self.parse(file)

        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<{self.__class__.__name__} len(words={len(self.words)})>"

    def parse(self, file):
        """parse file into list of words"""
        return [line.strip() for line in file]

    def random(self):
        """Return random word from word list"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: finds random words from file with blank lines"""

    def parse(self, file):
        """parse file to list of words, skip blanks/comments"""
        return [word for word in super().parse(file)
                if word != "" and not word.startswith("#")]
