class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(maxsize=None)
        def backtrack(numSum, i):
            if i == len(nums):
                if numSum == target:
                    return 1
                else:
                    return 0
            
            result = 0
            for op in [-1, 1]:
                numSum += op*nums[i]
                result += backtrack(numSum, i+1)
                numSum -= op*nums[i]
            return result 
        
        return backtrack(0, 0)
    
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int: