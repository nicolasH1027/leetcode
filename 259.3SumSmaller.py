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
    

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        "Two pointer, like the solution in 3 sum"
        "can be extended to k sum smaller"
        def twosumsmaller(nums, start, target):
            lo, hi = start, len(nums) - 1
            result = start
            while lo < hi:
                T = nums[lo] + nums[hi]
                if T >= target:
                    hi -= 1
                else:
                    result += hi - lo
                    lo += 1
            return result

        nums.sort()
        result = 0
        for i in range(len(nums)):
            # if i and nums[i] == nums[i - 1]: continue#  we dont need this line, because we are asked to find the number of index, not the distinct tuple.
            result += twosumsmaller(nums, i+1, target - nums[i])
        return result