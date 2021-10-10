# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):
            
            if not root:
                return None
            
            if root == p or root == q:
                return root
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            
            if left and right:
                return root
            
            return left or right
        
        res = dfs(root, p, q)
        
        if res == p or res == q:

            left = dfs(res.left, p, q)
            right = dfs(res.right, p, q)
            
            return res if left or right else None
            
        elif res != p and res != q:
            return res
        
        else:
            return None
            
            
            
            
        
        
        