"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        with extra space
        """
        if not root:
            return root
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            n = len(queue)
            for i in range(n):
                if i < n - 1:
                    queue[0].next = queue[1]
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        without extra space
        perfect binary tree
        recursive
        """
        
        def BFS(root):
        
            if not root:
                return 
            
            if root.left:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
            
            BFS(root.left)
            BFS(root.right)
        
        BFS(root)
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        without extra space
        perfect binary tree
        iterative
        """
        cur = root
        while cur and cur.left:
            next_level = cur.left
            while cur:
                cur.left.next = cur.right
                cur.right.next = cur.next.left if cur.next else None
                cur = cur.next
            cur = next_level
            
        
        return root