class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        operand = 0
        sign = '+'
        
        for i, c in enumerate(s):

            if c.isdigit():
                operand = 10*operand + int(c)
                
            if not c.isdigit() and c != ' ' or i == len(s) - 1:
                if sign == '+':
                    stack.append(operand)
                
                elif sign == '-':
                    stack.append(-operand)
                
                elif sign == '*':
                    pre = stack.pop()
                    stack.append(pre*operand)
                
                elif sign == '/':
                    pre = stack.pop()
                    stack.append(int(pre/operand))
                    
                operand = 0
                sign = c
        
        return sum(stack)

class Solution:
    def calculate(self, s: str) -> int:
        
        prev = operand = result = 0
        sign = '+'
        
        for i, c in enumerate(s):
            
            if c.isdigit():
                operand = 10*operand + int(c)
                
            if not c.isdigit() and c != ' ' or i == len(s) - 1:
                
                if sign == '+':
                    result += prev
                    prev = operand
                elif sign == '-':
                    result += prev
                    prev = -operand
                elif sign == '*':
                    prev *= operand
                elif sign == '/':
                    prev = prev / operand
                    prev = int(prev)
                
                sign = c
                operand = 0
            
        result += prev

        return result