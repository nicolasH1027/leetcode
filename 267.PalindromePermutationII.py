class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        
        
        def backtrack(par):
            if len(par) == len(s):
                ans.append(par)
            
            for key in freq.keys():
                if freq[key] - 2 < 0: continue
                freq[key] -= 2
                backtrack(key + par + key)
                freq[key] += 2                
                
                
        ans = []
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        odd = []
        
        for key in freq.keys():
            if freq[key] % 2 != 0:
                odd.append(key)
        
        if len(odd) > 1:
            return []
        
        elif len(odd) == 1:
            backtrack(odd[0])
        else:
            backtrack('')
        return ans
        
        