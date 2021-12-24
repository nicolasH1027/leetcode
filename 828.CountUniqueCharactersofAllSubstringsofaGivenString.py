class Solution:
    def uniqueLetterString(self, s: str) -> int:
        
        pos, n = collections.defaultdict(list), len(s)
        
        for c in s:
            pos[c].append(-1)
        
        for i, c in enumerate(s):
            pos[c].append(i)
            
        for c in s:
            pos[c].appned(n)
            
        ans = 0
        
        for c in pos.keys():
            m = len(pos[c])
            cnt, tmp = 0, pos[c]
            for i in range(1, m+1):
                cnt += (tmp[i+1] - tmp[i]) * (tmp[i] - tmp[i-1])
            ans += cnt
        
        return ans