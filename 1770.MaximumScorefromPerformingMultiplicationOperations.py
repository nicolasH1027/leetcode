class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        m, n = len(nums), len(multipliers)
        
        @lru_cache(maxsize = None)
        def dp(i, left):
            
            if i == n:
                return 0
            
            mul = multipliers[left]
            right = m - 1 - (i - left)
            
            return max(dp(i+1, left+1) + mul*nums[left], dp(i+1, left) + mul*nums[right])
        
        return dp(0,0)

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        m, n = len(nums), len(multipliers)
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(i, -1, -1):
                mul = multipliers[i]
                lo, hi = nums[j], nums[m - 1 - (i - j)]
                dp[i][j] = max(dp[i+1][j+1] + lo*mul, dp[i+1][j] + hi*mul)
        
        return dp[0][0]


    

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        m, n = len(nums), len(multipliers)

        test = [0]*(n+1)
        for i in range(n-1, -1, -1):
            prev = test[i+1]
            for j in range(i, -1, -1):
                mul = multipliers[i]
                lo, hi = nums[j], nums[m - 1 - (i - j)]
                tmp = test[j]
                test[j] = max(prev + lo*mul,  test[j] + hi*mul)
                prev = tmp
        return test[0]
                
                
                