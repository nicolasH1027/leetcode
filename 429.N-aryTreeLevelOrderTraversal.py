"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        "Recursion Version"
        if not root:
            return []
        def BFS(root, level):
            if len(result) == level:
                result.append([])
            
            result[level].append(root.val)
            for child in root.children:
                BFS(child, level+1)
        result = []
        BFS(root, 0)
        return result
    
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        "Iterative Version"
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
            n = len(queue)
            tmp = []
            for _ in range(n):
                cur = queue.popleft()
                tmp.append(cur.val)
                for child in cur.children:
                    queue.append(child)
            result.append(tmp)
        return result
        