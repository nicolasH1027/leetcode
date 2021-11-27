# divide and conquer algorithm with left and right pointer O(nlogn)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = self.maxsubarray(nums, 0, len(nums) - 1)
        
        return res[2]
    
    def maxsubarray(self, nums, low, high):
        
        if len(nums) == 0:
            return -1
        
        if low == high:
            return (low, high, nums[low])
        
        mid = low + (high - low) // 2
        
        leftlargest = self.maxsubarray(nums, low, mid)
        rightlargest = self.maxsubarray(nums, mid+1, high)
        midlargest = self.maxcross(nums, low, high, mid)
        
        if leftlargest[2] >= rightlargest[2] and leftlargest[2]>= midlargest[2]:
            return leftlargest
        
        elif rightlargest[2] >= leftlargest[2] and rightlargest[2] >= midlargest[2]:
            return rightlargest
        
        else:
            return midlargest
    
    
    def maxcross(self, nums, low, high, mid):
        
        leftsum = float(-inf)   
        SUM = 0
        lpt = mid
        for i in range(mid, low - 1, -1):
            SUM += nums[i]
            if SUM > leftsum:
                leftsum = SUM
                lpt = i
        
        rightsum = float(-inf)
        SUM = 0
        rpt = mid
        for j in range(mid+1, high + 1):
            SUM += nums[j]
            if SUM > rightsum:
                rightsum = SUM
                rpt = j

        
        return (lpt, rpt, leftsum + rightsum)
    

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = -float('inf')
        cur_sum = 0
        
        for num in nums:
            cur_sum = max(cur_sum + num,  num)
            max_sum = max(cur_sum, max_sum)
            
        return max_sum