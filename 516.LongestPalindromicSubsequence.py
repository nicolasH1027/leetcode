class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        dp(i, j) is defined as the length of the longest palindrome subsequence 
        between s[i] and s[j].
        if we know dp(i+1, j-1), then how to derive dp(i, j)
        
        if s[i] == s[j], then we can add this two string to the subsequence
        dp(i, j) = dp(i+1, j-1) + 2
        if s[i] != s[j], it means that s[i] and s[j] cant be in the subsequence
        in the same time
        so dp(i, j) = max(dp(i+1, j), dp(i, j-1))
        """ 
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]
    

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        space optimization
        """
        
        n = len(s)
        dp = [1]*n
        
        for i in range(n-1, -1, -1):
            pre = 0
            for j in range(i+1, n, 1):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j-1], dp[j])
                pre = tmp
        
        return dp[n-1]