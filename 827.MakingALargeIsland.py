class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        def neighbor(x, y):
            for dx, dy in [[-1,0], [1,0], [0,1], [0,-1]]:
                if 0 <= x + dx < n and 0 <= y + dy < n:
                    yield x + dx, y + dy
                
        def dfs(x, y, ind):
            ans = 1
            grid[x][y] = ind
            for nx, ny in neighbor(x, y):
                if grid[nx][ny] == 1:
                    ans += dfs(nx, ny, ind)
            return ans
        
        area, ind = {}, 2
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[ind] = dfs(i, j, ind)
                    ind += 1
                    
        ans = max(area.values() or [0])

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    index = set([grid[x][y] for x, y in neighbor(i,j) if grid[x][y] > 1])
                    ans = max(ans, 1 + sum([area[k] for k in index]))
        return ans 