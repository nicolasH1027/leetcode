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
        