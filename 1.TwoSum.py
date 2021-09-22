class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time O(n),  Space O(1) Hashmap
        """
        compliment = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in compliment:
                return [compliment[remain], i]
            compliment[nums[i]] = i
            

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        If we dont need to return the ind of original index, we can use the following
        Time O(nlog(n)),  Space O(1) Two pointer
        """
        nums.sort()
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            tmp = nums[lo] + nums[hi]
            if tmp == target:
                return [nums[lo], nums[hi]]
            elif tmp < target:
                lo += 1
            else:
                hi -= 1
        
            