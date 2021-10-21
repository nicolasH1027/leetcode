class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        "prefix sum"
        
        left, right = 0, sum(nums)
        
        for i in range(len(nums)):
            
            if left == right - nums[i] - left:
                return i
            
            left += nums[i]
        
        return -1
            