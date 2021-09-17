class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(row, col, pos):
            if pos == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n or (row, col) in seen:
                 return False
            if board[row][col] != word[pos]:
                return False
            seen.add((row, col))
            for i, j in [(-1,0), (1,0), (0,1), (0,-1)]:                
                if backtrack(row+i, col+j, pos + 1):
                    return True
            seen.remove((row, col))
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                seen = set()
                if backtrack(i, j, 0):
                    return True

        return False
