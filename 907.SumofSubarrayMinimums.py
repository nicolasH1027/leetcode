class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        n = len(arr)
        left, right, lstack, rstack = [0]*n, [0]*n, [], []
        
        for i in range(n):
            sub = 1
            while lstack and lstack[-1][0] > arr[i]:
                sub += lstack.pop()[1]
            
            lstack.append((arr[i], sub))
            left[i] = sub
        
        for i in range(n-1, -1, -1):
            sub = 1
            while rstack and rstack[-1][0] >= arr[i]:
                sub += rstack.pop()[1]
            
            rstack.append((arr[i], sub))
            right[i] = sub
            
        
        ans = 0
        
        for i in range(n):
            ans += arr[i]*left[i]*right[i]
            
        return ans % (10**9 + 7)
    
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        """
        我们需要一个单调递减栈（这里定义的递减是指stack从左往右递减）
        这个栈用来维护原数组元素递减的index，换句话说，栈内元素对应的
        原数组中的元素是递减的。这样我们就能找到left和right了
        """
        
        ans = 0
        "头尾两个哨兵变量可以保证首尾元素也能被考虑到"
        nums = [0] + arr + [0]
        stack = []
        
        for i, val in enumerate(nums):
            
            while stack and nums[stack[-1]] > val:
                j = stack.pop()
                k = stack[-1]
                ans += nums[j]*(i - j)*(j - k)
            
            stack.append(i)
        
        return ans % (10**9 + 7)
            
        