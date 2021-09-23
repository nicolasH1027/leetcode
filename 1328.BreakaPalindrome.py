class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        since its palindrome, we only need to traverse left half of the string
        replace the first non 'a' string into 'a'
        if all are 'a'
        then change the last one into 'b'
        """
        n = len(palindrome)
        if n == 1:
            return ""
        
        for i in range( n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
            
        return palindrome[:-1] + 'b'