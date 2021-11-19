# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        in_map = {val:i for i, val enumerate(inorder)}
        
        def helper(left, right):
            if left > right: return None
            ind = in_map[postorder.pop()]
            root = TreeNode(inorder[ind])
            root.right = helper(ind+1, right)
            root.left = helper(left, ind - 1)
            return root
        
        return helper(0, len(inorder) - 1)
        