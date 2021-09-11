from math import inf


class Solution:
    def numSquares(self, n: int) -> int:
        "Backtracking, brute force, TLE"
        def backtrack(n):
            if n == 0:
                return 0
            count = inf
            i = 1
            while i*i <= n:
                count = min(count, backtrack(n - i*i) +  1)
                i += 1
            return count   
        return backtrack(n)
                
                
class Solution:
    def numSquares(self, n: int) -> int:
        "Backtracking, with memorization, AC"
        seen = {}
        def backtrack(n, seen):
            if n in seen:
                return seen[n]
            if n == 0:
                return 0
            count = inf
            i = 1
            while i*i <= n:
                count = min(count, backtrack(n - i*i, seen) + 1)
                i += 1
            seen[n] = count
            return count
        return backtrack(n, seen)
        
# the memorization recursion is the same with dynamic programming
              
class Solution:
    def numSquares(self, n: int) -> int:
        "dynamic programming"
        dp = [inf]*(n + 1)
        dp[0] = 0  
        for i in range(1, n + 1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1 ) 
                j += 1        
        return dp[n]