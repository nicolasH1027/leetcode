class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        cnt = 0
        for i, ch in enumerate(s):
            if ch == '(':
                cnt += 1
                stack.append(i)
            if ch == ')':
                cnt -= 1
                if cnt < 0:
                    stack.append(i)
                    cnt = 0
                else:
                    stack.pop()
                    
        stack = set(stack)
        
        res = []
        
        for i, ch in enumerate(s):
            if i in stack:
                continue
            res.append(ch)
        
        return ''.join(res)