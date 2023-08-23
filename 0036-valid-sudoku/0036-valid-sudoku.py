class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkSet = set()

        # Check rows
        for i in range(len(board)):
            checkSet.clear()  # Clear the set for each row
            for j in range(len(board)):
                if board[i][j] in checkSet and board[i][j] != '.':  # Check for duplicates
                    return False
                else:
                    checkSet.add(board[i][j])  # Add current value to the set
        
        # Check columns
        for i in range(len(board)):
            checkSet.clear()  # Clear the set for each column
            for j in range(len(board)):
                if board[j][i] in checkSet and board[j][i] != '.':  # Check for duplicates
                    return False
                else:
                    checkSet.add(board[j][i])  # Add current value to the set
        
        # Check subgrids (3x3 boxes)
        for i in range(0, 9, 3):  # Iterate through rows of subgrids
            for j in range(0, 9, 3):  # Iterate through columns of subgrids
                checkSet.clear()  # Clear the set for each subgrid
                for x in range(3):  # Iterate through rows within the subgrid
                    for y in range(3):  # Iterate through columns within the subgrid
                        if board[i+x][j+y] in checkSet and board[i+x][j+y] != '.':  # Check for duplicates
                            return False
                        else:
                            checkSet.add(board[i+x][j+y])  # Add current value to the set
        
        return True  # If all checks pass, the Sudoku board is valid
