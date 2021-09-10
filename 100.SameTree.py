# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Collection


class Solution:
    "Recursion Version"
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(p, q):
            if not p and not q:
                return True
            
            if not p and q:
                return False
            
            if p and not q:
                return False
            
            if p.val != q.val:
                return False
            return True
        
        
        return helper(p.left, q.left) and helper(p.right, q.right)
    

class Solution:
    "Iterative Version"
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        from collections import deque
        queue = deque()
        queue.append((p, q))
        while queue:
            a, b = queue.popleft()
            if not a and not b:
                continue
            if not a and b:
                return False
            if a and not b:
                return False
            if a.val != b.val:
                return False
            queue.append((a.left, b.left))
            queue.append((a.right, b.right))
        return True        