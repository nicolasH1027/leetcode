class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left, right, valid, n = 0, 0, 0, len(nums)     
        ans = -float('inf')
        
        while right < n:
            if nums[right] == 0:
                valid += 1
                while valid > k:
                    if nums[left] == 0:
                        valid -= 1
                    left += 1
            ans = max(ans, right + 1 - left)
            right += 1
        return ans