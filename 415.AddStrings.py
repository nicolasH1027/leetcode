class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        n = max(len(num1), len(num2))
        num1 = num1.zfill(n)
        num2 = num2.zfill(n)
        
        carry = 0
        result = []
        for i in range(n-1, -1, -1):
            tmp = ord(num1[i]) + ord(num2[i]) - 2*ord('0')
            
            carry, val = divmod(tmp + carry, 10)
            
            result.append(str(val))
            
        
        if carry == 1:
            result.append('1')
            
        result.reverse()
        
        return ''.join(result)
            
            