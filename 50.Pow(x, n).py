class Solution:
    def myPow(self, x: float, n: int) -> float:
        "Recursion Version"
        if n < 0:
            x = 1/x
            n = -n
            
        def dfs(x, n):
            if n == 0:
                return 1
            
            result = dfs(x, n >> 1)
            return result * result if n % 2 == 0 else result * result * x
        
        return dfs(x, n)
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        "Iterative Version"
        
        if n < 0:
            x = 1/x
            n = -n
        result = 1
        while n:
            if n % 2 == 1:
                result = x*result
            n >> 1
            x *= x
        return result
            
            
        