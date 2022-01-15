class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        path, m, n = 0, len(grid), len(grid[0])
        
        start = ()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    path += 1
                    if grid[i][j] == 1:
                        start = (i, j)
        
        def valid(x, y):
            if 0 <= x < m and 0 <= y < n and grid[x][y] >= 0:
                return True
            else:
                return False
            

        def backtracking(x, y, walk):
            
            if grid[x][y] == 2 and walk == 1:
                return 1 
            
            tmp = grid[x][y]
            grid[x][y] = -4
            ans = 0
            
            for dx, dy in  [[1,0], [-1,0], [0,1], [0,-1]]:
                nx, ny = x + dx, y + dy
                if valid(nx, ny):
                    ans += backtracking(nx, ny, walk-1)
                    
            grid[x][y] = tmp
            
            return ans
        
        return backtracking(start[0], start[1], path)
    