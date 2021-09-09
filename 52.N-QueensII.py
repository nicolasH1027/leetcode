class Solution:
    def totalNQueens(self, n: int) -> int:     
        def backtrack(row, cols, diags, antidiags):  
            if row == n:
                self.solutions += 1
                return 
            for col in range(n):   
                diag = row - col
                anti = row + col         
                if col in cols or diag in diags or anti in antidiags:
                    continue    
                cols.add(col)
                diags.add(diag)
                antidiags.add(anti)    
                backtrack(row + 1, cols, diags, antidiags)
                cols.remove(col)
                diags.remove(diag)
                antidiags.remove(anti)      
            return       
        cols = set()
        diags = set()
        antidiags = set()
        self.solutions = 0
        backtrack(0, cols, diags, antidiags)
        return self.solutions