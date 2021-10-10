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