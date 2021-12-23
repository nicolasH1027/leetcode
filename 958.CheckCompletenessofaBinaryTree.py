# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        prev_null = False
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            
            cur = queue.popleft()
            if not cur:
                prev_null = True
            else:
                if prev_null:
                    return False
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)
        
        return True
            
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        self.pos = 0
        self.cnt = 0
        
        def helper(root, pos):
            
            if not root:
                return 
            
            self.cnt += 1
            
            self.pos = max(self.pos, pos)
            
            helper(root.left, 2*pos)
            helper(root.right, 2*pos + 1)
        
        helper(root, 1)
        
        return self.pos == self.cnt
                
                
            
        