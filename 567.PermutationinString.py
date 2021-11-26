class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}
        
        for c in s1:
            need[c] = need.get(c, 0) + 1
            
        left, right, valid, n = 0, 0, 0, len(s2)
        
        while right < n:
            
            c = s2[right]
            right += 1
            
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            while right - left >= len(s1):
                
                if valid == len(need):
                    return True
                
                d = s2[left]
                
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                left += 1
        return False
            
                