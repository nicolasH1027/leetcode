class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        def LIS(nums):
            
            ans = [0]*n
            
            stack = []
            
            for i, val in enumerate(nums):
                
                ind = bisect.bisect_left(stack, val)
                
                if ind == len(stack):
                    
                    stack.append(val)
                
                else:
                    
                    stack[ind] = val
                
                ans[i] = len(stack)
                
            return ans
        
        l, r = LIS(nums), LIS(nums[::-1])[::-1]
        
        ans = float('inf')
        
        for i in range(n):
            
            if l[i] > 1 and r[i] > 1:
                ans = min(ans, n - l[i] - r[i] + 1)
            
        
        return ans