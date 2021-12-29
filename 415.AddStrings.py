class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        num1, num2 = num1.zfill(n), num2.zfill(n)
        
        ans, carry = collections.deque(), 0
        
        for i in range(n-1, -1, -1):
            
            carry, digit = divmod(ord(num1[i]) + ord(num2[i]) - 2*ord('0') + carry, 10)
            
            ans.appendleft(str(digit))
        
        if carry:
            ans.appendleft('1')
        
        return ''.join(ans)