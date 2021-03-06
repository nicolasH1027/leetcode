class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        seen, cur = {0: -1}, 0
        
        for i, val in enumerate(nums):
            cur = (cur + val) % k
            
            if cur not in seen:
                seen[cur] = i
            else:
                if i - seen[cur] > 1:
                    return True               
        return False


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        seen = {0: -1}
        cusum = 0
        
        for i in range(len(nums)):
            cusum = (cusum + nums[i]) % k
            if cusum in seen:
                if i - seen[cusum] > 1:
                    return True
                else:
                    continue
            seen[cusum] = i
            
        return False