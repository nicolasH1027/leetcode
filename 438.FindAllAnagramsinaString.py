class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []
        
        need = {}
        window = {}
        
        for c in p:
            need[c] = need.get(c, 0) + 1
        
        left, right, valid, n = 0, 0, 0, len(s)
        ans = []
        while right < n:
            
            c = s[right]
            right += 1
            
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
    
            while right - left >= len(p):
                
                if valid == len(need) and right - left == len(p):
                    ans.append(left)
                
                d = s[left]
                
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                
                left += 1
        
        return ans
                    