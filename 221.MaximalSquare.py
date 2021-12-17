class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0]*(n + 1) for _ in range(m+1)]
        
        maxSide = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        
        return maxSide*maxSide
    
    
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [0]*(n + 1)
        
        maxSide = 0
        prev = dp[0]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '1':
                    tmp = dp[j]
                    dp[j] = min(prev,dp[j],dp[j-1]) + 1
                    maxSide = max(maxSide, dp[j])
                    prev = tmp
        return maxSide*maxSide