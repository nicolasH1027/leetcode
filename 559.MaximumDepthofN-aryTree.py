"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        "Top-Down manner"
        def helper(root, depth):
            if not root:
                return
            self.max_depth = max(self.max_depth, depth + 1)
            for child in root.children:
                helper(child, depth + 1)
        self.max_depth = 0
        helper(root, 0)
        return self.max_depth

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        "Bottom-Up manner"
        if not root:
            return 0
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        return max_depth + 1

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        "DFS Iterative"
        if not root:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0
        
        while stack:
            cur, depth = stack.pop()
            max_depth = max(max_depth, depth)
            for child in cur.children:
                stack.append((child, depth+1))
        
        return max_depth