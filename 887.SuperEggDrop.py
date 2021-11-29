class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        memo = {}
        
        def dp(k, n):
            
            if n == 0:
                return 0
                       
            if k == 1:
                return n
            
            if (k, n) in memo:
                return memo[(k, n)]
            
            res = float('inf')
            for i in range(1, n+1):
                res = min(res, max(dp(k-1, i - 1), dp(k, n - i)) + 1)
            memo[(k, n)] = res
            return res
        
        return dp(k, n)


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
                
        memo = {}
        
        def dp(k, n):
            
            if n == 0: return 0
                       
            if k == 1: return n
            
            if (k, n) in memo: return memo[(k, n)]
            
            res = float('inf')
            lo, hi = 1, n + 1
            
            while lo < hi:
                mid = lo + (hi - lo)//2
                broken = dp(k - 1, mid - 1)
                unbroken = dp(k, n - mid)
                if broken < unbroken:
                    lo = mid + 1
                    res = min(res, unbroken + 1)
                else:
                    hi = mid
                    res = min(res, broken + 1)

            memo[(k, n)] = res