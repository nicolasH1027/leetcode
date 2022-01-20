class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        向上取整也可以用如下方法
        
        (p-1)//k + 1
        """
        def valid(K):
            return sum(math.ceil(p/K) for p in piles) <= h
        
        lo, hi = 1, max(piles)
        
        while lo < hi:
            
            mid = lo + (hi - lo) // 2
            
            if not valid(mid):
                lo = mid + 1
            else:
                hi = mid
        
        return lo