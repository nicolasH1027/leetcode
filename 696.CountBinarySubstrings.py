class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        O(N) time, O(N) space
        """
        
        count = [1]
        
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                count.append(1)
            else:
                count[-1] += 1
        res = 0
        for i in range(len(count) - 1):
            res += min(count[i], count[i+1])
        
        return res

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count, prev, cur = 0, 0, 1
        
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                count += min(cur, prev)
                prev, cur = cur, 1
            else:
                cur += 1
                
        return count + min(cur, prev)
                
        
        