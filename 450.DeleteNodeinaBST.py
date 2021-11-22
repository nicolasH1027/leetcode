# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return
        
        if root.val == key:
            root = self.delete(root)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
            
        return root
            
            
    def delete(self, root):
        
        "use Precursor to replace the root"
        
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            node = root
            rightmost = root.left
            while rightmost.right:
                node = rightmost
                rightmost = rightmost.right
            root.val = rightmost.val
            if node != root:
                node.right = rightmost.left
            else:
                root.left = rightmost.left
            
            return root