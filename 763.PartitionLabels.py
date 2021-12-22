class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        freq = collections.Counter(s)
        
        ans, cnt, need = [], 0, {}
        
        for c in s:
            
            need[c] = need.get(c, 0) + 1
            
            if need[c] == freq[c]:
                cnt += 1
                
            if cnt == len(need):
                
                tol = sum([need[key] for key in need.keys()])
                ans.append(tol)
                need = {}
                cnt = 0
        return ans
            
            
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        rightmost = {key:i for i, key in enumerate(s)}
        
        
        ans, curright, left = [], 0, -1
        
        for i, c in enumerate(s):
            
            curright = max(curright, rightmost[c])
            
            if curright == i:
                ans.append(curright - left)
                left = i
        
        return ans
            
            
            
        