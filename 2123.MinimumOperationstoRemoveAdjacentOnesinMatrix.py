class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        
        m, n= len(grid), len(grid[0])
        
        seen = [[0]*n for _ in range(m)]
        
        
        def dfs(x, y, cnt):

            cnt[(x + y) % 2] += 1
            
            for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not seen[nx][ny] and grid[nx][ny]:
                    seen[nx][ny] = 1
                    dfs(nx, ny, cnt)

            return cnt
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if seen[i][j]: continue
                if not grid[i][j]: 
                    seen[i][j] = 1
                    continue
                seen[i][j] = 1
                ans += min(dfs(i, j, [0, 0]))
        
        return ans
                    