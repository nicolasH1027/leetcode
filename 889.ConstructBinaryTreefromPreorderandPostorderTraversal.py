# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre, post):    
        def build(i, j, n):
            if n <= 0: return None
            root = TreeNode(pre[i])
            if n == 1: return root
            k = ind[pre[i + 1]]      
            l = k - j + 1      
            root.left = build(i + 1, j, l)
            root.right = build(i + l + 1, k + 1, n - l - 1)
            return root
        
        ind = {val:i for i, val in enumerate(post)}
        
        return build(0, 0, len(pre))
