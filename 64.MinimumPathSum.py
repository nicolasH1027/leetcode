class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        memo = {}
        
        def dp(i, j):
            
            if i == 0:
                path = 0
                for k in range(j+1):
                    path += grid[0][k]
                memo[(i, j)] = path
                return memo[(i, j)]

            if j == 0:
                path = 0
                for k in range(i+1):
                    path += grid[k][0]
                memo[(i, j)] = path
                return memo[(i, j)]
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            left = dp(i, j-1)
            top = dp(i-1, j)
            
            if left <= top:
                memo[(i, j)] = left + grid[i][j]
            else:
                memo[(i, j)] = top + grid[i][j]
            
            return memo[(i, j)]

        return dp(len(grid)-1, len(grid[0])-1)
        

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        memo = {}
        
        def dp(i, j):
            
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return float('inf')
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            left = dp(i, j-1)
            top = dp(i-1, j)
            
            if left <= top:
                memo[(i, j)] = left + grid[i][j]
            else:
                memo[(i, j)] = top + grid[i][j]
            
            return memo[(i, j)]

        return dp(len(grid)-1, len(grid[0])-1)
    
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dp = [[0]*n for _ in range(m)]
    
        dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                
        return dp[m-1][n-1]
    

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dp = [0]*n
        dp[0] = grid[0][0]
        
        for i in range(1, n):
            dp[i] = dp[i-1] + grid[0][i]
        
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
                
        return dp[n-1]