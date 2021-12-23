class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ans = 0
        operand = 0
        sign = 1
        
        
        for c in s:
            
            if c.isdigit():
                operand = 10*operand + int(c)
            
            if c == '+':
                ans += operand*sign
                sign = 1
                operand = 0
            
            if c == '-':
                ans += operand*sign
                sign = -1
                operand = 0
            
            if c == '(':
                stack.append(ans)
                stack.append(sign)
                sign = 1
                ans = 0
            
            if c == ')':
                ans += sign*operand
                ans *= stack.pop()
                ans += stack.pop()
                sign = 1
                operand = 0
        
        return ans + sign*operand