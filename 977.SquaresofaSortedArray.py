class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        ans = [0]*len(nums)
        
        lpt, rpt, pt = 0, len(nums) - 1, len(nums) - 1
        
        while lpt <= rpt:
            
            x, y = nums[lpt]*nums[lpt], nums[rpt]*nums[rpt]
            
            if x < y:
                ans[pt] = y
                pt -= 1
                rpt -= 1
            else:
                ans[pt] = x
                pt -= 1
                lpt += 1
        
        return ans
            