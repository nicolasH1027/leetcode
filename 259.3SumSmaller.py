class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        """"
        Brute force require O(n^3) complexity, choose 3 from n
        Since we are quired to find less than, if we sort the nums, 
        its possible to use binary seach to find the elements that
        satisfy the condition
        """
        nums.sort()
        n = len(nums)
        result = 0
        
        import bisect
        result = 0
        for i in range(n - 2):
            for j in range(i+1, n):
                temp = target - nums[i] - nums[j]
                ind = bisect.bisect_left(nums, temp, j+1) - 1
                result += ind - j
        return result