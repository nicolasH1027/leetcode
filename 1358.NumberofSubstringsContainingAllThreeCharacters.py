class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        need = {}
        window = {}
        for c in 'abc':
            need[c] = need.get(c, 0) + 1
        
        left, right, valid, n = 0, 0, 0, len(s)
        ans = 0
        
        while right < n:
            
            c = s[right]

            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1
            
            while valid == 3:
                d = s[left]
                left += 1
                
                ans += n - right
                
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
        right += 1
        
        return ans