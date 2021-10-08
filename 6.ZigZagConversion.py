class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        ABCDEFGHIJK  3
        
        A    E    I  1
        B  D F  H K  2
        C    G       3
        
        1 2 3 2 1 2 3 .....
        
        A       G   
        B    F  H     K
        C  E    G   J
        D       I
        1 2 3 4 3 2 1 2 ....
        
        It's like the leaf node travse, while require you to cluster the leaf node into the same cluster
        """
        
        if numRows == 1:
            return s
        
        result = [""]*numRows
        
        ind = 0
        increase = True
        
        for ch in s:
            result[ind] += ch
            if ind == numRows - 1:
                increase = False
                
            if increase:
                ind += 1
            else:
                ind -= 1
            
            if ind == 0:
                increase = True
        
        return "".join(result)
    
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        """
        0        8
        1      7 9
        2    6   10
        3  5     11
        4        12 
        """

        if numRows == 1:
            return s
        
        res = [""]*numRows
        interval = 2*numRows - 2
        
        # for the first line
        for i in range(0, len(s), interval):
            res[0] += s[i]
        
        # for the middle line
        for i in range(1, numRows - 1):
            
            flag = 1
            j = i
            while j < len(s):
                res[i] += s[j]
                if flag:
                    j += interval - 2*i
                else:
                    j += 2*i
                flag += 1
                flag %= 2

        # for the last line
        for i in range(numRows-1, len(s), interval):
            res[numRows-1] += s[i]
        
        return "".join(res)
        