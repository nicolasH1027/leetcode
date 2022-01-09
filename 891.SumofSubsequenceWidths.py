class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        "排序之后就可以分别找到左右两边分别有多少个子序列"
        nums.sort()
        ans, n = 0, len(nums)
        
        for i, val in enumerate(nums):
            
            ans += val * (1 << i)
            ans -= val *(1 << (n - i - 1))
            
        return ans % (10**9 + 7)