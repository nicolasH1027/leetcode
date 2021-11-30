class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        if m < n:
            return self.minDistance(word2, word1)
        
        prev = [0]*(n + 1)
        dp = [0]*(n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[j] = 1 + prev[j-1]
                else:
                    dp[j] = max(prev[j], dp[j-1])
            prev, dp = dp, prev
        return m + n - 2*prev[n]