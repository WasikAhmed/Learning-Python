import random


class WordProvider:
    def __init__(self, filepath="data/words.txt"):
        self.filepath = filepath

    def get_random_word(self):
        with open(self.filepath, 'r') as file:
            words = file.read().splitlines()
        return random.choice(words)
