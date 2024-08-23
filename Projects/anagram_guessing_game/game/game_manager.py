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

        while True:
            print("\n--- Main Menu ---")
            print("1. Play Game")
            print("2. View Profile")
            print("3. Update Profile")
            print("4. Logout")
            choice = input("Select an option: ").strip()

            if choice == '1':
                self.play_game()
            elif choice == '2':
                self.view_profile()
            elif choice == '3':
                self.update_profile()
            elif choice == '4':
                print("Logging out...")
                self.user = None
                self.authenticate_user()
            else:
                print("Invalid option. Please choose again.")

    def play_game(self):
        word = self.word_provider.get_random_word()
        anagram = ''.join(sorted(word))

        print("Welcome to the Anagram Guessing Game!")
        print(f"Here is your anagram: {anagram}")
        print(f"You have {self.max_attempts} attempts to guess the correct word")

        self.attempts = 0
        while self.attempts < self.max_attempts:
            guess = self.player.get_guess()
            self.attempts += 1
            if self.check_guess(guess, word):
                print("Congratulations!!! You've guessed the word correctly.")
                self.user.update_stat(won=True)
                self.user.save_user()
                return  # Exit the loop if the user wins
            else:
                remaining_attempts = self.max_attempts - self.attempts
                if remaining_attempts > 0:
                    print(f"Incorrect guess! You have {remaining_attempts} attempts left. Try again.")
                else:
                    print("Incorrect guess! You have no attempts left.")

        print(f"You've failed! The correct word was: {word}")
        self.user.update_stat(won=False)
        self.user.save_user()

    def view_profile(self):
        print("\n--- Profile Details ---")
        print(f"Username: {self.user.username}")
        print(f"Wins: {self.user.wins}")
        print(f"Losses: {self.user.losses}")

    def update_profile(self):
        print("\n--- Update Profile ---")
        new_username = input("Enter new username (leave blank to keep current): ").strip()
        new_password = input("Enter new password (leave blank to keep current): ").strip()

        if new_username:
            self.user.username = new_username
        if new_password:
            self.user.password = User._hash_password(new_password)

        self.user.save_user()
        print("Profile updated successfully!")

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
