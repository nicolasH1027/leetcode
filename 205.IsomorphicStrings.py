class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = [-1]*256
        t_map = [-1]*256
        
        for i in range(len(s)):
            if s_map[ord(s[i]) - ord('a')] != t_map[ord(t[i]) - ord('a')]:
                return False
            s_map[ord(s[i]) - ord('a')] = i
            t_map[ord(t[i]) - ord('a')] = i
            
        return True
    
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))