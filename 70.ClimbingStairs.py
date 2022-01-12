class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        ans, lag2, lag1 = 0, 1, 2
        
        for _ in range(3, n + 1):
            ans = lag2 + lag1
            lag2 = lag1
            lag1 = ans
        
        return ans   