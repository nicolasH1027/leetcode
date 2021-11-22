class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        def helper(nums):
            if len(nums) <= 2:
                return 1
            
            left = [num for num in nums if num < nums[0]]
            right = [num for num in nums if num > nums[0]]
            
            constant = math.comb(len(left) + len(right), len(left)) % (10**9 + 7)
            
            return constant*helper(left)*helper(right)
        
        return (helper(nums) - 1) % (10**9 + 7)
        