class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        "这题把907的答案运用两次就可以了，分别求出最大和最小，最小的加符号，然后加起来"
        
        "求最小"
        
        ans, arr = 0, [-float('inf')] + nums + [-float('inf')]
        stack = []
        for i, val in enumerate(arr):
            while stack and arr[stack[-1]] > val:
                j = stack.pop()
                k = stack[-1]
                ans -= arr[j]*(i - j)*(j - k)
            stack.append(i)
            
        arr = [float('inf')] + nums + [float('inf')]
        stack = []
        
        for i, val in enumerate(arr):
            while stack and arr[stack[-1]] < val:
                j = stack.pop()
                k = stack[-1]
                ans += arr[j]*(i - j)*(j - k)
            stack.append(i)
        
        return ans
        