class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lpt, rpt = 0, len(s) - 1
        
        while lpt < rpt:
            
            if not s[lpt].isalnum():
                lpt += 1
                continue
            
            if not s[rpt].isalnum():
                rpt -= 1
                continue
            
            if s[lpt].lower() == s[rpt].lower():
                lpt += 1
                rpt -= 1
            else:
                return False
            
        
        return True