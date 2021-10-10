"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        
        O(NlogN), time, O(N) space
        """
        
        self.path = 0
        
        def dfs(root):
            if not root.children:
                return 1
            
            res = [dfs(i) for i in root.children]
            
            if len(res) == 1:
                self.path = max(self.path, res[0])
            else:
                res.sort()
                self.path = max(self.path, res[-1] + res[-2])
            
            return res[-1] + 1                    
        
        dfs(root)
        
        return self.path

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        
        O(NlogN), time, O(N) space
        """
        
        self.path = 0
        
        def dfs(root):
            if not root.children:
                return 1
            
            first, second = 0, 0
            
            for child in root.children:
                length = dfs(child)
                if length > first:
                    first, second = length, first
                elif length > second:
                    second = length
                    
            self.path = max(self.path, first + second)
            
            return max(first, second) + 1               
        
        dfs(root)
        
        return self.path