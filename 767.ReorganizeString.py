class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq, n = collections.Counter(s), len(s)
        maxCount = max(freq[key] for key in freq.keys())
        
        if maxCount > (n + 1) // 2:
            return ''
        
        ans = [0]*n
        
        even, odd, harlen = 0, 1, n // 2
        
        
        for key, count in freq.items():
            
            while count and count <= harlen and odd < n:
                ans[odd] = key
                count -= 1
                odd += 2
            
            while count:
                ans[even] = key
                count -= 1
                even += 2
        
        return ''.join(ans)