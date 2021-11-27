class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        memo = [[10002]*n for _ in range(m)]
        
        def dp(i, j):
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return 10002
            
            if i == 0:
                return matrix[0][j]
            
            if memo[i][j] != 10002:
                return memo[i][j]
            
            memo[i][j] = matrix[i][j] + min(dp(i-1, j-1), dp(i-1,j), dp(i-1, j+1))
            
            return memo[i][j]
        
        ans = float('inf')
        for j in range(n):
            ans = min(ans, dp(m-1, j))
        
        return ans

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    matrix[i][j] = matrix[i][j] + min(matrix[i-1][j], matrix[i-1][j+1])
                elif j == n - 1:
                    matrix[i][j] = matrix[i][j] + min(matrix[i-1][j], matrix[i-1][j-1])
                else:
                    matrix[i][j] = matrix[i][j] + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
        
        ans = float('inf')
        
        for j in range(n):
            ans = min(ans, matrix[m-1][j])
        
        return ans