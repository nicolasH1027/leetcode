class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if k == 1:
            return nums
        
        if len(nums)*k == 0:
            return []
        
        def clean(i):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
        
        queue = collections.deque()
        ans, n = [], len(nums)
        

        for i in range(k):
            clean(i)
            queue.append(i)
            
        ans.append(nums[queue[0]])

        for i in range(k, n):
            clean(i)
            queue.append(i)
            ans.append(nums[queue[0]])
        
        return ans
        
        