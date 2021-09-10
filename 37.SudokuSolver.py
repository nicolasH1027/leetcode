class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        from collections import defaultdict
        
        # initialized the defaultdict of set to record the seen value 
        row, col, box = defaultdict(set), defaultdict(set), defaultdict(set)
        
        # function that used to check whether the input v is valid at location (r, c)
        def valid(r, c, v):
            boxind = (r // 3)*3 + c // 3
            return v not in row[r] and v not in col[c] and v not in box[boxind]
        
        # place the value v into board and also into the three defaultdict
        def place(r, c, v):
            boxind = (r // 3)*3 + c // 3
            board[r][c] = str(v)
            row[r].add(v)
            col[c].add(v)
            box[boxind].add(v)

        # remove the value of v from the board and also the corresponding defaultdict
        def remove(r, c, v):
            boxind = (r // 3)*3 + c // 3
            board[r][c] = '.'
            row[r].remove(v)
            col[c].remove(v)
            box[boxind].remove(v)

        def backtrack(r, c):
            
            if r == 8 and c == 9:              # already fill out all the empty cell
                return True
            elif r == 9:                       # reach the last element of one row, so we jump into the first element in next row
                return backtrack(r+1, 0)
            else:
                if board[r][c] != '.':         # reach the seen element, so we jump to the next cell
                    return backtrack(r, c+1)
                else:
                    for i in range(1, 10):
                        if not valid(r, c, i):
                            continue
                        place(r, c, i)
                         # if the next cell return true, then we dont need to remove the value that insert in the current run, so we return true
                        #  however, if the next backtrack return False, that means the current input is invalid, so we need to remove
                        if backtrack(r, c+1): 
                            return True
                        remove(r, c, i)
                    # return False
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    place(r, c, int(board[i][j]))
                        
        backtrack(0, 0)
                
            