from __future__ import annotations
from TicTacToe import Board
import random

class Play:
    def __init__(self):
        self.board = Board()

    def start(self):
        raise NotImplementedError

class PlayDumbassBot(Play):
    def __init__(self):
        Play.__init__(self)

    def start(self):
        print("Let the games begin! You will be playing as X and the bot will be playing as O. \n")
        print(self.board.display())

        while self.board.check_win() is None and self.board.check_draw():
            move = input("Input your move: ").split(",")
            self.board.make_move(move[0], move[1], "X")

            print(f"You made the move ({move[0]}, {move[1]}). The current position of the board is: \n \n" + self.board.display() + "\n \n")

            move = self.pick_random()
            self.board.make_move(move[0], move[1], "O")

            print(f"The bot the move ({move[0]}, {move[1]}). The current position of the board is: \n \n" + self.board.display() + "\n \n")
        
        if self.board.check_draw():
            print("The following game ended in a draw!")
        else:
            print("The winner is " + self.board.check_win() + "!")

    def pick_random(self):
        return random.choice(self.board.get_available_moves())

class PlayProBot(Play):
    def __init__(self):
        Play.__init__(self)

    def start(self):
        pass

    def pick_minimax(self):
        pass

game1 = PlayDumbassBot()
game1.start()