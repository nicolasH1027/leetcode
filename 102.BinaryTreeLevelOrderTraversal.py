# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import collections


class Solution:
    "Iterative Version"
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            n = len(queue)
            tmp = []
            for _ in range(n):
                cur = queue.popleft()
                tmp.append(cur.val)
                for node in [cur.left, cur.right]:
                    if node:
                        queue.append(node)
            result.append(tmp)
        return result
                        
            
        

class Solution:
    "Recursion Version"    
    def levelOrder(self, root):
        result = []
        if not root:
            return result
        def BFS(root, level):               # unlike the iterative method, we need a variable of level to help us keep track of the level of the node
            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            for node in [root.left, root.right]:
                if node:
                    BFS(node, level + 1)
        BFS(root, 0)
        return result
            
             
            
    


        
        
            
        