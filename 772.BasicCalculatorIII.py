class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        sign = '+'
        operand = 0
        
        def op(num, sign, stack):
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                stack[-1] = int(stack[-1] / num)
            else:
                pass
        
        for i, c in enumerate(s):

            if c.isdigit():
                operand = 10*operand + int(c)
                
            if not c.isdigit() or i == len(s) - 1:
                
                if c != '(':
                    op(operand, sign, stack)
                    if c == ')':
                        tmp = 0
                        while isinstance(stack[-1], int):
                            tmp += stack.pop()
                        operation = stack.pop()
                        op(tmp, operation, stack)
                    operand, sign = 0, c
                else:
                    stack.append(sign)
                    operand, sign = 0, '+'
                    
        return sum(stack)