class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        O(N) time, O(N - d) where d is the replicate
        
        I think in python, the space complexity is at least  O(N - d),
        
        cause string is immutable in python
        """
        stack = []
        
        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
                
        return "".join(stack)
    


class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]
            
            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
            
        return ''.join(res[0: slow])