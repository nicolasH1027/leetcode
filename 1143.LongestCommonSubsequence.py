class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]
    
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        
        if m < n:
            return self.longestCommonSubsequence(text2, text1)
        
        prev = [0]*(n + 1)
        dp = [0]*(n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[j] = 1 + prev[j-1]
                else:
                    dp[j] = max(prev[j], dp[j-1])
            prev, dp = dp, prev
        return prev[n]
    

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        0301Liuhaiming