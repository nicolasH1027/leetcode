class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
    
        def dp(nums):
            
            if len(nums) == 1:
                return nums[0]
            
            lag_2, lag_1 = nums[0], max(nums[:2])
            cur = lag_1
            
            for i in range(3, len(nums) + 1):
                
                cur = max(lag_2 + nums[i-1], lag_1)
                lag_2 = lag_1
                lag_1 = cur
            
            return cur
        
        return max(dp(nums[:-1]), dp(nums[1:]))