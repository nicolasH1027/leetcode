class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        ans = CuMin = CuMax = nums[0]

        for val in nums[1:]:
            tmp = max(val, val*CuMax, val*CuMin)
            CuMin = min(val, val*CuMax, val*CuMin)
            CuMax = tmp
            ans = max(ans, CuMax)
        
        return ans
    
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        
        """
        n = len(nums)
        1.假设没有0,
        那么最大的子数组肯定以第0元素开头，或者第n-1元素结尾
        如果有偶数个负数，那么直接全部相乘
        如果是奇数个，那么假设第一个的位置是i，最后一个的位置是j
        结果只可能是 nums[i+1:]或 nums[:j]
        前面那个是后缀积，后面那个是前缀积
    
        2. 如果有0
        0相当于把数组分成了两个独立的数组，就重新计算就好了
        """
        
        ans, n = nums[0], len(nums)
        l = r = 0
        
        for i in range(n):
            l = nums[i]*(l if l else 1)
            r = nums[n - i -1]*(r if r else 1)
            ans = max(ans, l, r)
        
        return ans