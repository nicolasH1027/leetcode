class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        "马上能想到的方法就是这个 binary search 的 algorithm nlog(n)"
        prev, k = -float('inf'), 0

        for i in range(len(nums)):
            
            if nums[i] == prev:
                continue
 
            prev = nums[i]
            r = bisect.bisect_right(nums, nums[i])
            l = i
            for _ in range(min(2, r - l)):
                
                nums[k] = nums[l]
                
                k += 1
                l += 1

        return k
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        
        j, count = 1, 1

        for i in range(1, len(nums)):
            
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[j] = nums[i]
                j += 1
                
        return j

"""
for general question of at most k, 
"""

def removeDuplicates(nums: List[int], k: int) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    
    j, count = 1, 1

    for i in range(1, len(nums)):
        
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1
        
        if count <= k:
            nums[j] = nums[i]
            j += 1
            
    return j