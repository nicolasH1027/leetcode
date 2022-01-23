# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        l, r = 0, mountain_arr.length()
        
        while l < r:
            
            mid = l + (r - l)//2
            
            if mountain_arr.get(mid) < mountain_arr.get(mid-1):
                
                r = mid
                
            else:
                
                l = mid + 1
        
        peak = l - 1

        
        l, r = 0, peak + 1
        
        while l < r:
            
            mid = l + (r - l)//2
            
            mid_val = mountain_arr.get(mid)
            
            if mid_val == target:
                return mid
            
            elif mid_val < target:
                
                l = mid + 1
                
            else:
                
                r = mid
                
        l, r = peak + 1, mountain_arr.length()

        while l < r:
            
            mid = l + (r - l)//2

            mid_val = mountain_arr.get(mid)
            
            if mid_val == target:
                return mid
            
            elif mid_val < target:
                
                r = mid
                
            else:
                
                l = mid + 1
        
        return -1
            