#Player

import math,random

class Player:
    def __init__(self,letter):#constructor, The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.
        #letter is x or o
        self.letter = letter
    
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):#this class is derived from Player
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        #get a random valid spot
        square = random.choice(game.available_moves)
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Turn move (0-9)')


#Game
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.CurrentWinner = None
    
    def print_board(self):
        #just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        #0 | 1 | 2 etc to tell what number corresponds to which box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     #['x','o','x'] --> [(0,'x'),(1,'o'),(2,'o')]
        #     if spot == ' ':
        #         moves.append(i) 
        # return moves

        #another way to write this
        return [i for i, spot in enumerate(self.board) if  spot == ' ']
