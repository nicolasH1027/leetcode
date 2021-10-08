class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        j = len(nums) - 1
        while j >= 1:
            
            if nums[j - 1] < nums[j]:
                i = j
                while i < len(nums):
                    if nums[i] > nums[j - 1]:
                        i += 1
                    else:
                        break
                nums[j - 1], nums[i-1] = nums[i-1], nums[j - 1]

                lo, hi = j, len(nums) - 1
                while lo < hi:
                    nums[lo], nums[hi] = nums[hi], nums[lo]
                    lo += 1
                    hi -= 1
                return
            j -= 1
        nums.sort()
        return