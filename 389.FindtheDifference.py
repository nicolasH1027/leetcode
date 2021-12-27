class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        """
        a is a number

        a ^ a = 0
        a ^ 0 = a

        a^b^a = a^a^b
        """
        
        ans = 0
        
        for c in s:
            ans ^= ord(c)
        
        for c in t:
            ans ^= ord(c)
            
        return chr(ans)