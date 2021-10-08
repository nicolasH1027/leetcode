# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        the most straight way to do this is to travese
        the all tree inorder, then build the balanced tree
        which is the 
        108. Convert Sorted Array to Binary Search Tree
        """
        
        res = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root)
            
            inorder(root.right)
        
        inorder(root)
        
        def build(ls):
            if not ls:
                return None
            
            mid = len(ls) // 2
            
            root = ls[mid]
            root.left = build(ls[:mid])
            root.right = build(ls[mid+1:])
            
            return root
        
        return build(res)    