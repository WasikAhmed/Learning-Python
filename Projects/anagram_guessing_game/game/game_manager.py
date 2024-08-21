from .word_provider import WordProvider
from .player import Player
from .user import User


class GameManager:
    def __init__(self, max_attempts=3):
        self.word_provider = WordProvider()
        self.player = Player()
        self.max_attempts = max_attempts
        self.attempts = 0
        self.user = None

    def start_game(self):
        self.authenticate_user()
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
                self.user.update_stat(won=True)
                self.user.save_user()
                return  # Exit the loop if the user wins
            else:
                remaining_attempts = self.max_attempts - self.attempts  # Corrected this line
                if remaining_attempts > 0:
                    print(f"Incorrect guess! You have {remaining_attempts} attempts left. Try again.")
                else:
                    print("Incorrect guess! You have no attempts left.")

        print(f"You've failed! The correct word was: {word}")
        self.user.update_stat(won=False)
        self.user.save_user()

    @staticmethod
    def check_guess(guess, word):
        return guess.lower() == word.lower()

    def authenticate_user(self):
        print("Please log in or sign up:")
        while True:
            choice = input("Do you have an account? (yes/no): ").strip().lower()
            if choice == 'yes':
                username = input("Enter your username: ").strip()
                password = input("Enter your password: ").strip()
                user = User.authenticate(username, password)
                if user:
                    print("Login successful!")
                    self.user = user
                    break
                else:
                    print("Incorrect username or password. Please try again.")
            elif choice == 'no':
                username = input("Choose a username: ").strip()
                password = input("Choose a password: ").strip()
                user = User(username, password)
                user.save_user()
                print("Account created successfully!")
                self.user = user
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
