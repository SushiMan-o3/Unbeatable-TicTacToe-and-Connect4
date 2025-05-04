from __future__ import annotations
from typing import List, Optional
from TicTacToe import Board
import random
from Connect4 import Connect4
import json 

class PlayTicacToe:
    """
    A class representing a Tic Tac Toe game."""
    def __init__(self):
        """
        Initialize the game with a Tic Tac Toe board."""
        self.board = Board()

    def start(self):
        """
        Start the game. This method should be overridden in subclasses.
        """
        raise NotImplementedError

class PlayDumbassBot(PlayTicacToe):
    """
    A class representing a Tic Tac Toe game with a dumb bot."""
    def __init__(self):
        """
        Initialize the game with a Tic Tac Toe board."""
        PlayTicacToe.__init__(self)

    def start(self):
        """
        Start the game with a dumb bot. The bot makes random moves.
        """  
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
        """
        Pick a random move from the available moves on the board.
        Returns a tuple (row, col) representing the move.
        """
        val = random.choice(self.board.get_available_moves())
        return (val[0] + 1, val[1] + 1)

class PlayProBot(PlayTicacToe):
    """
    A class representing a Tic Tac Toe game with a professional bot.
    The bot uses the minimax algorithm to make optimal moves.
    """
    def __init__(self):
        PlayTicacToe.__init__(self)

    def start(self):
        """
        Start the game with a professional bot. The bot uses the 
        minimax algorithm to make optimal moves.
        """
        print("Let the games begin! You will be playing as X and the bot will be playing as O. \n")
        print(self.board.display())

        while self.board.check_win() is None and not self.board.check_draw():
            move = input("Input your move in (x,y): ").split(",")

            while not self.board.make_move(move[1], move[0], "X"):
                move = input("Invalid move, input your move in (x,y): ").split(",")

            print(f"You made the move ({move[1]}, {move[0]}). The current position of the board is: \n \n" + self.board.display() + "\n \n")

            if self.board.check_win() or self.board.check_draw():
                break 

            bot_move = self.minimax(self.board.board, 9, "O")

            self.board.make_move(bot_move[0]+1, bot_move[1]+1, "O")

            print(f"The bot the move ({bot_move[1]+1}, {bot_move[0]+1}). The current position of the board is: \n \n" + self.board.display() + "\n \n")
        
        winner = self.board.check_win()

        if winner is not None:
            print("The winner is " + winner + "!")
        else:
            print("The following game ended in a draw!")

    def minimax(self, position: List[List[str]], depth: int, max_player: str) -> tuple[int, int]:
        """
        Minimax algorithm to find the best move for the bot.
        The bot is the minimizing player and the player is the maximizing player.
        The function returns the best move for the bot. 
        """
        # so the minimizing player is O (the bot) and the maximizing player is X (the player)
        def helper(position: List[List[str]], depth: int, max_player: str):
            temp_board = Board(position)
            evaluation = temp_board.check_win()

            # base cases 
            if evaluation == "X":
                return -1, None
            if evaluation == "O":
                return 1, None
            if temp_board.check_draw():
                return 0, None

            best_move = random.choice(temp_board.get_available_moves())

            if max_player == "O":
                best_score = float("-inf")
            else:
                best_score = float("inf")
            
            for move in temp_board.get_available_moves():
                temp_board2 = Board(position)
                temp_board2.make_move(move[0]+1, move[1]+1, max_player)
                val = helper(temp_board2.board, depth-1, "X" if max_player == "O" else "O")

                if max_player == "O":
                    if val[0] > best_score:
                        best_score = val[0]
                        best_move = move
                else:
                    if val[0] < best_score:
                        best_score = val[0]
                        best_move = move

            return best_score, best_move
                
        return helper(position, depth, max_player)[1]
        

class PlayConnect4:
    """
    A class representing a Connect 4 game."""
    def __init__(self):
        """
        Initialize the game with a Connect 4 board."""
        self.board = Connect4()

    def start(self):
        """
        Start the game. This method should be overridden in subclasses.
        """
        raise NotImplementedError
    
class PlayStupidBot(PlayConnect4):
    """
    A class representing a Connect 4 game with a stupid bot."""
    def __init__(self):
        """
        Initialize the game with a Connect 4 board."""
        PlayConnect4.__init__(self)

    def start(self):
        """
        Start the game with a stupid bot. The bot makes random moves.
        """  
        print("Let the games begin! You will be playing as X and the bot will be playing as O. \n")
        print(self.board)

        while self.board.check_win() is None and not self.board.check_draw():
            move = int(input("Input your move: "))

            while not self.board.drop_disc(move, 1):
                move = int(input("Invalid move, input your move: "))

            print(f"You made dropped it at {move}. The current position of the board is: \n \n")
            print(self.board)

            if self.board.check_win():
                break 

            bot_move = self.pick_random()
            self.board.drop_disc(bot_move, 2)
        
        winner = self.board.check_win()

        if winner is not None:
            print("The winner is player" + str(winner) + "!")
        else:
            print("The following game ended in a draw!")

    def pick_random(self):
        """
        Pick a random move from the available moves on the board.
        Returns a column representing the move.
        """
        return random.choice(self.board.get_available_moves())


class PlayGenuis(PlayConnect4):
    """
    A class representing a Connect 4 game with a stupid bot."""
    def __init__(self):
        """
        Initialize the game with a Connect 4 board."""
        PlayConnect4.__init__(self)

    def start(self):
        """
        Start the game with a stupid bot. The bot makes random moves.
        """  
        print("Let the games begin! You will be playing as X and the bot will be playing as O. \n")
        print(self.board)

        while self.board.check_win() is None and not self.board.check_draw():
            move = int(input("Input your move: "))

            while not self.board.drop_disc(move, 1):
                move = int(input("Invalid move, input your move: "))

            print(f"You made dropped it at {move}. The current position of the board is: \n \n")
            print(self.board)

            if self.board.check_win():
                break 

            bot_move = self.minimax(self.board.board, 7, 2)
            self.board.drop_disc(bot_move+1, 2)

            print(f"The bot dropped it at {bot_move+1}. The current position of the board is: \n \n")
            print(self.board)
        
        winner = self.board.check_win()

        if winner is not None:
            print("The winner is player" + str(winner) + "!")
        else:
            print("The following game ended in a draw!")
    

    def minimax(self, position: List[List[str]], depth: int, max_player: str) -> int:
        """
        Pick a random move from the available moves on the board.
        Returns a column representing the move.
        """
        def helper(position: List[List[str]], depth: int, alpha, beta, max_player: str):
            with open('data.json', 'r') as file:
                data = json.load(file)
                if self.board.serialize() in data:
                    return data[self.board.serialize()]

            temp_board = Connect4(position)
            evaluation = temp_board.check_win()

            # base cases 
            if evaluation == 1:
                return -1, None
            if evaluation == 2:
                return 1, None
            if temp_board.check_draw() or depth == 0:
                return 0, None

            best_move = random.choice(temp_board.get_available_moves())

            if max_player == 2:
                best_score = float("-inf")
            else:
                best_score = float("inf")
            
            for move in temp_board.get_available_moves():
                temp_board2 = Connect4(position)
                temp_board2.drop_disc(move+1, max_player)
                val = helper(temp_board2.board, depth-1, alpha, beta, 1 if max_player == 2 else 2)

                if max_player == 2:
                    if val[0] > best_score:
                        best_score = val[0]
                        best_move = move

                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
                else:
                    if val[0] < best_score:
                        best_score = val[0]
                        best_move = move

                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break

            return best_score, best_move
        return helper(position, depth, float('-inf'), float('inf'), max_player)[1]
    
g = PlayGenuis()
g.start()