class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Naive way
        """
        if len(nums) <= 2:
            return max(nums)
        
        n = len(nums)
        dp = [0]*(n+1)
        dp[1], dp[2] = nums[0], nums[1]
        
        for i in range(3, n+1):
            
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-3] + nums[i-2], dp[i-3] + nums[i-1])
        
        return dp[n]
    
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = [0]*(n+1)
        dp[1], dp[2] = nums[0], max(nums[:2])
        
        for i in range(3, n+1):
            
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        
        return dp[n]
    

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        lag_2, lag_1 = nums[0], max(nums[:2])
        cur = lag_1
        
        for i in range(3, n+1):
            
            cur = max(lag_2 + nums[i-1],  lag_1)
            lag_2 = lag_1
            lag_1 = cur
        
        return cur