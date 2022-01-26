"""
这里的循环问题， 指的是 数组问题中， 遇到的数组是头尾也相接的数组

有若干种思路

1. 将数组和自己进行拼接， 

2. iterate 2n but with mod

3. 分头和尾两种情况讨论

"""

"213. House Robber II"
"此打家劫舍题假设了数组是循环数组， 但是因为头尾两个数，只能二选一，所以，分别讨论即可"
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def dp(nums):
            
            if len(nums) == 1:
                
                return nums[0]
            
            lag2, lag1 = nums[0], max(nums[:2])
            
            for i in range(2, len(nums)):
                
                lag1, lag2 = max(lag2 + nums[i], lag1), lag1
            
            return lag1
        
        return max(dp(nums[:-1]), dp(nums[1:]))



"796. Rotate String"
"此题，循环字符串，直接拼接字符串，然后用kmp 或者 自带的算法进行运算， python 自带的是 Boyer–Moore–Horspool O（n + m）"
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        return len(s) == len(goal) and goal in s + s



"2134. Minimum Swaps to Group All 1's Together II"
"此题也可以用拼接法，但是会造成不必要的空间开销，因为是求最值，那么通过mod直接遍历2n次就可以了"
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        tol, n = sum(nums), len(nums)
        
        MoveSum = 0
        
        for i in range(tol):
            if nums[i] == 1:
                MoveSum += 1
                
        ans = MoveSum
        
        for i in range(tol, 2*n):
            if nums[i%n]:
                MoveSum += 1

            if nums[(i-tol)%n]:
                MoveSum -= 1
            ans = max(ans, MoveSum)
        
        return tol - ans