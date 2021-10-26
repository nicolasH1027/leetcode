class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if haystack == "" and needle == "":
            return 0
        
        if len(haystack) < len(needle):
            return -1
        
        if len(needle) == 0:
            return 0
        
        i = 0
        j = 0   
        next_arr = self.getNext(needle)
            
        while i < len(haystack)   and j < len(needle) :
            
            if j == -1 or haystack[i] == needle[j]:
                
                j += 1
                i += 1
            
            else:
                
                j = next_arr[j]
        
        if j == len(needle):
            
            return i - j
        
        return -1

    
    def getNext(self, needle: str) -> List[int]:
        
        next_arr = [-1]*len(needle)
        
        i = 0
        j = -1
        
        while i < len(needle) - 1:
            
            if j == -1 or needle[i] == needle[j]:
                
                j += 1
                i += 1
                
                if needle[i] != needle[j]:
                    next_arr[i] = j
                else:
                    next_arr[i] = next_arr[j]
                
            else:
                
                j = next_arr[j]
                
        return next_arr