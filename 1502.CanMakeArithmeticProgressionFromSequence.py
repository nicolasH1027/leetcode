class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        O(N) time complexity,  O(1) space complexity
        """
        
        m = min(arr)
        dif = (max(arr) - m) / (len(arr) - 1)
        
        # all value are the same
        if dif == 0: return True
        
        pt = 0
        
        while pt < len(arr):
            
            if arr[pt] == m + pt*dif:
                pt += 1
            else:
                dis = arr[pt] - m
                if dis % dif != 0: return False
                pos = int(dis / dif)
                if arr[pos] == arr[pt]: return False
                arr[pos], arr[pt] = arr[pt], arr[pos]
        return True
        
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        O(N) time, O(N) space
        """
        
        m = min(arr)
        
        dif = (max(arr) - m) / (len(arr) - 1)
        
        if dif == 0: return True
        
        unique = set()
        
        for val in arr:
            if (val - m) % dif != 0:
                return False
            unique.add(val)
        
        return len(unique) == len(arr)