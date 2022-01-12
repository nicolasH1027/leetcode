class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        for c in s:
            
            if c == ']':
                
                tmp = []
                while stack[-1] != '[':
                    tmp.append(stack.pop()) 
                stack.pop()
                
                k, expo = 0, 1
                while stack and stack[-1].isdigit():
                    k += int(stack.pop())*10**(expo - 1)
                    expo += 1

                ele = ''
                while tmp:
                    ele += tmp.pop()

                stack.append(ele*k)
            
            else:
                stack.append(c)
        
        return ''.join(stack)