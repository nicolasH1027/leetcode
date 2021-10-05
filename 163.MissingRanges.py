class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
    
        lo = lower - 1
        nums.append(upper + 1)
        result = []
        for num in nums:
            if abs(num - lo) == 2:
                result.append(f"{num-1}")
            if abs(num - lo) > 2:
                result.append(f"{lo+1}->{num-1}")
            lo = num
            
        return result