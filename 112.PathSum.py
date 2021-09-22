# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        "Recursion"
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0 
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return
        
        stack = [(root, root.val)]
        
        while stack:
            cur, value = stack.pop()
            
            if value == targetSum:
                return True
            
            if cur.left:
                stack.append((cur.left, value + cur.left.val))
            
            if cur.right:
                stack.append((cur.right, value + cur.right.val))      
        return False 