class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Not very intuitive way
        """
        dig = [int(i) for i in str(num)]
        
        x, y, max_ind = 0, 0, len(dig) - 1
        
        for i in range(len(dig)-1, -1, -1):
            if dig[i] > dig[max_ind]:
                max_ind = i
            elif dig[i] < dig[max_ind]:
                x = i
                y = max_ind
        
        dig[x], dig[y] = dig[y], dig[x]
        
        
        

        
        return res
    

class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Straight forward way
        """
        dig = [int(i) for i in str(num)]
        dic = {x:i for i, x in enumerate(dig)}
        
        res = 0
        for i in range(len(dig)):
            
            for j in range(9, dig[i], -1):
                if j in dic and dic[j] > i:
                    dig[i], dig[dic[j]] = dig[dic[j]], dig[i]
                    for i in range(len(dig)):
                        res = res*10 + dig[i]
                    return res
                    
        for i in range(len(dig)):
            res = res*10 + dig[i]            
        
        return res