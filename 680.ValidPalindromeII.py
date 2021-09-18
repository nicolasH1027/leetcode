class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid(s):
            lo, hi = 0, len(s)-1
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True
        
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return is_valid(s[:lo] + s[lo+1:]) or is_valid(s[:hi] + s[hi+1:])
            lo += 1
            hi -= 1
        return True
    