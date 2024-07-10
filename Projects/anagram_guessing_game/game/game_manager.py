from .word_provider import WordProvider
from .player import Player


class GameManager:
    def __init__(self):
        self.word_provider = WordProvider()
        self.player = Player()

    def start_game(self):
        word = self.word_provider.get_random_word()
        anagram = ''.join(sorted(word))

        print("Welcome to the Anagram Guessing Game!")
        print(f"Here is your anagram: {anagram}")

        while True:
            guess = self.player.get_guess()
            if self.check_guess(guess, word):
                print("Congratulations!!! You've guessed the word correctly.")
                break
            else:
                print("Incorrect guess! Try again.")

    @staticmethod
    def check_guess(guess, word):
        return guess.lower() == word.lower()
