"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

from BST import Node


class Solution:
    "Iterative Version"
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return 
        
        stack = []
        prev = Node(0)
        head, cur = prev, root
 
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            
            prev.right = cur
            cur.left = prev
            prev = cur
            
            cur = cur.right
        
        head.right.left = prev
        prev.right = head.right
        
        return head.right
            
class Solution:
    "Recursion Version"
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return 
        head = Node(0)
        prev = None
        self.InorderDFS(root)
        self.prev.right =  self.head.right
        self.head.right.left = self.prev
        return self.head.right
    
    def InorderDFS(self, root):
        if not root: return 
    
        self.InorderDFS(root.left)
        "============================================================"
        if self.prev:
            self.prev.right = root
            root.left = self.prev
        else:
           self.head.right = root
        self.prev = root
        "============================================================"
        self.InorderDFS(root.right)
        
            
            
        
