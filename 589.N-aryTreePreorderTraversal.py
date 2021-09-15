"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        "Recursion Version"
        def dfs(node):
            if not node:
                return []
            cur = [node.val]
            for child in node.children:
                cur += dfs(child)
            return cur
        return dfs(root)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        "Iterative Version"
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            stack.extend(cur.children[::-1]) # be careful the order here
        return result