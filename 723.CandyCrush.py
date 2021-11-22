class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        m = len(board)
        n = len(board[0])
        
        while True:
            seen = set()
            
            for i in range(m):
                for j in range(n):
                    if j > 1 and board[i][j] and board[i][j] == board[i][j-1] == board[i][j-2]:
                        seen.add((i, j))
                        seen.add((i, j-1))
                        seen.add((i, j-2))
                    if i > 1 and board[i][j] and board[i][j] == board[i-1][j] == board[i-2][j]:
                        seen.add((i,j))
                        seen.add((i-1, j))
                        seen.add((i-2, j))
                        
            if not seen:
                break
            
            for i, j in seen:
                board[i][j] = 0
                
            for col in range(n):
                p = q = m - 1
                while p >= 0:
                    if board[p][col] != 0:
                        board[p][col], board[q][col] = board[q][col], board[p][col]
                        q -= 1
                    p -= 1
        return board