class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lpt = 0
        for rpt in range(1, len(nums)):
            if nums[lpt] != nums[rpt]:
                lpt += 1
                nums[lpt] = nums[rpt]
        return lpt + 1 if len(nums) != 0 else lpt