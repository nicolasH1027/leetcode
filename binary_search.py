
def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] > x: hi = mid
        else: lo = mid+1
    return lo

"""
向上取整  x/y,  (x + y - 1)//y

二分法常见的模板有三种， 可从leetcode上查阅。
但是最重要的是搞清楚每次二分法运用时候的不变量是什么

例如

left, right = 0, len(nums)

while left < right:
    mid = left + (right - left)//2
    
    if nums[mid] < x:
        
        left = mid + 1
        
    else:
    
        right = mid
return left

上面这个模板， 维护的 是一个 [left, right) 左闭右开的区间。所以right其实是我们要查找的对象的下一个。
可以用binary search解决的问题有如下几个
"""

"875. Koko Eating Bananas"
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        每次能吃k个香蕉，那么最小的k是多少，能让我们能在h小时内吃完所有香蕉
        
        所以，一定存在一个k， 当小于k的时候， 结果 > h小时，然后 大于等于k的时候
        ，大于等于h小时， 所以我们需要寻找最左边的k。
        
        k 值           k'
                       -------------------------- k >= k',  h' >= h
        ---------------
        
        假设来到corner case [3, 4)
        
        此时 取到 3
        
        对应的  cnt < h'，那么 k = 3 + 1 == 4
        """
        
        left, right = 1, sum(piles) + 1
        
        while left < right:
            
            mid, cnt = left + (right - left)//2, 0
            
            for p in piles:
                
                cnt += (p + mid - 1)//mid
            
            if cnt > h:
                
                left = mid + 1
            
            else:
                
                right = mid
        
        return left


"1011. Capacity To Ship Packages Within D Days"

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        """
        此题和上面那题思路一模一样
        """
        tol = sum(weights)
        
        left, right = max(weights), tol+1

        while left < right:
            
            mid, CuSum, cnt = left + (right - left)//2, 0, 1
            
            for w in weights:
                
                if CuSum + w > mid:
                    
                    cnt += 1
                    
                    CuSum = 0
                    
                CuSum += w
            
            if cnt > days:
                
                left = mid + 1
            
            else:
                
                right = mid
            
        return left
    
    
    
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        
        """
        注意，此题问的是，最大能获得的甜度，
        
        s            s'             
                     ----------------- 当 s >= s'， 此时 只能切 k' <  k + 1
        -------------                  当 s < s'， 此时 我们有 k' >= k + 1, 
        
        根据这个图， 我们应该找到s'左边的点， 从而使得 k' = k + 1 而s'取得最大值
        
        假设 corner case 是 [3, 4)
        
        此时，我们在 3的位置，那么 cnt >= k + 1, 我们会选择调到 s'的地方，此时left==right，
        跳出循环，
        而我们要找的量则是
        left - 1        
        """

        left, right = min(sweetness),  sum(sweetness)//(k + 1) + 1
        
        while left < right:
            
            mid, cur, cnt = left + (right - left)//2, 0, 0
        
            for s in sweetness:
                cur += s
                if cur >= mid:
                    cnt += 1        
                    cur = 0
            
            if cnt >= k + 1:
                left = mid + 1
            else:                
                right = mid
 
        return left - 1
    
"410. Split Array Largest Sum"


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        """
        
        s                  s'
                           -------------------   s >= s', m' <= m
        ------------------                       s < s', m' > m

        """
        
        left, right = max(nums), sum(nums) + 1
        
        while left < right:    
            mid, cur, cnt = left + (right-left)//2, 0, 1       
            for n in nums:
                cur += n
                if cur > mid:
                    cnt += 1    
                    cur = n
            if cnt > m:
                
                left = mid + 1    
            else:
                
                right = mid
        return left





"2141. Maximum Running Time of N Computers"

"模板解法"



class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        
        """
        最理想的状态就是 sum(batteries)//n, 那么我们只需要进行
        二分查找，在 0 和 sum(batteries)//n 之间不停搜索，找到某个点， k，
        
        k 是可以通过二分查找确定的。因为如果可以运行 k 分钟，那么也一定可以运行 k-1, k-2, ⋯ 分钟。因此一定存在一个最小的 k'
        """
        
        left, right = 0, sum(batteries)//n + 1
        
        while left < right:
            
            mid = left + (right - left)//2
            
            tol = 0
            
            for val in batteries:
                
                tol += min(val, mid)
            "tol 统计的是，当前分钟mid下，一共能运行多长时间，如果小于理论 n * mid，那么右移边界"
            if tol >= n*mid:
                
                left = mid + 1
            
            else:
                
                right = mid
        
        return left - 1


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        tol = sum(batteries)
        batteries.sort()
        
        while batteries[-1] > tol // n:
            
            tol -= batteries.pop()
            n -= 1
            
        return tol // n

