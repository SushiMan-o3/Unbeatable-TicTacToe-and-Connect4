from __future__ import annotations
from typing import List, Optional
from Connect4 import Connect4, evaluate_board
import random
import json

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


class PlayPro(PlayConnect4):
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
    

    def minimax(self, position: List[List[int]], depth: int, max_player: int) -> int:
        original_player = max_player
        max_depth = depth

        def helper(position: List[List[int]], depth: int, alpha, beta, current_player: int):
            temp_board = Connect4(position)
            winner = temp_board.check_win()

            if winner == original_player:
                return 1000 - (max_depth - depth), None
            elif winner == (3 - original_player):
                return -1000 + (max_depth - depth), None
            elif temp_board.check_draw():
                return 0, None
            elif depth == 0:
                return evaluate_board(temp_board, original_player), None

            best_move = temp_board.get_available_moves()[0]
            if current_player == original_player:
                best_score = float("-inf")
            else:
                best_score = float("inf")

            for move in temp_board.get_available_moves():
                new_board = Connect4(position)
                new_board.drop_disc(move + 1, current_player)
                score, _ = helper(new_board.board, depth - 1, alpha, beta, 3 - current_player)

                if current_player == original_player:
                    if score > best_score:
                        best_score = score
                        best_move = move
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
                else:
                    if score < best_score:
                        best_score = score
                        best_move = move
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break

            return best_score, best_move

        try:
            with open('opening_book.json', 'r') as file:
                opening_book = json.load(file)
                key = self.board.serialize()
                if key in opening_book:
                    return opening_book[key]
        except FileNotFoundError:
            pass

        return helper(position, depth, float('-inf'), float('inf'), max_player)[1]

