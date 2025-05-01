from __future__ import annotations
from typing import List, Optional, Tuple
from colorama import Fore, Style

class Connect4:
    """
    A class to represent a Connect 4 game. The game is played on a 6x7 grid, where 
    two players take turns dropping discs into columns. The objective is to connect 
    four discs in a row, either horizontally, vertically, or diagonally.
    """
    def __init__(self, board: Optional[List[List[int]]] = None):
        if not board or len(board) != 6:
            self.board = [[0] * 7 for _ in range(6)]
        else:
            self.board = [row.copy() for row in board]

    def __str__(self):
        rtn = ""
        for row in self.board:
            colored_row = []
            for cell in row:
                if cell == 1:
                    colored_cell = Fore.RED + str(cell) + Style.RESET_ALL
                elif cell == 2:
                    colored_cell = Fore.BLUE + str(cell) + Style.RESET_ALL
                else:
                    colored_cell = str(cell)
                colored_row.append(colored_cell)
            rtn += "|".join(colored_row) + "\n"
            rtn += "-" * 14 + "\n"
        rtn += "1|2|3|4|5|6|7\n"
        return rtn
    
    def drop_disc(self, column: int, player: int) -> bool:
        """
        Drop a disc into the specified column for the given player.
        Returns True if the move was successful, False if the column is full.
        """
        row = 0

        while row < 6 and self.board[row][column-1] == 0:
            row += 1
        
        if row == 0:
            return False
        else:
            self.board[row-1][column-1] = player
            return True

    def check_win(self):
        def check_row(row: List[int]):
            for index in range(len(row)-4):
                if row[index] != 0 and row[index] == row[index+1] == row[index+2] == row[index+3]:
                    return row[index]
            return None
                
        def check_column(column: int):
            for row in range(len(self.board)-4):
                if self.board[row][column] != 0 and self.board[row][column] == self.board[row+1][column] == self.board[row+2][column] == self.board[row+3][column]:
                    return self.board[row][column]
            return None
                
        def check_diagonal():
            for row in range(3, 6):
                for column in range(4):
                    if self.board[row][column] != 0 and self.board[row][column] == self.board[row-1][column+1] == self.board[row-2][column+2] == self.board[row-3][column+3]:
                        return self.board[row][column]
            for row in range(3):
                for column in range(4):
                    if self.board[row][column] != 0 and self.board[row][column] == self.board[row+1][column+1] == self.board[row+2][column+2] == self.board[row+3][column+3]:
                        return self.board[row][column]
            return None


        for row in self.board:
            if check_row(row):
                return check_row(row)

        for column in range(6):
            if check_column(column):
                return check_column(column)

        if check_diagonal():
            return check_diagonal()
        
        return None
    
    def check_draw(self):
        """
        Check if the game is a draw. A draw occurs when the board is full and there are no winners.
        """
        if self.check_win():
            return False
        
        for row in self.board:
            for val in row:
                if val == 0:
                    return False
                
        return True
    
    def get_available_moves(self) -> List[int]:
        """
        Get a list of available moves (columns) where a disc can be dropped.
        """
        lst = []

        for val in range(len(self.board[0])):
            if self.board[0][val] == 0:
                lst.append(val)
        
        return lst