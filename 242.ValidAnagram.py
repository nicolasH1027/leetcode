class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        need = [0]*26
        
        for c in t:
            need[ord(c) - ord('a')] += 1
        
        for c in s:
            need[ord(c) - ord('a')] -= 1
            if need[ord(c) - ord('a')] < 0:
                return False
        return True