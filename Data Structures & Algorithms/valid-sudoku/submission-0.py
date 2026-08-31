class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #iterate rows
        for row in range(0,9):
            seen = set()
            for col in range(0,9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

       # iterate cols
        for row in range(0,9):
            seen = set()
            for col in range(0,9):
                if board[col][row] == '.':
                    continue
                if board[col][row] in seen:
                    return False
                seen.add(board[col][row])


        #iterate boxes
        arr_row = [-1,0,1]
        arr_col = [-1,0,1]
    
        for irow in range(0,2):
            for icol in range(0,2):
                seen = set()
                row = 1 + irow*3
                col = 1 + icol*3
                for j in arr_row:
                    for k in arr_col:
                        if board[row + j][col + k] == '.':
                            continue
                        if board[row + j][col + k] in seen:
                            return False
                        seen.add(board[row + j][col + k])


            
        return True
        

       