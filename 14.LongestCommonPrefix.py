class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortstr = min(strs, key=len)
        
        for i, ch in enumerate(shortstr):
            for j in strs:
                if j[i] != ch:
                    return shortstr[:i]
        
        return shortstr
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        minlen = min([len(i) for i in strs])
        
        res = ""
        
        for i in range(minlen):
            
            tmp = []
            
            for j in strs:
                
                tmp.append(j[i])
            
            if all(item == tmp[0] for item in tmp):
                res += tmp[0]
            
            else:
                break
        
        return res