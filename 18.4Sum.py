class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
	
        def twosum(nums, target):
            lo, hi = 0, len(nums) - 1
            result = []
            while lo < hi:
                if nums[lo] + nums[hi] < target:
                    lo += 1
                elif nums[lo] + nums[hi] > target:
                    hi -= 1
                else:
                    result.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
            return result
        
        def ksum(nums, target, k):
            res = []
            if len(nums) == 0 or target < nums[0]*k or nums[-1]*k < target:
                return res
            if k == 2:
                return twosum(nums, target)
            for i in range(len(nums) - k):
                if i and nums[i] == nums[i - 1]: continue
                for item in ksum(nums[i+1:], target - nums[i], k-1):
                    res.append([nums[i]] + item)
            return res
        nums.sort()
        return ksum(nums, target, 4)
                
                
                
            
        
        
        
        
        
        
        
        
        
        
        