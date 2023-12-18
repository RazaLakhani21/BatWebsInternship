import math
import random

class Player:
    def __init__(self,letter):
        #letter is c or o
        self.letter = letter

        #we want all players to gettheir next move given a game
        def get_move(self,game):
            pass

class RandomComputerPlayer(Player):
    def __inti__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        #get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square
        

class HumanPlayer(Player):
    def __inti__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-8):')
            #
            #
            #
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again.')

        return val
