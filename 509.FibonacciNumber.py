class Solution:
    def fib(self, n: int) -> int:
        
        dp = [0]*(n+1)
        dp[0], dp[1] = 0, 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
            
        return dp[n]
    

class Solution:
    def fib(self, n: int) -> int:
        
        cur, prev1, prev2 = n, 1, 0
        
        for _ in range(2, n + 1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        
        return cur