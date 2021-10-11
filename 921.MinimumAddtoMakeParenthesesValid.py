class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        res = 0
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
            else:
                if count:
                    count -= 1
                else:
                    res += 1

        return res + count
        
        
        
        
        
        
        
        
#         stack = []
#         for ch in s:
#             if ch == '(':
#                 stack.append(ch)
#             else:
#                 if stack and stack[-1] == '(':
#                     stack.pop()
#                 else:
#                     stack.append(ch)
        
#         return len(stack)