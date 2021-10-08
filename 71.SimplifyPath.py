class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        O(N), this question is similar with the question like Reverse Polish notation, or the calculator
        please visit the leetcode problem 
        150. Evaluate Reverse Polish Notation
        224. Basic Calculator
        """
        stack = []
        for ele in path.split('/'):
            
            if ele == '..' and stack:
                stack.pop() 
            
            elif ele not in ['', '.', '..']:
                stack.append(ele)
        return '/' + '/'.join(stack)    