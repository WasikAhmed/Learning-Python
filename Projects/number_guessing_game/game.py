class Game:
    def welcome(self):
        game_description = '''The main objective of this game is to guess a secret number within a guessing limit.
There are three levels(Easy, Medium, Hard) in this game. Choose your desired level.
Guess limit for each level:
Easy-> 10 times
Medium-> 5 times
Hard-> 3 times

Try your luck!!! Happy gaming!!!
'''
        print('Welcome to my guessing game!!!\n')
        print(game_description)