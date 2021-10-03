class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        iterate the string
        """
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        carry = 0
        res = []
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1    
            if carry % 2 == 1:
                res.append('1')
            else:
                res.append('0')
            carry //= 2
        if carry == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)
        
            
        
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Bitwise operation
        
        and:  &   this gives you the carry, but remember to shift it to the left
        1 0 1 0
        1 1 0 0
        
        1 0 0 0
        
        << this will shift your binary number to the left by one position
        
        1 0
        1 0 0
        
        XOR, ^  this will help you do the actual addition
        
        1 0 1 0
        1 1 0 0
        
        0 1 1 0
        
        """
        
        a, b = int(a, 2), int(b, 2)
        
        while b:
            
            tmp = a & b
            
            a = a ^ b
            
            b = tmp << 1
        
        return bin(a[2:])
            
            
        
        
        
        