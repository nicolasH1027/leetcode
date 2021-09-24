class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cur = len(s) - 1
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                length = cur - i
                cur -= 1
                
            if length > 0:
                return length
        return cur + 1
            