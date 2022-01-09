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