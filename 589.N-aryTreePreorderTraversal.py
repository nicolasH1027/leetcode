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
        def helper(root):
            if not root:
                return
            result.append(root.val)
            for child in root.children:
                helper(child)
        result = []
        helper(root)
        return result

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            for i in range(len(cur.children) - 1, -1, -1):
                stack.append(cur.children[i])
        return result
        
    
    
    
    
    
    


# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         "Iterative Version, not efficient"
#         if not root:
#             return []
#         stack = [root]
#         result = []
#         while stack:
#             cur = stack.pop()
#             result.append(cur.val)
#             stack.extend(cur.children[::-1]) # be careful the order here
#         return result