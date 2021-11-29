class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        memo = {}
        
        def dp(i, j):
            
            if i == len(s1):
                ans = 0
                for c in s2[j:]:
                    ans += ord(c)
                memo[(i, j)] = ans
                return ans
            
            if j == len(s2):
                ans = 0
                for c in s1[i:]:
                    ans += ord(c)
                memo[(i, j)] = ans
                return ans
            
            if (i, j) in memo:
                return memo[(i,j)]
            
            if s1[i] == s2[j]:
                memo[(i, j)] = dp(i+1, j+1)
            else:
                memo[(i, j)] = min(dp(i+1, j) + ord(s1[i]), dp(i, j+1) + ord(s2[j]))
            
            return memo[(i, j)]
        
        return dp(0, 0)


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        m, n = len(s1), len(s2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            dp[i][0] = sum([ord(s1[k]) for k in range(i)])
        
        for j in range(1, n+1):
            dp[0][j] = sum([ord(s2[k]) for k in range(j)])
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        
        return dp[m][n]
    

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        m, n = len(s1), len(s2)
        
        dp = [0]*(n+1)
        
        for j in range(1, n+1):
            dp[j] = sum([ord(s2[k]) for k in range(j)])
        
        for i in range(1, m+1):
            pre = dp[0]
            dp[0] = sum([ord(s1[k]) for k in range(i)])
            for j in range(1, n+1):
                tmp = dp[j]
                if s1[i-1] == s2[j-1]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j] + ord(s1[i-1]), dp[j-1] + ord(s2[j-1]))
                pre = tmp
        
        return dp[n]