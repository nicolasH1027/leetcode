class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        dic = {'1': '1', '6':'9', '8':'8', '9':'6', '0':'0'}
        n = len(num)
        
        for i in range((n + 1)//2):
            
            if num[i] not in dic or dic[num[i]] != num[n - i - 1]:
                return False
            
        return True