class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        
        @functools.lru_cache
        def backtrack(start, end):
            
            if start >= end:
                return 1
            tmp = 0
            for i in range(start, end + 1):
                left = backtrack(start, i-1)
                right = backtrack(i+1, end)
                tmp += left * right
            return tmp
        
        return backtrack(1, n)
    
class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        
        return dp[n]
                