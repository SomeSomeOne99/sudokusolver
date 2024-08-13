class Solution(object):
    def checkValid(self, board, position, digit):
        digit = str(digit)
        for row in range(9): # same column
            if board[position[0]][row] == digit and row != position[1]:
                return False
            if board[row][position[1]] == digit and row != position[0]:
                return False
        for column in range(3 * (position[0]//3), 3*(position[0]//3) + 3):
            for row in range(3 * (position[1]//3), 3*(position[1]//3) + 3):
                if board[column][row] == digit and row != position[1] and column != position[0]:
                    return False
        return True
    def solveSudoku(self, board):
        for column in range(9):
            for row in range(9):
                if board[column][row] == ".":
                    for digit in range(9, 0, -1): #range(1, 10): #
                        valid = self.checkValid(board, (column, row), digit)
                        if valid:
                            board[column][row] = str(digit)
                            calculation = self.solveSudoku(board)
                            if calculation == None:
                                board[column][row] = "."
                                continue
                            return calculation
                    return None
        return board
