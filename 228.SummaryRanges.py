class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return []
        
        result = []
        nums.append(nums[-1] + 2)
        lo = 0
        for i, num in enumerate(nums):
            if i == len(nums) - 1 or num - nums[i-1] >= 2:
                if lo == i - 1:
                    result.append(str(nums[lo]))
                else:
                    result.append(str(nums[lo]) + "->" + str(nums[i-1]))
                lo = i
        return result
    
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        result = []
        lo = 0
        for i, num in enumerate(nums):
            if i == len(nums) - 1 or nums[i+1] - num >= 2:
                if nums[lo] == num:
                    result.append(str(nums[lo]))
                else:
                    result.append(str(nums[lo]) + "->" + str(nums[i]))
                lo = i+1
        return result