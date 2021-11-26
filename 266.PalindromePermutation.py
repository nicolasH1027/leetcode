class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        dic = {}
        
        for c in s:
            dic[c] = dic.get(c, 0) + 1
            
        cnt = 0
        
        for key in dic.keys():
            cnt += dic[key] % 2
            
        return cnt <= 1