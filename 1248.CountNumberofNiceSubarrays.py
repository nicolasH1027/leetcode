class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        compared with 560 subarray sum equals to k, they are the same with the technique prefix sum
        """
        
        seen = {0:1}
        cucnt = 0
        cnt = 0
        
        for i in range(len(nums)):
            cucnt += nums[i] % 2
            
            if cucnt - k >= 0:
                cnt += seen.get(cucnt - k)
            
            seen[cucnt] = seen.get(cucnt, 0) + 1
        
        return cnt