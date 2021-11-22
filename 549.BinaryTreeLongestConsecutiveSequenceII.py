# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.maxlength = -float('inf')
        
        def helper(root):
            
            if not root:
                return [0, 0]
            
            lin, ldr = helper(root.left)
            rin, rdr = helper(root.right)
            
            cin = cdr = 1
            
            if root.left:
                if root.left.val == root.val + 1:
                    cin = lin + 1
                elif root.left.val == root.val - 1:
                    cdr = ldr + 1
            
            if root.right:
                if root.right.val == root.val + 1:
                    cin = max(cin, rin + 1)
                elif root.right.val == root.val - 1:
                    cdr = max(cdr, rdr + 1)
                    
            self.maxlength = max(self.maxlength, cin + cdr - 1)
            
            return [cin, cdr]
        
        helper(root)
        
        return self.maxlength