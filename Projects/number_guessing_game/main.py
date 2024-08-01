# Welcome the player
# Take permission to start or exit the game
# If the user starts the game, take input for game level
# Levels: easy, medium, hard
# In this game the player have to guess the correct number within a guess limit
# Guess limit: easy-> 10 times, medium-> 5 times, hard-> 3 times

from Projects.number_guessing_game.game import Game


def main():
    game = Game()
    game.welcome()


if __name__ == '__main__':
    main()
