
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
        注意，此题问的是，最大能获得的甜度，我们用这题彻底阐述二分搜索时的注意事项
        
        s                          
                        ----------------- 当 s > s'， 此时 只能切 k' <  k + 1
        -------------s'                   当 s <= s'， 此时 我们有 k' >= k + 1, 
        
        根据这个图， 我们应该找到s'这个点，就是下面这条虚线最右边的点，从而使得 k' = k + 1 而s'取得最大值，
        
        需要提醒自己的是，我们现在维护的区间是 左闭右开的区间  [a, b)， 即右边的b是取不到的
        
        下一步要决定的就是，给定一个s， 我们怎么算这个 k', 通用的代码如下
        
        for s in sweetness:
            cur += s
            if cur >= mid:
                cnt += 1        
                cur = 0
        
        另外一个重要的点 在于 cur >= mid 还是 cur > mid，这会导致最后返回值得不同，
        
        先尝试  cur >= mid， 在这个条件下，我们统计的是，当 s 可以取到 mid的情况下，最大能分出多少组出来， 
        
        对应的是上面 s <= s', k' >= k + 1的情况， 然后我们讨论 corner case
                        4
                        -----------------  
        -------------3                     
        [3, 4)    

        此时， 我们算出来的 肯定的 left = 3， 那么下一次循环呢？ 因为 对应 s = 3 算出来的 k' 肯定是小于等于 k + 1的，
        那么此时我们需有 left = mid + 1， 然后就是 4 == 4 跳出循环， 那么我们的答案应该是 left - 1
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


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """
        接着我们尝试， cur > mid， 在这个条件下，我们统计的是，当 s 取到比mid大的情况下，最大能分出。
        
        注意，这里， mid是取不到的。 对照下面的图，我们其实算的是 s > s' 的时候， 只能取到
        k' < k + 1
        
                        ----------------- 当 s > s'， 此时 只能切 k' <  k + 1
        -------------s'                   当 s <= s'， 此时 我们有 k' >= k + 1, 
        
        然后我们讨论 corner case
                          4
                          -----------------  
        -------------2                     
        [2, 4)    

        此时， 假设正确答案是3， 那么此时mid 是3， 当 s 大于 3的时候， 我们能取到的 k'肯定是小于 k + 1，
        那么此时我们需要做的是  right = mid, 就是 [2, 3)
        
        然后下一轮循环，  此时， mid 是2，那么此时， 因为正确答案是 3， 那么我们取到的k' 肯定是大于等于 k + 1，
        那么此时我们需要做的是 left = mid + 1, 此时 [3, 3)，跳出循环，我们的答案就是 3 了

        """
        
        left, right = min(sweetness),  sum(sweetness)//(k + 1) + 1
        
        while left < right:
            
            mid, cur, cnt = left + (right - left)//2, 0, 0
        
            for s in sweetness:
                cur += s
                if cur > mid:
                    cnt += 1        
                    cur = 0
            
            if cnt >= k + 1:
                left = mid + 1
            else:                
                right = mid
 
        return left 
        
        
        
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        """
        我们接着讨论 leetcode 参考答案的意思， 其实很明显， 参考答案维护的是
        
        左开右闭 区间  (a, b]， 此时的a是我们取不到的值， 首先要确定的就是，
        
        左开右闭 怎么取 mid， 之间我们维护左闭右开的时候 是  left + (right - left)//2，这个其实是落在左中点上，
        
        那么此时，左开右闭，我们需要落在右中点， 那么很简单， left + (right - left + 1)//2， 这样就可以了， 等价于  (left + right + 1)//2
        
        之前的图就变成了下面这样
                      s'
                      ----------------- 当 s >= s'， 此时 只能切 k' <=  k + 1
        -------------                   当 s < s'， 此时 我们有 k' > k + 1, 
        
        所以我们的目标是找到上面这条虚线最左边的点， 假设我们选 cur >= mid
        
        for s in sweetness:
            cur += s
            if cur >= mid:
                cnt += 1        
                cur = 0
                
        此时我们统计的是 s >= mid 的时候最少 有多少 k'，所以当 k' >= k + 1时，我们左移 区间 left = mid， 因为我们要求的是最大值，所以直接左移
        
        
        
        然后我们讨论 corner case
                          3  4
                          -----------------  
        -------------1                     
        (1, 4]     假设正确答案是3

        此时，我们算出来的 mid 是 3， 然后统计 k'， 等于 k + 1，
        
        此时我们 左移区间 (3, 4]， 然后我们求mid 得到 4， 对应的k'小于 k + 1,右移
        
        (3, 3], 返回 right

        """    

        left, right = min(sweetness) - 1,  sum(sweetness)//(k + 1)
        
        while left < right:
            
            mid, cur, cnt = left + (right - left + 1)//2, 0, 0
        
            for s in sweetness:
                cur += s
                if cur >= mid:
                    cnt += 1        
                    cur = 0
            
            if cnt >= k + 1:
                left = mid 
            else:                
                right = mid -1
 
        return right
    


        
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        """

                      s'
                      ----------------- 当 s >= s'， 此时 只能切 k' <=  k + 1
        -------------                   当 s < s'， 此时 我们有 k' > k + 1, 
        
        我们选 cur > mid
        
        for s in sweetness:
            cur += s
            if cur > mid:
                cnt += 1        
                cur = 0
                
        此时我们统计的是 s > mid，  的时候最少 有多少 k'，注意，此时我们的计算不包括 mid， 如果 k' >= k + 1，说明
        
        我们应该右移区间  right = mid - 1, 注意 和前面 cur >= mid 不同， 因为，此时不包含mid， 说明最后我们不会越界，直接返回 right
        
        我们讨论 corner case
                          3
                          -----------------  
        -------------2                     
        (2, 3]     假设正确答案是3

        此时，我们算出来的 mid 是 3， 然后统计 k'，此时， 因为统计的是 大于 3的情况，  说明最后的结果肯定 小于 k+ 1,
        
        那么我们需要 右移区间  right = mid - 1
        
        (2, 2]， 跳出循环， 返回 right + 1

        """    

        left, right = min(sweetness) - 1,  sum(sweetness)//(k + 1)
        
        while left < right:
            
            mid, cur, cnt = left + (right - left + 1)//2, 0, 0
        
            for s in sweetness:
                cur += s
                if cur > mid:
                    cnt += 1        
                    cur = 0
            
            if cnt >= k + 1:
                left = mid 
            else:                
                right = mid -1
 
        return right + 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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

