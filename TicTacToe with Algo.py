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

        while self.board.check_win() is None and not self.board.check_draw():
            move = input("Input your move in (x,y): ").split(",")

            while not self.board.make_move(move[1], move[0], "X"):
                move = input("Invalid move, input your move in (x,y): ").split(",")

            print(f"You made the move ({move[1]}, {move[0]}). The current position of the board is: \n \n" + self.board.display() + "\n \n")

            if self.board.check_win():
                break 

            bot_move = self.pick_random()
            self.board.make_move(bot_move[0], bot_move[1], "O")

            print(f"The bot the move ({bot_move[1]}, {bot_move[0]}). The current position of the board is: \n \n" + self.board.display() + "\n \n")
        
        winner = self.board.check_win()

        if winner is not None:
            print("The winner is " + winner + "!")
        else:
            print("The following game ended in a draw!")


    def pick_random(self):
        val = random.choice(self.board.get_available_moves())
        return (val[0] + 1, val[1] + 1)

class PlayProBot(Play):
    def __init__(self):
        Play.__init__(self)

    def start(self):
        pass

    def pick_minimax(self):
        pass

game1 = PlayDumbassBot()
game1.start()