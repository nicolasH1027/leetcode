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
        
        if not root:
            return None
        
        queue = collections.deque([root])
        
        while queue:
            n = len(queue)
            prev = queue.popleft()
            if prev.left:
                queue.append(prev.left)
            if prev.right:
                queue.append(prev.right)
                
            for i in range(1, n):
                tmp = queue.popleft()
                prev.next = tmp
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
                prev = tmp
                
        return root
    

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        queue = collections.deque([root])
        
        while queue:
            n = len(queue)
                
            for i in range(n):
                tmp = queue.popleft()
                if i < n - 1:
                    tmp.next = queue[0]
                
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
                
        return root
    
