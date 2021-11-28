class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        map_order = {}
        map_s = [0]*len(order)
        rest = []
        
        for i, c in enumerate(order):
            map_order[c] = i
        
        ans = []
        
        for c in s:
            if c not in map_order:
                ans.append(c)
            else:
                map_s[map_order[c]] += 1
                
        for i, val in enumerate(map_s):
            tmp = order[i]*val
            ans.append(tmp)
        
        
        return ''.join(ans)