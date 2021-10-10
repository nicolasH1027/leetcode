"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        O(N) time, O(N) for worse case, O(H) for balanced case
        """
        path = set()

        while p:
            path.add(p.val)
            p = p.parent
        
        while q:
            if q.val in path:
                return q
            q = q.parent
        
        return
    
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        O(N) time, O(1)
        """
        
        p1, p2 = p, q
        
        while p1 != p2:
            "by this way, p and q will traverse the same distance"
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        
        return p1
        
        
        