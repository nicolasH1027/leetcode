class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}
        
        def dp(i, j):
            
            if i == -1 or j == -1:
                return max(i+1, j+1)
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i-1, j-1)
            else:
                memo[(i, j)] = min(dp(i-1, j) + 1,
                                  dp(i, j-1) + 1,
                                  dp(i-1, j-1) + 1)
            return memo[(i,j)]
            
        return dp(len(word1)-1, len(word2)-1)
    
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
        
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1, 
                                   dp[i][j-1] + 1,
                                   dp[i-1][j-1] + 1)
        
        return dp[m][n]
    
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)
        
        dp = [0]*(n+1)
        for i in range(n+1):
            dp[i] = i
        
        for i in range(1, m+1):
            pre = dp[0]
            dp[0] = i
            for j in range(1, n+1):
                tmp = dp[j]
                if word2[j-1] == word1[i-1]:
                    dp[j] = pre
                else:
                    dp[j] = min(pre + 1, 
                                   dp[j] + 1,
                                   dp[j-1] + 1)
                pre = tmp
        return dp[n]