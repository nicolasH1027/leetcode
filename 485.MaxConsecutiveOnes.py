class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Time O(n), space O(1)
        """
        max_num = 0
        cur_num = 0

        for num in nums:
            if num == 0:
                max_num = max(max_num, cur_num)
                cur_num = 0
            else:
                cur_num += 1
        
        return max(max_num, cur_num)