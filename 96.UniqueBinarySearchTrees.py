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