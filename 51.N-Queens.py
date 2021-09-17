class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        'Same way with N-queen II'
        def backtracking(board, row, cols, diags, antidiags):
            if row == n:
                tmp = ["".join(board[i]) for i in range(n)]
                result.append(tmp)
                return 
            for i in range(n):
               if i in cols or row - i in diags or row + i in antidiags:
                   continue
               cols.add(i)
               diags.add(row - i)
               antidiags.add(row + i)
               board[row][i] = 'Q' 
               backtracking(board, row+1, cols, diags, antidiags)
               board[row][i] = '.' 
               cols.remove(i)
               diags.remove(row - i)
               antidiags.remove(row + i)
            return

        result = []
        cols = set()
        diags = set()
        antidiags = set()
        board = [['.']*n for _ in range(n)]
        backtracking(board, 0, cols, diags, antidiags)
        return result
        