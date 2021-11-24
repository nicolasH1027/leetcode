class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        if not board:
            return []
        
        neigh = [(1,1), (1,-1), (-1,1), (-1,-1), (0,1), (0,-1), (1,0), (-1,0)]
        
        i, j = click[0], click[1]
        
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
      
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'M':
                board[i][j] = 'X'
                return
            
            cnt = 0
            
            for ix, jy in neigh:
                ni, nj = i + ix, j + jy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                    cnt += 1
            
            if cnt:
                board[i][j] = str(cnt)
            else:
                board[i][j] = 'B'
                for ix, jy in neigh:
                    ni, nj = i + ix, j + jy
                    if  0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'E':
                        dfs(ni, nj)
        
        dfs(i, j)
        
        return board
