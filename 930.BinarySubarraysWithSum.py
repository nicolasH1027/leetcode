class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        """
        same code with 1248
        """
        seen = {0:1}
        cucnt = 0
        cnt = 0
        
        for i in range(len(nums)):
            cucnt += nums[i]
            
            if cucnt - goal >= 0:
                cnt += seen.get(cucnt - goal,0)
            
            seen[cucnt] = seen.get(cucnt, 0) + 1
        
        return cnt
    
