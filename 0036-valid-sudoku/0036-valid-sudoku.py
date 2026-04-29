class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                current_cell = board[i][j]

                if current_cell == ".":
                    continue


                if( current_cell in rows[i] 
                    or current_cell in cols[j] 
                    or current_cell in squares[(i // 3, j // 3)] ):
                    return False

                    
                cols[j].add(current_cell)
                rows[i].add(current_cell)
                squares[i // 3, j//3].add(current_cell)
            
        return True