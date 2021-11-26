class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {}
        window = {}
        
        for c in t:
            need[c] = need.get(c, 0) + 1
            
        left, right, valid, n, size = 0, 0, 0, len(s), float('inf')
        
        while right < n:
            
            c = s[right]
            
            right += 1
            
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            while valid == len(need):
                if right - left < size:
                    ans = left, right
                    size = right - left
                    
                d = s[left]
                
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    
                left += 1
        
        return '' if size == float('inf') else s[ans[0]:ans[1]] 
    


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {}
        window = {}
        
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        filter_s = []
        
        for i, c in enumerate(s):
            if c in need:
                filter_s.append((i, c))
                
            
        left, right, valid, n, size = 0, 0, 0, len(filter_s), float('inf')
        
    
        
        while right < n:
            
            c = filter_s[right][1]
            
            
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1
                
            while valid == len(need):
                d = filter_s[left][1]
                
                end = filter_s[right][0]
                start = filter_s[left][0]
                
                if end - start + 1 < size:
                    size = end - start + 1
                    ans = size, start, end
                if window[d] == need[d]:
                    valid -= 1
                    
                window[d] -= 1
                
                left += 1
            right += 1
            
        return '' if size == float('inf') else s[ans[1]:ans[2]+1]
                
                
            