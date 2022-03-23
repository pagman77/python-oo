from random import sample


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Create word finder from file path"""
        self.path = path
        self.words = self.read_file()
        self.print_word()

    def __repr__(self):
        return f"<Word Finder path = {self.path}>"

    def read_file(self):
        """Read file and return word list"""
        file = open(self.path)
        word_list = []
        for line in file:
            word_list.append(line)
        return word_list

    def print_word(self):
        """Print word count to console"""
        print(f"{len(self.words)} words read")

    def random(self):
        """Return random word from word list"""
        random_word = sample(self.words, k=1)[0]
        if random_word.endswith("\n"):
            return random_word[:len(random_word)-1]
        return random_word


class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: finds random words from file with blank lines"""

    def __init__(self, path):
        super().__init__(path)

    def special_word_list(self):
        """return word list without blanks or lines that start with #"""
        return [line for line in self.words if line[0].isalpha()]

    def special_random(self):
        """Return random word from special word list"""
        random_word = sample(self.special_word_list(), k=1)[0]
        if random_word.endswith("\n"):
            return random_word[:len(random_word)-1]
        return random_word

    def print_word(self):
        """Print special word count to console"""
        print(f"{len(self.special_word_list())} words read")
