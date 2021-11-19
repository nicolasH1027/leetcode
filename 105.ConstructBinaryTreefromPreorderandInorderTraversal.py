# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        
        preorder = collections.deque(preorder) 
        inorder_map = {n:i for i, n in enumerate(inorder)}
		
        def build_tree(start, end):
            if start > end: return None
            root_index = inorder_map[preorder.popleft()]
            root = TreeNode(inorder[root_index])
            root.left = build_tree(start, root_index-1)
            root.right = build_tree(root_index+1, end)
            return root
        
        return build_tree(0, len(inorder)-1)