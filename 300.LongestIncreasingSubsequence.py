class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        top = []
        
        for num in nums:
            
            pos = bisect.bisect_left(top, num)
            
            if pos == len(top):
                top.append(num)
            else:
                top[pos] = num
        
        return len(top)
            