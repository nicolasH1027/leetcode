class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        "TLE"
        if not nums:
            return 0
        
        hi = max(nums)
        lo = min(nums)
        dat = [0]*(hi - lo + 2)
        
        for num in nums:
            dat[num-lo] += 1
        
        cur = 0
        res = 0

        for val in dat:
            if val != 0:
                cur += 1
            else:
                res = max(res, cur)
                cur = 0
        return res


class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak