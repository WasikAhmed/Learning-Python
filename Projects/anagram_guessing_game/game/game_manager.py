from .word_provider import WordProvider
from .player import Player


class GameManager:
    def __init__(self, max_attempts=3):
        self.word_provider = WordProvider()
        self.player = Player()
        self.max_attempts = max_attempts
        self.attempts = 0

    def start_game(self):
        word = self.word_provider.get_random_word()
        anagram = ''.join(sorted(word))

        print("Welcome to the Anagram Guessing Game!")
        print(f"Here is your anagram: {anagram}")
        print(f"You have {self.max_attempts} attempts to guess the correct word")

        while self.attempts < self.max_attempts:
            guess = self.player.get_guess()
            self.attempts += 1
            if self.check_guess(guess, word):
                print("Congratulations!!! You've guessed the word correctly.")
                break
            else:
                remaining_attempts = self.max_attempts - self.attempts
                if remaining_attempts > 0:
                    print(f"Incorrect guess! You have {remaining_attempts} attempts left. Try again.")
                else:
                    print("Incorrect guess! You have no attempts left.")
                    print(f"You've failed! The correct word was: {word}")

    @staticmethod
    def check_guess(guess, word):
        return guess.lower() == word.lower()
