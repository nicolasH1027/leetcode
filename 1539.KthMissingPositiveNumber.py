class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        if k <= arr[0] - 1:
            return k
        
        k -= arr[0] - 1
        
        for i in range(1, len(arr)):
            gap = arr[i] - arr[i-1] - 1
            if k <= gap:
                return arr[i-1] + k
            else:
                k -= gap
        return arr[-1] + k
    

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        l, r = 0, len(arr)
        
        while l < r:
            
            pivot = l + (r - l)//2
            
            if arr[pivot] - pivot - 1 < k:
                l += 1
                
            else:
                r = pivot
        
        return l + k