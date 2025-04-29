from __future__ import annotations
from typing import List, Optional
import copy

class Board:
    """
    A class representing a Tic Tac Toe board.  
    """
    def __init__(self, board: Optional[List[List[str]]]):
        """
        Initialize the Tic Tac Toe board with empty cells. 
        The board is represented as a 3x3 grid with each cell initialized to "."
        """
        if board is None or len(board) != 3:
            self.board = [
                [".", ".", "."],
                [".", ".", "."],
                [".", ".", "."]
            ]
        else:
            self.board = [row.copy() for row in board]	

    def display(self) -> str:
        """
        Display the current state of the board in a readable format.
        Each cell is separated by a pipe (|) and rows are separated by dashes.
        """
        display_str = ""
        for row in self.board:
            display_str += " | ".join(row) + "\n"
            display_str += "-" * 9 + "\n"
        return display_str
    
    def get_available_moves(self) -> List[tuple[int, int]]:
        """
        Get a list of available moves on the board.
        Each move is represented as a tuple (row, col).
        """
        avaliable_moves = []

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ".":
                    avaliable_moves.append((row, col))
        
        return avaliable_moves

    def make_move(self, row: str, col: str, player: str) -> bool:
        """
        Make a move on the board for the given player at the specified row and column.
        The row and column are expected to be 1-indexed (1-3).
        The player should be either "X" or "O".
        Returns True if the move was successful, False otherwise.
        """
        row, col = int(row) - 1, int(col) - 1

        if not (0 <= row <= 2) or not (0 <= col <= 2):
            return False
        if player.upper() not in ["X", "O"]:
            return False
        
        if self.board[row][col] == ".":
            self.board[row][col] = player.upper()
            return True
        
        return False
    
    def check_win(self) -> Optional[str]:
        """
        Check if there is a winning condition on the board.
        A player wins if they have three of their marks in a row, column, or diagonal.
        """
        for row in self.board:
            if row[0] != "." and row[0] == row[1] == row[2]:
                return row[0]

        for col in range(3):
            if self.board[0][col] != "." and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.board[0][col]

        if self.board[0][0] != "." and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != "." and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None

    def check_draw(self) -> bool:
        """
        Check if the game is a draw.
        A draw occurs when all cells are filled and there is no winner.
        """
        if self.check_win() is not None:
            return False
        
        for row in self.board:
            for col in row:
                if col == ".":
                    return False
                
        return True